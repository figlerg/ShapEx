from alphabet.letter import Letter
from alphabet.letter_type import LetterType

class ConstLetter(Letter):
    def __init__(self, c, length = 'undefined'):
        self.c = c
        self.length = length

    def __str__(self):
        out = "const(" + str(self.c) + ")"
        return out


    def get_type(self):
        return LetterType.CONST

    def deepcopy_own(self):
        return ConstLetter(self.c, self.length)

    def get_param_list(self, return_constant = True):
        if return_constant:
            return [self.c, self.length]
        else:
            return [self.length]





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
