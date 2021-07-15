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

import os

import numpy as np
import functools



mode = (0.5,WordSamplerMode.SEARCH,-1,0,DirectionSampling.RDHR,Shrinking.NO_SHRINKING,InitPoint.SMT,'uniform',0, None)


spec_dir = os.getcwd()
input_file = os.path.join(spec_dir,"bug_001.sx")
# line(a,b,l).const(b,l).sine(a,b,c,d,l).sinc(a,b,c,d,l).exp(a,b,c,l)

shapex = ShapEx(*mode)
shapex.add_shape_expression(input_file)

samples = shapex.samples(100)

plotter(samples)


