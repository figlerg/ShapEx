# TODO like in anyHR constraints
# TODO enum switch for word sampler, etc

# TODO Boltzmann: precompute gen func, modulus
# TODO breadth first search: precompute list of paths

# import random
import warnings
from enum import Enum

import numpy as np
from numpy.polynomial import Polynomial as P

from shapex.alphabet.letter import Letter
from shapex.misc.Error import InputError, IllegalParameterError

from shapex.word_sampler.sapathfinder.find_paths import find_paths
from shapex.word_sampler.visitors.BoltzmannSampler import GenFuncVisitor, BoltzmannVisitor
from shapex.word_sampler.visitors.RE2SAVisitor import RE2SAVisitor




class WordSamplerMode(Enum):
    SEARCH = 1
    BOLTZMANN = 2

    def __eq__(self, other):
        return self.value == other.value


# TODO remove isinstance in baseclass and do it with these types instead. Should be safer
# class ExpressionType(Enum):
#     EXPRESSION = 0
#     ATOMIC = 1
#     CONCAT = 2
#     UNION = 3
#     KLEENE = 4


class Expression(object):
    def __init__(self):
        self.children = list()

        # setup for word samplers
        self.word_sampler = None
        self._word_sampler_mode = None
        self.word_sampler_mem = {}
        self._gen_func = None


    def set_sampler(self, word_sampler: WordSamplerMode = WordSamplerMode.SEARCH, budget=100, target_mu=None):
        # set opts and precompute the values necessary for sampling a word from a expression
        # this process differs depending on the word sampler chosen

        self._word_sampler_mode = word_sampler

        if word_sampler == WordSamplerMode.SEARCH:
            visitor = RE2SAVisitor(self)
            aut = visitor.create_aut()
            self.word_sampler_mem['aut'] = aut
            self.word_sampler_mem['path_list'] = find_paths(aut, budget)

            self.sample = self._search_word_sampler

        if word_sampler == WordSamplerMode.BOLTZMANN:


            # assert target_mu, \
            #     "'target_mu' parameter has not been set. Boltzmann sampling needs a target expected word length."
            visitor = GenFuncVisitor(self)
            (g_enum, g_denom), deterministic = visitor.calculate_gen_func()

            if deterministic:
                warnings.warn("The shape expression seems to be deterministic. "
                              "The Boltzmann sampler can only return one word and is equivalent to the BFS algorithm.")
                visitor = RE2SAVisitor(self)
                aut = visitor.create_aut()
                self.word_sampler_mem['aut'] = aut


                budget = 1 # this might be 0 and is not checked at the beginning if boltzmann was chosen
                self.word_sampler_mem['path_list'] = find_paths(aut, budget)

                self.sample = self._search_word_sampler
                return


            roots = g_denom.roots()  # these are the poles, rconv is the first one after 0
            pos = list([root for root in roots if (not np.iscomplex(root)) and root > 0])
            try:
                rconv = np.real(pos[0])
            except IndexError:
                rconv = float('inf')

            g_enum_prime = g_enum.deriv()
            g_denom_prime = g_denom.deriv()

            # root finding- this comes from the expected mean depending on the generating functions. We solve for z later
            # N = z*(g'(z)/g(z))
            # <-> N*g(z) -z*g'(z) = 0

            p = g_enum
            q = g_denom
            p_ = g_enum_prime
            q_ = g_denom_prime
            # the above gives us (with the quotient rule)

            poly = target_mu * p * (q ** 2) - P([0, 1]) * q * (p_ * q - q_ * p)
            roots = poly.roots()

            # this should be unique, but often something close to rconv is in here as well, so i take the 1st one
            # (probably floating point error)
            in_0_rconv = list([root for root in roots if (not np.iscomplex(root))
                               and root > 0
                               and root < rconv])


            bad_params = False
            try:
                fitting_boltzmann_param = np.real(in_0_rconv[0])
            except IndexError:
                bad_params = True

            # this structure makes the output message clearer (because the index error is not the problem)
            if bad_params:
                raise IllegalParameterError('target_word_length',target_mu,'Cannot match words of given word length.')

            self.word_sampler_mem['z'] = fitting_boltzmann_param
            # self.word_sampler_mem['z'] = 0.4

            # print(self.word_sampler_mem['z'])
            self.sample = self._boltzmann_word_sampler

            # setrecursionlimit(10000)

            # self.

    def _search_word_sampler(self):

        choice = np.random.choice(len(self.word_sampler_mem['path_list']))
        path = self.word_sampler_mem['path_list'][choice]
        return path

    def _boltzmann_word_sampler(self):
        sampler = BoltzmannVisitor(self)
        path = sampler.sample()

        return path

    # this simply raises an exception if it is called before a sampler is set
    def sample(self):
        assert False, \
            "Before sampling, you need to set the word sampler for an expression exp by calling 'exp.set_sampler(opts)'"


class AtomicExpression(Expression):
    def __init__(self, letter: Letter):
        Expression.__init__(self)
        self.letter = letter

    def __str__(self):
        return str(self.letter)


class ConcatExpression(Expression):
    def __init__(self, op1, op2):
        Expression.__init__(self)
        self.children.append(op1)
        self.children.append(op2)

    def __str__(self):
        return '(' + str(self.children[0]) + '.' + str(self.children[1]) + ')'


class UnionExpression(Expression):
    def __init__(self, op1, op2):
        Expression.__init__(self)
        self.children.append(op1)
        self.children.append(op2)

    def __str__(self):
        return '(' + str(self.children[0]) + ' union ' + str(self.children[1]) + ')'


class KleeneExpression(Expression):
    def __init__(self, op1):
        Expression.__init__(self)
        self.children.append(op1)

    def __str__(self):
        return '(' + str(self.children[0]) + '* )'
