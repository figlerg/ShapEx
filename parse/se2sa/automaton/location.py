class Location:
    def __init__(self, name, is_initial, is_final):
        self.is_initial = is_initial
        self.is_final = is_final
        self.name = name

    def __str__(self):
        out = 'loc(' + self.name + ', ' + str(self.is_initial) + ', ' + str(self.is_final) + ')'
        return out

    def deepcopy_own(self):
        return Location(self.name, self.is_initial, self.is_final)
    #for easier handling in se2sa

    @property
    def is_initial(self):
        return self.__is_initial

    @is_initial.setter
    def is_initial(self, is_initial):
        self.__is_initial = is_initial

    @property
    def is_final(self):
        return self.__is_final

    @is_final.setter
    def is_final(self, is_final):
        self.__is_final = is_final

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name



