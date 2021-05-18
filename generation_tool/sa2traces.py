from collections import deque

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

from generation_tool.ideal_atomics import line_gen, const_gen, sine_gen, sinc_gen, exp_gen
from misc.visualize import plotter
from sapathfinder import find_paths
from se2sa.Error import *
from se2sa.automaton.alphabet.letter import Letter
from se2sa.automaton.alphabet.letter_type import LetterType
from se2sa.automaton.automaton_container import ShapeAutomatonContainer
from se2sa.automaton.interval import IntervalObject
from generation_tool.instantiate import instantiate


# this is just an interface to the inputstring for set_gen in shapes.py
def to_typestring(letter: Letter):
    letter_type = letter.get_type()
    if letter_type == LetterType.LINE:
        return 'line'
    elif letter_type == LetterType.CONST:
        return 'const'
    elif letter_type == LetterType.SINE:
        return 'sine'
    elif letter_type == LetterType.SINC:
        return 'sinc'
    elif letter_type == LetterType.EXP:
        return 'exponential'

    return 'letter type unknown'


def interval_to_pair(intervals):
    # return list of intervals in the form ((a_start,a_end),(b_start, b_end),..)
    if isinstance(intervals, IntervalObject):
        return tuple((intervals.start, intervals.end), )  # nested tuple so input fits
    elif isinstance(intervals, list):
        return tuple((interval.start, interval.end) for interval in intervals)
    else:
        raise InputError('Wrong input', 'This function expects an IntervalObject or an iterable of them')


def atomic_gen(param, shape, dist_mode='uniform',
               timestep=1., threshold=1., positive_example=True,
               close_to_target=True, epsilon=float('inf'), mse_target=None,
               start: tuple = (0, 0)):
    """
    converts param to format: [length, start_x, start_y, a, b,...], then inserts this into gen_functions,
    so it's just an interface between paths2traces and [shape]_gen
    """

    # TODO this is horrible... the relative offset should not be detected inside of line_gen, etc
    #  instead, they should simply be invoked in parameters...
    #  this requires a lot of refactoring though (all generators below, here, paths2traces)

    tmp = deque(param)
    param_input_format = [tmp.pop(), start[0], start[1]] + list(tmp)

    if shape == 'line':
        exact = line_gen(param_input_format, timestep)

    elif shape == 'const':
        exact = const_gen(param_input_format, timestep)

    elif shape == 'sine':
        exact = sine_gen(param_input_format, timestep)

    elif shape == 'sinc':
        exact = sinc_gen(param_input_format, timestep)

    elif shape == 'exponential':
        exact = exp_gen(param_input_format, timestep)

    else:
        print('no valid shape letter!')
        raise InputError('Illegal input:', 'not a letter')

    return add_noise(exact, threshold, dist_mode,
                     positive=positive_example,
                     close_to_target=close_to_target, epsilon=epsilon, target=mse_target)


def generate_noise(dist_type: str, dist_par: float, size: int):
    """
    Generate a vector of length 'size' of noise values according to a distribution of type 'dist_type' characterized
    by a parameter 'dist_par'.

    Parameters
    ----------
    dist_type: string
        Type of the distribution to use for generating the noise. Allowed values: "normal" and "uniform"
    dist_par: float
        Parameter of the distribution. For the random uniform distribution this is the boundary of the interval from
        which are drwan the noise values. For the normal distribution, it is the standard deviation of a normal
        distribution with the mean=0.
    size: int
        The number of noise values to be generated, i.e. the length of the returned noise vector.

    Returns
    -------
    out: array
        An array of length=size containing the generated noise values.
    """

    if dist_type == "normal":
        noise_vector = np.random.normal(0, dist_par, size)
    elif dist_type == "uniform":
        noise_vector = np.random.uniform(-dist_par, +dist_par, size)
    else:
        raise InputError('illegal input', 'invalid noise distribution dist')

    return noise_vector


def add_noise(curve, threshold,
              mode='uniform', positive=True,
              close_to_target=True, target=0, epsilon=np.inf):
    # curve: [xval:list, yval:list, mse:float, ex_end_point:tuple]; yval contains the noise-free shape
    # mode: the distribution type used to generate the noise; 'uniform' and 'normal' supported currently
    # target: the value that the _mse_ of the signal with the added noise should be approximately (+/-epsilon) equal to
    # last 3 params are used like this: if close_to_target=True and you
    # specify a noise target, epsilon as measure for how close we want to get
    #   --> it will try to make noise with mse epsilon-close to the target

    if threshold == 0.:
        return curve

    assert ((positive and (target <= threshold)) or (not positive and (target >= threshold)))

    if not close_to_target:
        # close_to_target forces the value to be epsilon close to target
        # if close_to_target is false, the while-loop below will only compute one iteration

        epsilon = np.inf

    counter = 0  # safety for infinite loops
    max_counter = 10000  # arbitrary, one could compute the prob for this to be enough
    epsilon_ = epsilon

    noise_vector = np.zeros(len(curve[1]))

    # compute the noise distribution parameter
    if mode == "normal":
        # dist_param is the std of a normal distribution with mean=0
        dist_param = np.sqrt(target)
    elif mode == "uniform":
        # dist_param gives the interval [-dist_param, +dist_param) of the uniform random distribution
        dist_param = np.sqrt(3 * target)
    else:
        raise InputError('illegal input', 'invalid noise distribution dist')

    # add noise and compute mse
    mse = np.inf if positive else -np.inf
    while (positive and mse > threshold) or (not positive and mse <= threshold) or (abs(mse - target) >= epsilon_):

        if counter > max_counter:
            counter = 0
            epsilon_ += epsilon
            print("> INFO: no noise with mse < abs(target-epsilon_) generated after {} iterations.\n".format(
                max_counter) +
                  "        Increasing epsilon_ (by epsilon): {}".format(epsilon_))

        noise_vector = generate_noise(mode, dist_param, len(curve[1]))

        mse = (np.square(noise_vector)).mean()

        counter += 1

    curve_with_noise: list = curve.copy()

    curve_with_noise[1] += noise_vector
    curve_with_noise[2] = mse

    return curve_with_noise


def targets(threshold, noise_density, positive):
    # the idea is to return intervals in which the noise values are allowed to be (still check pos/neg)
    # positive: targets are e.g. at 0%, 10%, 20%, ..., 100%
    # negative: targets are e.g. at 100%, 120%, ..., 300%

    if positive:
        # noise_targets = [threshold * (i/10) for i in range(11)]
        # epsilon = threshold / 10
        if threshold == 0:
            (noise_targets, epsilon) = (np.array([0.]), 0.)
        else:
            (noise_targets, epsilon) = np.linspace(0, threshold, noise_density, retstep=True)

    else:
        # noise_targets = [threshold * (1 + i/5) for i in range(11)]
        # epsilon = threshold / 5

        # NOTE: the returned epsilon below will be a negative number, since start > stop in np.linspace()
        (noise_targets, epsilon) = np.linspace(3 * threshold, threshold, noise_density, endpoint=False, retstep=True)
        noise_targets.sort()
        epsilon = abs(epsilon)

    # abs(epsilon) below because epsilon is negative for the negative examples (s. above)
    return noise_targets, epsilon


def paths2traces(input_paths: set, density: int, noise_density: int,
                 aut: ShapeAutomatonContainer, seed: int, dist_mode='uniform',
                 timestep: float = 1., threshold: float = 1., positive_example=True,
                 close_to_target=True, continuity_constraints:str=None, param_sampling=True,
                 n=None,
                 relational_input=False, non_integer_durations=False,
                 handle_nonlin_constr = False):
    params = aut.shape_param
    param_interval_map = aut.intervals

    param_combinations, index = instantiate(params, param_interval_map, density, seed=seed,
                                            uniform_sampling=param_sampling, n=n,
                                            relational_input=relational_input, aut=aut,
                                            non_integer_durations=non_integer_durations, timestep=timestep, handle_nonlin_constr=handle_nonlin_constr)

    # this function gives some specific ranges for the noise value that should be reached
    noise_targets, epsilon = targets(threshold, noise_density, positive_example)

    # tqdm is a little addon to see the process of trace generation in cmd:

    traces = []
    path_counter = 0
    path_len = len(input_paths)

    np.random.seed(seed=seed)  # for np random in atomic_gen

    for path in list(input_paths):
        path_counter += 1
        for target in noise_targets:
            # TODO this tqdm creates a new bar for each noise target, doesn't look nice
            for combination in tqdm(param_combinations, position=0,
                                    desc='Traces generated for path ' + str(path_counter) + '/' + str(path_len)):

                trace = []  # [x_val, y_val, mse, last_point]

                for letter in path:

                    letter_type = to_typestring(letter)

                    param_vars = letter.get_param_list(return_constant=True)

                    ## i think the following makes even less sense after refactoring, so I just always
                    ## use the whole param valuation
                    # if letter_type in ['line', 'const', 'sine', 'sinc', 'exponential'] and (
                    #         relative_offset_on or continuity_filter):
                    #     param_vars = letter.get_param_list(return_constant=True)
                    # else:
                    #     param_vars = letter.get_param_list(return_constant=False)  # this is ordered!

                    param_values = [combination[index[var]] for var in param_vars]
                    # now param_values are in the right order for input in atomic_gen

                    hardcoded = continuity_constraints == 'hardcoded'
                    continuity_filter = continuity_constraints == 'filter'
                    # standard mode is with relative offsets now

                    if hardcoded:
                        assert letter_type in ['line', 'const', 'sine', 'sinc', 'exponential'], \
                            "relative offsets have not been implemented for letter" + letter_type

                        if not trace:
                            start = (0, param_values[-2])

                            trace = atomic_gen(param_values, letter_type, dist_mode=dist_mode,
                                               timestep=timestep, threshold=threshold,
                                               positive_example=positive_example,
                                               close_to_target=close_to_target, mse_target=target, epsilon=epsilon,
                                               start=start
                                               )

                            settings_labels = [(parameter, combination[index[parameter]])
                                               for parameter in params]
                            # these are global, need only look at first segment

                            trace.insert(3, settings_labels)
                        else:
                            start = trace[-1]

                            # this is necessary because now all the param values include the offset inputs at the
                            # end, but in this mode we need it only for first segment. param values looks like this:
                            # [slope, offset, duration]
                            if letter_type == 'const':
                                nr_params = 0  # just nondiscrete!
                            elif letter_type == 'line':
                                nr_params = 1
                            elif letter_type == 'exponential':
                                nr_params = 2
                            elif letter_type in ['sine', 'sinc']:
                                nr_params = 3
                            else:
                                assert False, "This should be impossible!"

                            new_segment = atomic_gen((param_values[0:nr_params] + [(param_values[-1]), ]),
                                                     letter_type,
                                                     dist_mode=dist_mode,
                                                     timestep=timestep, threshold=threshold,
                                                     positive_example=positive_example,
                                                     close_to_target=close_to_target, mse_target=target,
                                                     epsilon=epsilon,
                                                     start=start)

                            trace[0] = np.concatenate((trace[0], new_segment[0]))
                            trace[1] = np.concatenate((trace[1], new_segment[1]))
                            trace[2] = max(trace[2], new_segment[2])  # mse of concat is max of both

                            trace[-1] = new_segment[-1]




                    elif continuity_filter:
                        assert letter_type in ['line', 'const', 'sine', 'sinc', 'exponential'], \
                            "relative offsets have not been implemented for letter" + letter_type

                        if not trace:
                            start = (0, 0)

                            trace = atomic_gen(param_values, letter_type, dist_mode=dist_mode,
                                               timestep=timestep, threshold=threshold,
                                               positive_example=positive_example,
                                               close_to_target=close_to_target, mse_target=target, epsilon=epsilon,
                                               start=start
                                               )

                            settings_labels = [(parameter, combination[index[parameter]])
                                               for parameter in params]
                            # these are global, need only look at first segment

                            trace.insert(3, settings_labels)
                        else:
                            start = (trace[-1][0], 0)


                            new_segment = atomic_gen(param_values,
                                                     letter_type,
                                                     dist_mode=dist_mode,
                                                     timestep=timestep, threshold=threshold,
                                                     positive_example=positive_example,
                                                     close_to_target=close_to_target, mse_target=target,
                                                     epsilon=epsilon, start=start)

                            tolerance = 1.05

                            if abs(trace[-1][1] - new_segment[1][0]) >= tolerance:
                                trace = 'discarded'
                                break
                                # pass

                            trace[0] = np.concatenate((trace[0], new_segment[0]))
                            trace[1] = np.concatenate((trace[1], new_segment[1]))
                            trace[2] = max(trace[2], new_segment[2])  # mse of concat is max of both

                            trace[-1] = new_segment[-1]


                    else:  # no constraints!
                        if not trace:
                            start = (0, 0) # this looks wrong but isn't... relative offset gets added in atomic gen

                            trace = atomic_gen(param_values, letter_type, dist_mode=dist_mode,
                                               timestep=timestep, threshold=threshold,
                                               positive_example=positive_example,
                                               close_to_target=close_to_target, mse_target=target, epsilon=epsilon,
                                               start=start
                                               )

                            settings_labels = [(parameter, combination[index[parameter]])
                                               for parameter in params]
                            # these are global, need only look at first segment

                            trace.insert(3, settings_labels)
                        else:
                            start = (trace[-1][0], 0) # again, relative offset is added in atomic_gen
                            new_segment = atomic_gen(param_values, letter_type,
                                                     dist_mode=dist_mode,
                                                     timestep=timestep, threshold=threshold,
                                                     positive_example=positive_example,
                                                     close_to_target=close_to_target, mse_target=target,
                                                     epsilon=epsilon,
                                                     start=start)

                            trace[0] = np.concatenate((trace[0], new_segment[0]))
                            trace[1] = np.concatenate((trace[1], new_segment[1]))
                            trace[2] = max(trace[2], new_segment[2])  # mse of concat is max of both

                            trace[-1] = new_segment[-1]

                # continuity constraint not satisfied?
                if trace == 'discarded':
                    continue

                # for saving mse and target mse in settings file:
                settings_tag_mse_target = ('target value mse', target)
                settings_tag_mse = ('actual mse', trace[2])

                trace[3].append(settings_tag_mse_target)
                trace[3].append(settings_tag_mse)
                trace[3].append(('epsilon', epsilon))

                traces.append(trace)

    return traces


if __name__ == '__main__':
    pass

    # testbatch = set_gen(10, ((1,10),), (4,))
    #
    # layer_2 = set_gen(10, ((1,10),), (4,), continued_traces=testbatch)

    # plotter(layer_2)
