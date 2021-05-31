class Transition:
    def __init__(self, name, source, target, letter):
        self.name = name
        self.source = source
        self.target = target
        self.letter = letter

    def deepcopy_own(self):
        return Transition(self.name, self.source.deepcopy_own(), self.target.deepcopy_own(), self.letter)

    # for easier handling in expression2aut

    def __eq__(self, other):
        return tuple(self.__dict__.values()) == tuple(other.__dict__.values())

    def __hash__(self):
        return hash(self.__dict__.values())

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source):
        self.__source = source

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, target):
        self.__target = target

    @property
    def letter(self):
        return self.__letter

    @letter.setter
    def letter(self, letter):
        self.__letter = letter

    def __str__(self):
        source = self.source
        letter = self.letter
        target = self.target

        out = str(source) + " ---" + \
              str(letter) + "---> " + str(target)

        return out
