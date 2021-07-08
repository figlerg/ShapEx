import math
from math import exp

import numpy as np
from anyHR.hit_and_run.hit_and_run import DirectionSampling, Shrinking, InitPoint

from shapex.alphabet.exp_letter import ExpLetter
from shapex.alphabet.line_letter import LineLetter
from shapex.alphabet.const_letter import ConstLetter
from shapex.alphabet.sine_letter import SineLetter
from shapex.alphabet.sinc_letter import SincLetter
from shapex.expression.Expression import WordSamplerMode
from shapex.misc.visualize import plotter
from shapex.shapex.ShapEx import ShapEx
import itertools

from shapex.misc.Error import *

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
# timesteps = (-1, 0, 1,) # -1 handled
timesteps = (0.5, 1,)
word_samplers = (WordSamplerMode.SEARCH, WordSamplerMode.BOLTZMANN)
# search_budget = (0, 1, 10) # 0 is handled
# word_lengths = (0, 1, 10) # 0 is handled
search_budget = (-1,0,5,)
word_lengths = (2,3,10,)
dir_sampling_modes = (DirectionSampling.RDHR, DirectionSampling.CDHR)
shrinking_modes = (Shrinking.NO_SHRINKING, Shrinking.SHRINKING)
init_point_modes = (InitPoint.PSO, InitPoint.SMT)
# noise_dists = ('uniform', 'normal') # normal is difficult to test
noise_dists = ('uniform',)
# noise_vals = (0,) if gaussian is tested, use this line
noise_vals = (0,0.01)
seeds = (None,)

# these are in the right order, do the cartesian product to get all combinations of modes
cart_prod = (
timesteps, word_samplers, search_budget, word_lengths, dir_sampling_modes, shrinking_modes, init_point_modes,
noise_dists, noise_vals, seeds)

# these are all the parameter inputs that are bing tested (this is a lot!)
modes = list(itertools.product(*cart_prod))

# print(modes)

# def run_test_all_modes(input_file):
#     for mode in modes:
#         print(mode)
#         shapex = ShapEx(*mode)
#         shapex.add_shape_expression(input_file)
#
#         samples = shapex.samples(10)


class TestShapEx(unittest.TestCase):

    # 001
    def test_line(self):
        """
        single line atomic with constraint
        """
        input_file = r"C:\Users\giglerf\Documents\dev\dev_code\ShapEx\shapex\tests\001.sx"
        for mode in modes:
            with self.subTest(i=mode):

                # print(mode)
                try:
                    shapex = ShapEx(*mode)
                    shapex.add_shape_expression(input_file)

                    samples = shapex.samples(10)

                    # assertions

                    self.assertTrue(len(samples)==10)

                    # this checks if the samples are equal for same seed, and unequal for no given seed (system time)
                    reproducibility_test(self,mode,samples,input_file)

                    # test some specification characteristics
                    for sample in samples:
                        self.assertTrue(-0.01 <= sample[1][0] <= 1.01, msg= "Line- 1st point impossible: mode {}, sample{}".format(mode, sample)) # first val
                        if len(sample[0]) == 2:
                            self.assertTrue(-0.01 <= sample[1][1] <= 2.01, msg= "Line- last point impossible: mode {}, sample{}".format(mode, sample)) # last val

                        if len(sample[0]) == 3:
                            self.assertTrue(-0.01 <= sample[1][2] <= 3.01, msg= "Line- last point impossible: mode {}, sample{}".format(mode, sample)) # last val


                except IllegalParameterError:
                    # these are handled already and can be assumed to be user errors
                    pass


    # 002
    def test_const(self):
        """
        single const atomic
        """
        input_file = r"C:\Users\giglerf\Documents\dev\dev_code\ShapEx\shapex\tests\002.sx"
        for mode in modes:
            with self.subTest(i=mode):

                # print(mode)
                try:
                    shapex = ShapEx(*mode)
                    shapex.add_shape_expression(input_file)

                    samples = shapex.samples(10)

                    # plotter(samples)

                    # assertions

                    self.assertTrue(len(samples)==10)

                    # this checks if the samples are equal for same seed, and unequal for no given seed (system time)
                    reproducibility_test(self,mode,samples,input_file)

                    for sample in samples:
                        self.assertTrue(-0.01 <= sample[1][0] <= 1.01, msg= "Const- 1st point impossible: mode {}, sample{}".format(mode, sample)) # first val

                        # check whether the constant appears to have slope zero
                        self.assertTrue(abs(sample[1][0]-sample[1][-1]) <= 0.02, msg= "Const- Not constant? mode {}, sample{}".format(mode, sample)) # first val


                except IllegalParameterError:
                    # these are handled already and can be assumed to be user errors
                    pass

    # 003
    def test_sine(self):
        """
        single sine atomic
        """
        input_file = r"C:\Users\giglerf\Documents\dev\dev_code\ShapEx\shapex\tests\003.sx"
        for mode in modes:
            with self.subTest(i=mode):

                # print(mode)
                try:
                    shapex = ShapEx(*mode)
                    shapex.add_shape_expression(input_file)

                    samples = shapex.samples(10)

                    # plotter(samples)

                    # assertions

                    self.assertTrue(len(samples)==10)

                    # this checks if the samples are equal for same seed, and unequal for no given seed (system time)
                    reproducibility_test(self,mode,samples,input_file)


                    for sample in samples:
                        param_vals = dict(sample[3]) # dict of sampled parameters

                        # the trace has to be within [-a,a] (with some tolerance) because it is a*sin(bx)
                        self.assertTrue(max(np.abs(sample[1])) <= param_vals['a']+0.01, msg= "Amplitude is exceeded: mode {}, sample{}".format(mode, sample)) # first val


                except IllegalParameterError:
                    # these are handled already and can be assumed to be user errors
                    pass

    #004
    def test_sinc(self):
        """
        single sinc atomic
        """
        input_file = r"C:\Users\giglerf\Documents\dev\dev_code\ShapEx\shapex\tests\004.sx"
        for mode in modes:
            with self.subTest(i=mode):

                # print(mode)
                try:
                    shapex = ShapEx(*mode)
                    shapex.add_shape_expression(input_file)

                    samples = shapex.samples(10)

                    # plotter(samples)

                    # assertions

                    self.assertTrue(len(samples)==10)

                    # this checks if the samples are equal for same seed, and unequal for no given seed (system time)
                    reproducibility_test(self,mode,samples,input_file)


                    for sample in samples:
                        param_vals = dict(sample[3]) # dict of sampled parameters

                        # the trace has to be within [-a,a] (with some tolerance) because it is a*sin(bx)
                        # self.assertTrue(max(np.abs(sample[1])) <= param_vals['a']+0.01, msg= "Amplitude is exceeded: mode {}, sample{}".format(mode, sample)) # first val
                        # TODO think of a fitting assertion

                except IllegalParameterError:
                    # these are handled already and can be assumed to be user errors
                    pass

    #005
    def test_exp(self):
        """
        single exponential atomic
        """
        input_file = r"C:\Users\giglerf\Documents\dev\dev_code\ShapEx\shapex\tests\005.sx"
        for mode in modes:
            with self.subTest(i=mode):

                # print(mode)
                try:
                    shapex = ShapEx(*mode)
                    shapex.add_shape_expression(input_file)

                    samples = shapex.samples(10)

                    # plotter(samples)

                    # assertions

                    self.assertTrue(len(samples)==10)

                    # this checks if the samples are equal for same seed, and unequal for no given seed (system time)
                    reproducibility_test(self,mode,samples,input_file)

                    # check if min/max is exceeded for given params:
                    spec_max = 10 + exp(1*10)
                    spec_min = 0 - 0.01

                    self.assertLessEqual(max(list([sample[1].max() for sample in samples])), spec_max)
                    self.assertGreaterEqual(min(list([sample[1].min() for sample in samples])), spec_min)

                    # check if the trace fits the params
                    for sample in samples:
                        param_vals = dict(sample[3]) # dict of sampled parameters
                        a = param_vals['a']
                        b = param_vals['b']
                        c = param_vals['c']
                        l = param_vals['l']

                        start = c
                        if mode[0]:
                            # the ceil bit is necessary due to the mechanics of duration parameters:
                            # these are sampled as normal params and then get rounded up to next multiple of timestep
                            end = a*np.exp(b*mode[0]*math.ceil(l/mode[0])) - a+c

                        self.assertAlmostEqual(sample[1][0],start,delta= 0.01,msg= 'Unexpected start point for exp')
                        self.assertAlmostEqual(sample[1][-1],end,delta= 0.01,msg= 'Unexpected end point for exp. Diff = {}'.format(abs(sample[1][-1]-end)))




                except IllegalParameterError:
                    # these are handled already and can be assumed to be user errors
                    pass


    def test_det_word_sampler(self):
        '''
        Tests whether the word samplers return the single possible word for a deterministic automaton
        '''

        input_file = r"C:\Users\giglerf\Documents\dev\dev_code\ShapEx\shapex\tests\006.sx"
        # line(a,b,l).const(b,l).sine(a,b,c,d,l).sinc(a,b,c,d,l).exp(a,b,c,l)
        a,b,c,d,l = 'a', 'b', 'c', 'd', 'l'
        only_word = (LineLetter(a,b,l), ConstLetter(b,l), SineLetter(a,b,c,d,l),SincLetter(a,b,c,d,l), ExpLetter(a,b,c,l))



        for mode in modes:
            with self.subTest(i=mode):
                try:
                    shapex = ShapEx(*mode)
                    shapex.add_shape_expression(input_file)

                    for i in range(10):
                        word = shapex._expression.sample()

                        self.assertTrue(word == only_word)



                except IllegalParameterError:
                    # these are handled already and can be assumed to be user errors
                    pass


    def test_kleene_word_sampler(self):
        '''
        Tests whether the output sequences are matched by the expression (with a kleene *)
        '''

        input_file = r"C:\Users\giglerf\Documents\dev\dev_code\ShapEx\shapex\tests\007.sx"
        # line(a,b,l).const(b,l).sine(a,b,c,d,l).sinc(a,b,c,d,l).exp(a,b,c,l)
        a,b,c,d,l,l2 = 'a', 'b', 'c', 'd', 'l','l2'
        phi_0 = (LineLetter(a,b,l2), ConstLetter(b,l), SineLetter(a,b,c,d,l),SincLetter(a,b,c,d,l), ExpLetter(a,b,c,l2)) # this is repeated because of kleene



        for mode in modes:
            with self.subTest(i=mode):
                try:
                    shapex = ShapEx(*mode)
                    shapex.add_shape_expression(input_file)

                    for i in range(100):
                        word = shapex._expression.sample()

                        for j in range(len(word)):
                            self.assertTrue(word[j] == phi_0[j%5])



                except (IllegalParameterError, InputError):
                    # these are handled already and can be assumed to be user errors
                    pass


    def test_union_word_sampler(self):
        '''
        Tests whether the word samplers return the single possible word for a deterministic automaton
        '''

        input_file = r"C:\Users\giglerf\Documents\dev\dev_code\ShapEx\shapex\tests\008.sx"
        # line(a,b,l).const(b,l).sine(a,b,c,d,l).sinc(a,b,c,d,l).exp(a,b,c,l)
        a,b,c,d,l,l2 = 'a', 'b', 'c', 'd', 'l','l2'

        # the two words that can be sampled
        phi_1 = (LineLetter(a,b,l2), ConstLetter(b,l), SineLetter(a,b,c,d,l))
        phi_2 = (SincLetter(a,b,c,d,l), ExpLetter(a,b,c,l2))





        for mode in modes:
            with self.subTest(i=mode):
                try:
                    shapex = ShapEx(*mode)
                    shapex.add_shape_expression(input_file)

                    for i in range(100):
                        word = shapex._expression.sample()

                        self.assertTrue(word == phi_1 or word == phi_2)



                except IllegalParameterError:
                # except (InputError, IllegalParameterError):
                    # these are handled already and can be assumed to be user errors
                    pass




def reproducibility_test(tester_self, mode, samples,input_file):
    if mode[-1]:
        # test reproducibility
        shapex2 = ShapEx(*mode)
        shapex2.add_shape_expression(input_file)
        samples2 = shapex2.samples(10)

        for i in range(len(samples)):
            for j in range(len(samples[i])):
                tester_self.assertTrue(np.all(samples[i][j].shape==samples2[i][j].shape))
                tester_self.assertTrue(np.all(samples[i][j]==samples2[i][j]))
    else: # no seed given
        # test reproducibility
        shapex2 = ShapEx(*mode)
        shapex2.add_shape_expression(input_file)
        samples2 = shapex2.samples(10)

        # the two samples should be different if no seed is given!
        same = True
        for i in range(len(samples)):
            for j in [0,1]:
                if np.all(samples[i][j].shape!=samples2[i][j].shape):
                    same = False
                    break
                    # this also means that the two samples are different and means the test passes
                    # otherwise the next line gives a warning because it cannot compare the two

                # if all the shapes are the same, at least the values should be different
                if not np.all(samples[i][j]==samples2[i][j]):
                    same = False
                    break

        tester_self.assertFalse(same, 'Output is the same even though no seed was given.')