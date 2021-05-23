class ShapEx(object):
    def __init__(self, mu=0, sigma=0):
        self.__expression = None  # new.
        self.__constraint = None  # from anyHR
        self.__hr = None  # from anyHR
        self.mu = mu
        self.sigma = sigma

    # TODO getters setters of these vars (property). constraint setter should reinitialise hr. hr setter should override
    #  self.__constraint. make public again, since it should be possible to do it without sx file

    def sample(self):
        path = self.__expression.sample()
        params = self.__hr.next_sample()

        example = self._create_example(path, params)

        # generate ideal example
        return example

    def samples(self):
        return

    # do n samples

    def _create_example(self, path, params):
        return

    # create_ideal
    # add_noise

    def add_shape_expression(self, filename: str):
        return
# opening file and generating __expression, etc
