class IntervalObject:
    def __init__(self, newstart:float=float("-inf"), newend:float=float("inf"), is_discrete=False, timestep = False):

        if newstart > newend:
            tmp = newstart
            newstart = newend # this doesn't change anything outside of function
            newend = tmp
            print('WARNING: One of the Intervals [a,b] satisfies b < a. This is switched automatically.')


        self.start = newstart
        self.end = newend
        self.is_discrete = is_discrete
        self.timestep = timestep

    def __str__(self):
        if self.is_discrete:
            discrete_mark = ' (discrete)'
        else:
            discrete_mark = ''

        return '[' + str(self.start) + ', ' + str(self.end) + ']' + discrete_mark

    def is_unbounded(self):
        return self.start == float('-inf') and self.end == float ('inf')

    def sat(self, value):
        return self.start <= value <= self.end

    def is_singleton(self):
        # simple check whether the interval contains just one number
        return self.start == self.end

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start:float):
        self.__start = start

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end: float):
        self.__end = end

    @property
    def is_discrete(self):
        return self.__is_discrete

    @is_discrete.setter
    def is_discrete(self, is_discrete:bool):
        self.__is_discrete = is_discrete

    @property
    def timestep(self):
        return self.__timestep

    @timestep.setter
    def timestep(self, timestep:float):
        self.__timestep = timestep