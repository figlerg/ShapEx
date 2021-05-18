from se2sa.automaton.alphabet.letter import Letter
from se2sa.automaton.alphabet.letter_type import LetterType

class ExpLetter(Letter):
    def __init__(self, a, b, c, length = 'undefined'):
        #the atomic shape exponential is of the form f(x) = a + b * exp (c * x)
        self.a = a
        self.b = b
        self.c = c
        self.length = length

    def __str__(self):
        out = "exp(" + str(self.a) + ", " + str(self.b) + ", " + str(self.c) + ")"
        return out


    def get_type(self):
        return LetterType.EXP

    def deepcopy_own(self):
        return ExpLetter(self.a, self.b ,self.c, self.length)
    #for easier handling in se2sa

    def get_param_list(self, return_constant = True):
        if return_constant:
            return [self.a, self.b , self.c, self.length]
        else:
            return [self.a, self.b, self.length]




    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        self.__c = c

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length



