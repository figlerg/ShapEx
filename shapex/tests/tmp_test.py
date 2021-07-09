import math

from shapex.alphabet.const_letter import ConstLetter
from shapex.alphabet.exp_letter import ExpLetter
from shapex.alphabet.line_letter import LineLetter
from shapex.alphabet.sinc_letter import SincLetter
from shapex.alphabet.sine_letter import SineLetter
from shapex.misc.Error import IllegalParameterError
from shapex.misc.visualize import plotter
from shapex.shapex.ShapEx import ShapEx
from anyHR.hit_and_run.hit_and_run import DirectionSampling, Shrinking, InitPoint
from shapex.expression.Expression import WordSamplerMode

import numpy as np
import functools

np.random.seed(0)


mode = (0.5,WordSamplerMode.SEARCH,5,3,DirectionSampling.RDHR,Shrinking.NO_SHRINKING,InitPoint.SMT,'uniform',0, None)

input_file = r"C:\Users\giglerf\Documents\dev\dev_code\ShapEx\shapex\tests\007.sx"
# line(a,b,l).const(b,l).sine(a,b,c,d,l).sinc(a,b,c,d,l).exp(a,b,c,l)
a,b,c,d,l,l2 = 'a', 'b', 'c', 'd', 'l', 'l2'
phi_0 = (LineLetter(a,b,l2), ConstLetter(b,l), SineLetter(a,b,c,d,l),SincLetter(a,b,c,d,l), ExpLetter(a,b,c,l2)) # this is repeated because of kleene

try:
    shapex = ShapEx(*mode)
    shapex.add_shape_expression(input_file)


    for i in range(100):
        word = shapex._expression.sample()




        for j in range(len(word)):
            assert word[j] == phi_0[j%5]



except IllegalParameterError:
    # these are handled already and can be assumed to be user errors
    pass

samples = shapex.samples(10)

plotter(samples)


