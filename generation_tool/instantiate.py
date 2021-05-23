import numpy as np
import itertools
from bisect import bisect
from tqdm import tqdm

# from uniform_SMT.aut2sampling_matrix import sampling_matrix
# from uniform_SMT.uniform_polytope import sampler
from typing import Dict, Set, List
from parse.se2sa.interval import IntervalObject
from parse.se2sa.automaton import ShapeAutomatonContainer
from parse.se2sa.automaton import RelationObject

from sympy import StrictLessThan, StrictGreaterThan, LessThan, GreaterThan

# Dejan's code as of 2021/01
from sampling.constraint.constraints import Constraints
from sampling.hit_and_run.hit_and_run import HitAndRun


def instantiate(params: tuple, param_interval_map: dict, density: int, seed: int, uniform_sampling=False, n=None,
                relational_input=False, aut: ShapeAutomatonContainer = None, non_integer_durations=False, timestep=1.0,
                handle_nonlin_constr = False):
    # added uniform sampling mode -> instead of iteration, it samples uniformly on the n-rectangle
    # TODO these input parameters need to be checked. right now, relational input overwrites other modes

    # RELATIONAL SAMPLING MODE
    if relational_input:
        if uniform_sampling:
            print('WARNING: detected relational input. Uniform sampling parameter has no effect, this implementation '
                  'only works for strictly interval-based input. You can disregard this warning or \n'
                  "1) not use parameter '--param_sampling' or '-ps'\n"
                  '2) clear the specification of any relational input')
            # THIS SHOULD NEVER HAPPEN, changed main
            uniform_sampling = False
        assert aut != None, "'instantiate' function needs whole automaton container for relational input mode."

        shape_param: Set[str] = list(aut.shape_param.copy()) # list fixes the order
        intervals: Dict[str, IntervalObject] = aut.intervals.copy()
        relations: List[RelationObject, str] = aut.relations.copy()

        # A,b, bin = sampling_matrix(aut)
        # this is actually unnecessary when I use Dejan's code, but useful for getting the number of variable parameters
        # TODO maybe get rid of it

        index: Dict[str, int] = {}

        # TODO the indexing here is not nice, this is due to the constant parameters needing different handling
        #  refactor?
        var_param_count = 0
        for param in shape_param:
            try:
                if not intervals[param].is_singleton():
                    index[param] = len(index) # just counting
                    var_param_count += 1
            except KeyError:
                pass

        # as of 10/2020 index above is just for the variable parameters...
        # So all sampled values are assigned to the first m columns and for constant params we need to continue the idx:
        for param in shape_param:
            try:
                if intervals[param].is_singleton():
                    index[param] = max(index.values()) + 1
            except KeyError:
                pass



        # idx_continued = index

        # reorder so that the constant values are first
        shape_param = sorted(shape_param, key= lambda parameter : index[parameter])

        # find all discrete parameters, save them in temporary set and sort later when setting the indices

        # discrete_param = set()  # could be done as sortedset, but I want alphanumerically sorted anyways
        # for parameter in shape_param:
        #     try:
        #         if intervals[parameter].is_discrete:
        #             discrete_param.add(parameter)
        #     except KeyError:
        #         pass

        parameter_combinations = np.ndarray((n, len(params)))

        # the samples gained via hit and run (all variables that are nonconstant!)
        # sampled_combinations = sampler(n, A, b, seed=seed)

        # NEW CODE WITH DEJANS HIT AND RUN

        variables = list([p for p in shape_param if not intervals[p].is_singleton()])

        constraints = Constraints(variables)

        for rel in relations:
            print(rel)
            constraints.add_constraint(str(rel))
            # constraints.add_constraint('a*l <= 0.6')

        try:
            bounds = list(((intervals[param].start,intervals[param].end) for param in variables))
        except KeyError:
            raise Exception("Right now the parameters need to have bounds.")


        # copied from main_hit_and_run_2D_ball and modified a bit
        hr = HitAndRun(S=constraints, B=bounds)

        sampled_combinations = np.ndarray([n,var_param_count])

        # a_s = []
        # r_s = [[0, 0]]
        total_rejections = 0
        for i in range(n):
            sample, rejections = hr.next_sample()
            total_rejections = total_rejections + rejections
            # a_s.append(sample)
            sampled_combinations[i, :] = sample


        print('Total number of rejections: ' + str(total_rejections))


        np.random.seed(seed=seed)

        # now i fix the discrete parameters by rounding to closest
        for param in shape_param:
            # 1st fill up parameter combinations by 1) sampled combinations and 2) correct constants
            idx = index[param]
            if idx in range(sampled_combinations.shape[1]):
                parameter_combinations[:, idx] = sampled_combinations[:,idx]
            else:
                parameter_combinations[:, idx] = intervals[param].start * np.ones((n))



            try:
                if intervals[param].is_discrete:
                    start = intervals[param].start
                    end = intervals[param].end

                    if start == end:
                        discrete_durations = np.asarray(start).reshape(1)
                    else:
                        discrete_durations = np.arange(start=start, stop=end, step=timestep)

                    samples = parameter_combinations[:, index[param]]

                    # find closest allowed value for each sample
                    for i, value in enumerate(samples):
                        closest_idx = bisect(discrete_durations, samples[i], hi=len(discrete_durations) - 1)
                        # inspired by https://stackoverflow.com/a/33455153
                        d1, d2 = discrete_durations[closest_idx], discrete_durations[closest_idx - 1]
                        samples[i] = d1 if abs(samples[i] - d1) < abs(samples[i] - d2) else d2

                    parameter_combinations[:,index[param]] = samples  # not sure if numpy does a shallow copy by default



            except KeyError:
                pass

        out = parameter_combinations, index

        # import matplotlib.pyplot as plt
        # import sympy
        # # a,l = sympy.symbols('a l')
        # # sympy.plot_parametric(a*l-5)
        # # eqn = sympy.Eq(a*l,0.7)
        # #
        # # sympy.plot_implicit(eqn)
        # # ts = np.linspace(0.7,1,1000)
        # plt.figure(figsize=(10,10))
        # ts = np.linspace(0,0.7,1000)
        # x = np.linspace(0,1,1000)
        # # plt.plot(ts, 0.7/ts)
        # # plt.plot(ts,0.7-ts)
        # # plt.Rectangle((0,0),1,1,ec ='g', lw = 10)
        # zero = np.zeros(x.shape)
        # one = np.ones(x.shape)
        # plt.plot(x,zero, zero,x,x, one, one, x, color='k')
        #
        # plt.scatter(parameter_combinations[:,index['a']], parameter_combinations[:,index['l']])
        # plt.show()


        pass

    # TODO should be refactored, a lot of code should be able to be reusable between these modes
    # SAMPLING MODE
    elif uniform_sampling:
        assert n, "In uniform sampling mode, instantiate function needs non-negative integer number of " \
                  "samples "
        # TODO can these parameters be made more intuitive? Should I create a separate function instead?

        counter = 0
        index = {}

        np.random.seed(seed=seed)

        # np_type_string = '|'
        # for param in params:
        #     if param_interval_map[param].is_discrete:
        #         np_type_string += 'i4,'
        #     else:
        #         np_type_string += 'f4,'
        # np_type_string = np_type_string[0:-1]

        parameter_combinations = np.ndarray((n, len(params)))

        enumerator = 0
        index = {}

        for param in params:
            index[param] = enumerator
            enumerator += 1
            # I want to be able to call a value by its name out of a single combination
            # for a single instance i can now just call instance[index[param]]

            start = param_interval_map[param].start
            end = param_interval_map[param].end

            if param_interval_map[param].is_discrete:
                if not non_integer_durations:
                    random_vector = np.random.randint(start, end + 1, n)
                else:
                    # this is the addition for non_integer durations with timestep. Here, float values for
                    # durations are allowed
                    # random_vector = np.random.uniform(start, end, n)
                    discrete_durations = np.arange(start=start, stop=end, step=timestep)
                    if discrete_durations.size == 0:
                        discrete_durations = np.asarray(start).reshape((1,))
                        # the condition means start == end and will result in empty array, which obviously cant be sampled

                    # if not np.isclose(end, discrete_durations[-1]):
                    #     print('WARNING: Interval of ' + param + ' can not be fully reached with this timestep. To '
                    #                                             'get rid of this message, (end - start) should be'
                    #                                             ' divisible by timestep.')
                    random_vector = np.random.choice(discrete_durations, n)

            else:
                param_type = float
                random_vector = start + (end - start) * np.random.rand(n)

            parameter_combinations[:, enumerator - 1] = random_vector

        out = parameter_combinations, index
        # plt.scatter(parameter_combinations[:,0],parameter_combinations[:,1])
        # plt.show()

        # return out

    # ITERATION MODE
    else:
        gridline_vectors = []
        enumerator = 0
        index = {}
        for param in params:
            index[param] = enumerator
            enumerator += 1
            # I want to be able to call a value by its name out of a single combination
            # for a single instance i can now just call instance[index[param]]

            start = param_interval_map[param].start
            end = param_interval_map[param].end

            # if param_interval_map[param].is_discrete: # old one before discrete interval changes
            if param_interval_map[param].is_discrete and not non_integer_durations:
                param_type = int
            else:
                param_type = float

            if (start == end):
                # if start == end we can only consider one value for 'param' (even if 'density'>1):
                gridline_vectors.append([param_type(start)])
            elif (density == 1):
                # if 'param' is variable and 'density' == 1, i.e. we only want to consider one value from the possible values for
                # 'param', then we take the middle of the possible values range:
                gridline_vectors.append([param_type((start + end) / 2.)])
            else:
                # depending on the values of start, end and density, linspace may return an array containing duplicates; thus we
                # transform the array into a set (to remove the duplicates) and then back into a sorted list (sorted just for the sake
                # of elegancy, otherwise not needed):
                gridline_vectors.append(sorted(list(set(np.linspace(start, end, density, dtype=param_type)))))
            # print("{} in [{},{}], map={}".format(param, start, end, gridline_vectors[-1]))

        parameter_combinations = itertools.product(*gridline_vectors)
        # this is now an itertools object with all possible combinations of the param grid

        # list important, itertools gets consumed when iterated
        out = list(parameter_combinations), index


    # old simple filtering
    if handle_nonlin_constr:

        # detect nonlinear constraints:
        for relation in aut.relations:
            if isinstance(relation, (str, StrictLessThan, StrictGreaterThan, LessThan, GreaterThan)):
                print(relation)


        # testing rejection function: TODO this is just temporary (or at least incomplete)
        samples, index = out
        # epsilons = [0.5, 1, 2, 3,5, 10]
        # pd.DataFrame()

        epsilon = 0.5

        # create logical table
        non_sat = np.zeros(len(samples))

        for i, sample in enumerate(tqdm(samples,desc='Rejecting samples not satisfying the nonlinear constraints.')):
            is_rejected = reject(sample, epsilon, index, aut)
            non_sat[i] = is_rejected

        ratio = (n - non_sat.sum()) / n

        print("{} % of samples satisfy continuity __constraint.".format(ratio * 100))
        return samples[~non_sat.astype(bool)], index

        return out
    else: return out


def reject(sample: np.ndarray, epsilon: float, sample_index, aut:ShapeAutomatonContainer):
    value_tuples = [(par, sample[sample_index[par]]) for par in sample_index.keys()]
    # this makes it easier to have each parameter as an actual variable in namespace (TODO unsafe, probably)

    # TODO find some way to sanitize inputs. Eval might just be unsafe, though
    illegal_names = locals().keys()
    # need to exclude these for parameter names!
    assert set(illegal_names).isdisjoint(set(sample_index.keys())), \
        "Encountered an illegal parameter identifier: " + str(set(illegal_names).intersection(set(sample_index.keys())))

    # get pairs directly into namespace:
    locals().update(value_tuples)
    non_sat = False
    for relation in aut.relations:
        if isinstance(relation,str):
            if not eval(relation):  # evaluate whether the __constraint is satisfied
                non_sat = True  # change value if this is the case. rest of relations need not be considered
                break

        # TODO There probably is some unnecessary code around because I first handled the nonlinear constraints as strings, then as sympy objects! this should be cleaned up!
        if isinstance(relation,(str, StrictLessThan, StrictGreaterThan, LessThan, GreaterThan)): # TODO NOT TESTED!
            if not relation.subs(dict(value_tuples)):  # evaluate whether the __constraint is satisfied
                non_sat = True  # change value if this is the case. rest of relations need not be considered
                break

    return non_sat


# first try
# def reject(sample: np.ndarray, epsilon: float, sample_index):
#     a1 = sample[sample_index['a1']]
#     a2 = sample[sample_index['a2']]
#     b = sample[sample_index['b']]
#     d = sample[sample_index['d']]
#
#     return (abs(a1 * d - b) > epsilon)
