from anyHR.hit_and_run.hit_and_run import DirectionSampling, Shrinking, InitPoint

from shapex.expression.Expression import WordSamplerMode
from shapex.misc.visualize import plotter
from shapex.shapex.ShapEx import ShapEx
import itertools


import unittest

# these test the whole shapex class, meaning they are not actual unit tests with regard to the subroutines in anyHR,
#  the sample generators etc.

# The way we test is to create 10 samples without noise for all supported modes. The specifications are saved in the
# according .sx file. The test assertion depends on the specification and is some rudimentary measure of how the
# generated signals should look. TODO see whether we can improve the test assertions
# I also added some corner cases like n = 0, etc

settings_list = []
# params:
# timestep=1.0, word_sampler=WordSamplerMode.SEARCH, search_budget=100, target_word_length=0,
#               dir_sampling=DirectionSampling.RDHR, shrinking=Shrinking.NO_SHRINKING, init_point=InitPoint.PSO,
#               noise_dist='uniform', noise=0)
word_samplers = (WordSamplerMode.SEARCH, WordSamplerMode.BOLTZMANN)
search_budget = (0,1,10)
word_lengths = (0,1,10)
dir_sampling_modes = (DirectionSampling.RDHR, DirectionSampling.CDHR)
shrinking_modes = (Shrinking.NO_SHRINKING, Shrinking.SHRINKING)
init_point_modes=(InitPoint.PSO, InitPoint.SMT)
noise_dists=('uniform','gaussian')
noise_vals = (0,)

# these are in the right order, do the cartesian product to get all combinations of modes
cart_prod = (word_samplers, search_budget, word_lengths, dir_sampling_modes, shrinking_modes, init_point_modes, noise_dists, noise_vals)

# these are all the parameter inputs that are bing tested (this is a lot!)
modes = list(itertools.product(*cart_prod))





class TestShapEx(unittest.TestCase):

    # 001
    def test_const(self):
        """
        single constant atomic
        """
        filename = r"/shapex/tests/specifications/det.sx"



    def test_line(self):
        """
        single exponential atomic
        """
    def test_sine(self):
        """
        single exponential atomic
        """
    def test_sinc(self):
        """
        single exponential atomic
        """
    def test_exp(self):
        """
        single exponential atomic
        """




filename = r"/shapex/tests/specifications/det.sx"

shapex = ShapEx(noise=0, word_sampler=WordSamplerMode.BOLTZMANN, target_word_length=20)

shapex.add_shape_expression(filename)

plotter(shapex.samples(10))