# TODO like in anyHR constraints
# TODO enum switch for word sampler, etc

# TODO Boltzmann: precompute gen func, modulus
# TODO breadth first search: precompute list of paths

from enum import Enum

import random
# TODO set seeds in this file

from alphabet.letter import Letter
from word_sampler.sapathfinder.find_paths import find_paths
from word_sampler.visitors.RE2SAVisitor import RE2SAVisitor


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
            # visitor = BoltzmannVisitor(self)
            pass

    def _search_word_sampler(self):
        out = random.choice(self.word_sampler_mem['path_list'])
        return out

    def _boltzmann_word_sampler(self, target_mean, ):
        pass

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
