import numpy as np

from shapex.misc.Error import InputError


def create_x_values(duration: int, timestep: float = 1.0):
    """
    Returns a numpy.array of evenly spaced numbers starting from 0. until 'duration' with the indicated 'timestep'.
    'duration' is included in the returned array only if [0,duration] can be divided into an exact number of intervals of length 'timestep'.
    UPDATE 03.10.2019: The tool has been adapted to handle the length of an
      atomic shape (given as a dparam in the file specification) as the number
      of samples and not as a duration in seconds. As a consequence the parameter
      'duration' passed to this method is now the number of samples; the duration
      can be obtained by simply multiplying the number of samples by the time step,
      but we don't actually need the duration here, we only need the number of samples.
      To be checked whether this change in handling the old parameter 'duration' has
      any impact in other parts of Felix' code.
    """
    # n_samples = int(duration//timestep)                     # 03.10.2019: commented out
    # return np.linspace(0, n_samples*timestep, n_samples+1)  # 03.10.2019: commented out
    # Update 03.10.2019:
    # Update 14.05.2020- if clause for automatic handling of non-integer durations
    if isinstance(duration, int):
        return np.linspace(0, (duration - 1) * timestep, int(duration))
    else:  # in case a float value is given
        x = np.arange(start=0, stop=duration + timestep, step=timestep)
        return x


def line_gen(fixed_function_parameters: list, timestep: float = 1.):
    """
    input: fixed_function_parameters ~ [duration,x_0,y_0, slope]
        plus parameters for noise
    output: [x values, trace values, mse from exact line]
        where trace values are a noisified line (NOT THE FIRST VALUE!)
        with f(x) = slope * x
        with some correction constant so it starts at (x_0,y_0)
    """

    # EDIT: give optional relative offset parameter at the end of fixed function parameters, so [duration,x_0,y_0, slope, rel_offset]

    has_relative_offset = len(fixed_function_parameters) == 5

    if len(fixed_function_parameters) != 4 and not has_relative_offset:
        raise InputError('illegal input', 'invalid parameter vector length')

    duration = fixed_function_parameters[0]
    start_val = [float(fixed_function_parameters[1]), float(fixed_function_parameters[2])]
    slope = float(fixed_function_parameters[3])

    if has_relative_offset:
        relative_offset = fixed_function_parameters[4]
    else:
        relative_offset = 0

    # x_values
    # x = np.array(range(duration + 1))
    x = create_x_values(duration, timestep)
    transferred_x = x + start_val[0]  # translation

    # perfect line
    line = slope * x + start_val[1] + relative_offset

    # if has_relative_offset:
    #     line = slope * x + relative_offset # with relative offset I do not fix the starting point to the end of last atomic
    # else:
    #     line = slope * x + start_val[1]
    # TODO maybe I should make "has_relative_offset" a parameter instead for more control ?

    exact_function = [transferred_x, line, .0]

    exact_end_point = (transferred_x[-1], exact_function[1][-1])  # for concatenation!

    exact_function.append(exact_end_point)  # output is now [xval:list, yval:list, mse:float, ex_end_point:tuple)

    # return trace
    return exact_function


def const_gen(fixed_function_parameters: list, timestep: float = 1.):
    # fixed_function parameters is here: [duration, x_0, y_0] (constant is fully defined by point)

    # EDIT: give optional relative offset parameter at the end of fixed function parameters, so [duration,x_0,y_0, rel_offset]

    has_relative_offset = len(fixed_function_parameters) == 4

    if len(fixed_function_parameters) != 3 and not has_relative_offset:
        raise InputError('illegal input', 'invalid parameter vector length')

    slope = 0
    params = list(fixed_function_parameters)
    params.insert(3, slope)  # now it's the same as line_gen input

    return line_gen(params, timestep)


def sine_gen(fixed_function_parameters: list, timestep: float = 1.):
    """
    function form: f(x) = a*sin(bx + c) + correction
    input: fixed_function_parameters ~ [duration,x_0,y_0,a,b,c]

    output: see line_gen
    """

    # EDIT: give optional relative offset parameter at the end of fixed function parameters, so [duration,x_0,y_0,a,b,c, rel_offset]

    has_relative_offset = len(fixed_function_parameters) == 7

    if len(fixed_function_parameters) != 6 and not has_relative_offset:
        raise InputError('illegal input', 'invalid parameter vector length')

    a, b, c = fixed_function_parameters[3:6]

    if has_relative_offset:
        relative_offset = fixed_function_parameters[-1]
        intercept = a * np.sin(b * 0 + c)
        y_0 = relative_offset + fixed_function_parameters[2]
        correction = -(intercept - y_0)  # gets transferred later!
    else:
        intercept = a * np.sin(b * 0 + c)
        y_0 = fixed_function_parameters[2]
        correction = -(intercept - y_0)  # gets transferred later!

    # x_values
    # x = np.array(range(fixed_function_parameters[0] + 1))  # different: start with x=1
    duration = fixed_function_parameters[0]
    x = create_x_values(duration, timestep)
    transferred_x = x + fixed_function_parameters[1]

    # y_values
    exact_y_values = a * np.sin(b * x + c) + correction

    # function (exact)
    exact_function = [transferred_x, exact_y_values, 0]

    exact_end = (transferred_x[-1], exact_y_values[-1])
    # signal.append(exact_end)  # for concat
    exact_function.append(exact_end)  # for concat

    return exact_function


def sinc_gen(fixed_function_parameters: list, timestep: float = 1.):
    """
    this returns a sinc of the form (a * sin(b * x + c)) / (b * x + c)
    it transfers the values, so that the intersect  (first tuple) is in the designated starting point
    so (0, sinc(0)) -> (x_0, y_0)

    :param close_to_target:
    :param fixed_function_parameters:
    :param noise_dist_spec:
    :param dist_mode:
    :param threshold:
    :return:
    """

    # EDIT: give optional relative offset parameter at the end of fixed function parameters, so [duration,x_0,y_0,a,b,c, rel_offset]

    has_relative_offset = len(fixed_function_parameters) == 7

    if len(fixed_function_parameters) != 6 and not has_relative_offset:
        raise InputError('illegal input', 'invalid parameter vector length')

    a, b, c = fixed_function_parameters[3:6]

    # prevent zero division, this limit exists and is calculated in else

    if has_relative_offset:
        relative_offset = fixed_function_parameters[-1]
    else:
        relative_offset = 0

    # need to prevent division wit zero- this limit existsand is a without offset
    if c:
        d = relative_offset + fixed_function_parameters[2] - a * np.sin(c) / c
    else:
        d = a + relative_offset

    # x_values
    # x = np.array([i for i in range(fixed_function_parameters[0] + 1)])
    duration = fixed_function_parameters[0]
    x = create_x_values(duration, timestep)

    transferred_x = x + fixed_function_parameters[1]

    # actual values from function, beginning at the max/min location
    enum = (a * np.sin(b * x + c))
    denom = (b * x + c)

    exact_y_values = np.divide(enum, denom, out=(np.ones_like(enum) * a), where=denom != 0) + d

    # function_values (exact)
    exact_function = [transferred_x, exact_y_values, .0]  # last entry for mse later

    # signal = add_noise(exact_function, noise_dist_spec, dist_mode,
    #                    threshold=threshold, close_to_target=close_to_target)

    exact_end = (transferred_x[-1], exact_y_values[-1])  # for concat
    exact_function.append(exact_end)

    return exact_function


def exp_gen(fixed_function_parameters: list, timestep: float = 1.):
    # arbitrary exp fct: f(x)=a*exp(b*t) + c
    # fixed_function_parameters =[duration,x_0,y_0,b,c]

    # EDIT: give optional relative offset parameter at the end of fixed function parameters, so [duration,x_0,y_0,b,c, rel_offset]

    has_relative_offset = len(fixed_function_parameters) == 6

    if len(fixed_function_parameters) != 5 and not has_relative_offset:
        raise InputError('illegal input', 'invalid parameter vector length')

    duration = fixed_function_parameters[0]
    a, b = fixed_function_parameters[3:5]

    # y_0-b*exp(c*x_0) = a
    if has_relative_offset:
        relative_offset = fixed_function_parameters[-1]
        y_0 = fixed_function_parameters[2] + relative_offset
    else:
        y_0 = fixed_function_parameters[2]
    x_0 = fixed_function_parameters[1]

    intercept = a # a*exp(0) = a
    correction = -(intercept - y_0)

    # x = np.array(range(duration + 1))
    x = create_x_values(duration, timestep)
    transferred_x = x + x_0  # translation

    exact_y = a * (np.exp(b * x)) + correction
    exact_function = [transferred_x, exact_y, .0]  # last entry for mse later

    # signal = add_noise(exact_function, noise_dist_spec, dist_mode,
    #                    threshold=threshold, close_to_target=close_to_target)

    exact_end_point = (transferred_x[-1], exact_y[-1])
    exact_function.append(exact_end_point)
    return exact_function
