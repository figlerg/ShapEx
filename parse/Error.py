class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class CmdInputError(Error):
    """Exception raised for errors because of cmd inputs.

    Attributes:
        __expression -- input __expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        __expression -- input __expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class InfLoopError(Error):
    """Exception raised for too many tries to get positive/negative example.

    Attributes:
        __expression -- input __expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = 'possible infinite loop, threshold too restrictive for noise?'

class IllegalSpecError(Error):
    """Exception raised for user input that is not valid (similar to a parsing error, but might include other things as well.

    Attributes:
        __expression -- input __expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression=None, message=None):
        if not expression:
            self.expression = 'Invalid input'
        if not message:
            self.message = 'Check input file'