from .letter import Letter
from .letter_type import LetterType

class LineLetter(Letter):
    def __init__(self, slope, offset, length = 'undefined'):
        self.slope = slope
        self.offset = offset
        self.length = length

    def get_type(self):
        return LetterType.LINE

    def get_param_list(self, return_constant = True):
        if return_constant:
            return [self.slope, self.offset, self.length]
        else:
            return [self.slope, self.length]

    def deepcopy_own(self):
        return LineLetter(self.slope, self.offset, self.length)
    #for easier handling in se2sa


    def __str__(self):
        out = "line(" + str(self.slope) + ", " + str(self.offset) + ")"
        return out

    # def __deepcopy__(self, memo):
    #     return Location(self.name, self.is_initial, self.is_final)
    # #for easier handling in se2sa




    @property
    def slope(self):
        return self.__slope

    @slope.setter
    def slope(self, slope):
        self.__slope = slope

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset):
        self.__offset = offset

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

