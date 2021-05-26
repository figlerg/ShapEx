from collections import deque

import numpy as np

from generation_tool.ideal_atomics import line_gen, const_gen, sine_gen, sinc_gen, exp_gen
from alphabet.letter import Letter
from alphabet.letter import LetterType
from parse.Error import InputError, InfLoopError
from parse.se2sa.interval import IntervalObject


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


def atomic_gen(param, shape, dist_mode='uniform', timestep=1., start: tuple = (0, 0)):
    """
    converts param to format: [length, start_x, start_y, a, b,...], then inserts this into gen_functions,
    so it's just an interface between paths2traces and [shape]_gen
    """

    # TODO should be refactored

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

    return add_noise(exact, dist_mode)


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
        which the values are drawn. For the normal distribution, it is the standard deviation of a normal
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
        raise InputError('illegal input', 'invalid noise distribution noise_dist')

    return noise_vector


def add_noise(curve, mode='uniform', dist_param = 0):
    # curve: [xval:list, yval:list, mse:float, ex_end_point:tuple]; yval contains the noise-free shape
    # mode: the distribution type used to generate the noise; 'uniform' and 'normal' supported currently

    if dist_param == 0:
        return curve

    # add noise and compute mse
    noise_vector = generate_noise(mode, dist_param, len(curve[1]))

    mse = (np.square(noise_vector)).mean()

    curve_with_noise: list = curve.copy()

    curve_with_noise[1] += noise_vector
    curve_with_noise[2] = mse

    return curve_with_noise
