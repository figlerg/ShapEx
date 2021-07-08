import math

from shapex.misc.Error import IllegalParameterError
from shapex.misc.visualize import plotter
from shapex.shapex.ShapEx import ShapEx
from anyHR.hit_and_run.hit_and_run import DirectionSampling, Shrinking, InitPoint
from shapex.expression.Expression import WordSamplerMode

import numpy as np
import functools

np.random.seed(0)

input_file = r"C:\Users\giglerf\Documents\dev\dev_code\ShapEx\shapex\tests\005.sx"

mode = (1,WordSamplerMode.SEARCH,5,5,DirectionSampling.RDHR,Shrinking.NO_SHRINKING,InitPoint.PSO,'uniform',0)

try:
    shapex = ShapEx(*mode)
    shapex.add_shape_expression(input_file)

    samples = shapex.samples(1000)

    for sample in samples:
        param_vals = dict(sample[3]) # dict of sampled parameters
        a = param_vals['a']
        b = param_vals['b']
        c = param_vals['c']
        l = param_vals['l']

        start = c
        end = a*np.exp(b*math.ceil(l))-a+c

        assert abs(sample[1][0]-start) <= 0.01, 'Unexpected start point for exp'
        assert abs(sample[1][-1]-end) <= 0.001, 'Unexpected end point for exp. Diff = {}'.format(abs(sample[1][-1]-end))

    #
    # shapex2 = ShapEx(*mode)
    # shapex2.add_shape_expression(input_file)
    #
    # samples2 = shapex2.samples(100)
    #
    # # print(np.hstack(samples == samples2).all())
    # for i in range(len(samples)):
    #     for j in range(len(samples[i])):
    #         assert np.all(samples[i][j]==samples2[i][j])


    # print(samples)

except IllegalParameterError:
    # these are handled already and can be assumed to be user errors
    pass

plotter(samples)