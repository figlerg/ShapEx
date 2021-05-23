from alphabet.letter import Letter
from alphabet.letter_type import LetterType

class SineLetter(Letter):
    def __init__(self, a, b, c, d, length = 'undefined'):
        #the atomic shape sine is of the form f(x) = a * sin(b * x + c) + d
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.length = length

    def __str__(self):
        out = "sine(" + str(self.a) + ", " + str(self.b) + ", " +\
              str(self.c) + ", " + str(self.d) +")"
        return out


    def get_type(self):
        return LetterType.SINE

    def deepcopy_own(self):
        return SineLetter(self.a, self.b , self.c, self.d, self.length)
    #for easier handling in se2sa

    def get_param_list(self, return_constant = True):
        if return_constant:
            return [self.a, self.b , self.c, self.d, self.length]
        else:
            return [self.a, self.b, self.c, self.length]




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
    def d(self):
        return self.__d

    @d.setter
    def d(self, d):
        self.__d = d

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length



