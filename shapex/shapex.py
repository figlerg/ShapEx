import numpy as np
from anyHR.hit_and_run.hit_and_run import *

from SpecLoaderVisitor import SpecLoaderVisitor
from expression.Expression import Expression, WordSamplerMode
from generation_tool.generate_traces import to_typestring, atomic_gen
from misc.visualize import plotter
from parse.generated.ShapeExpressionLexer import *
from parse.generated.ShapeExpressionParser import *
from parse.se2sa.SyntaxError import HardSyntaxErrorStrategy
import tqdm


class ShapEx(object):
    def __init__(self, timestep=1.0,
                 word_sampler=WordSamplerMode.SEARCH, search_budget=100, target_word_length=0,
                 dir_sampling=DirectionSampling.RDHR, shrinking=Shrinking.NO_SHRINKING, init_point=InitPoint.PSO,
                 noise_dist='uniform', mu=0, sigma=0):
        self._expression = None  # new.
        self._constraint = None  # from anyHR
        self._hr = None  # from anyHR

        self._timestep = timestep

        # params for word sampling
        self.word_sampler = WordSamplerMode.SEARCH
        self._word_sampler = word_sampler
        self._search_budget = search_budget
        self._target_word_length = target_word_length

        # params for valuation sampling
        self._dir_sampling = dir_sampling
        self._shrinking = shrinking
        self._init_point = init_point

        # params for noise sampling
        self.noise_dist = noise_dist
        self.mu = mu
        self.sigma = sigma

    # TODO getters setters of these vars (property). constraint setter should reinitialise hr. hr setter should override
    #  self._constraint. make public again, since it should be possible to do it without sx file

    def sample(self):
        path = self._expression.sample()
        params, rejections = self._hr.next_sample()
        params = np.concatenate((params,np.asarray(list(self._constants.values()))))
        # TODO this casting is probably impeding performance

        self._hr: HitAndRun

        index = dict([(name,i) for i,name in enumerate(self._hr.constraint.var_name_list)])
        for item in self._constants.items():
            index[item[0]] = len(index)

        example = self._create_example(path, params, index)

        # generate ideal example
        return example

    def samples(self, n):
        out = []
        for i in tqdm.tqdm(range(n),desc='Samples generated', position=0, leave=True):
            out.append(shapex.sample())

        return out



    # do n samples

    def _create_example(self, path, param_values, index):
        trace = []  # [x_val, y_val, mse, last_point]

        for letter in path:

            letter_type = to_typestring(letter)

            param_vars = letter.get_param_list(return_constant=True)

            param_values_selected = [param_values[index[var]] for var in param_vars]
            # now param_values are in the right order for input in atomic_gen

            if not trace:
                start = (0, 0)  # relative offset gets added later in atomic gen

                trace = atomic_gen(param_values_selected, letter_type, dist_mode=self.noise_dist, timestep=self._timestep,
                                   start=start)

                settings_labels = [(parameter, param_values[index[parameter]])
                                   for parameter in param_vars]
                # these are global, need only look at first segment

                trace.insert(3, settings_labels)
            else:
                start = (trace[-1][0], 0)  # again, relative offset is added in atomic_gen
                new_segment = atomic_gen(param_values_selected, letter_type, dist_mode=self.noise_dist, timestep=self._timestep, start=start)

                trace[0] = np.concatenate((trace[0], new_segment[0]))
                trace[1] = np.concatenate((trace[1], new_segment[1]))
                trace[2] = max(trace[2], new_segment[2])  # mse of concat is max of both

                trace[-1] = new_segment[-1]

        return trace

    # add_noise

    def add_shape_expression(self, file_path: str):
        input_stream = FileStream(file_path)

        # process specification
        lexer = ShapeExpressionLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShapeExpressionParser(stream)
        parser._errHandler = HardSyntaxErrorStrategy()
        ctx = parser.shape_expression()

        # translate to regular expression object
        visitor = SpecLoaderVisitor()
        reg_exp, bounds_dict, constraints, singletons_dict = visitor.visit(ctx)

        self._expression = reg_exp
        self._constraint = constraints
        bounding_box = list([(item[1].start, item[1].end) for item in bounds_dict.items()])

        self._hr = HitAndRun(constraints, bounding_box, self._dir_sampling, self._shrinking, self._init_point)
        self._constants = singletons_dict


# opening file and generating _expression, etc


if __name__ == '__main__':
    filename = r"C:\Users\giglerf\Documents\dev\ShapEx\examples\example_after_refactoring.sx"

    shapex = ShapEx()

    shapex.add_shape_expression(filename)

    testexp = shapex._expression

    testexp: Expression

    testexp.set_sampler()

    print(testexp.sample())



    plotter(shapex.samples(1000))


