# TODO like in anyHR constraints
# TODO enum switch for word sampler, etc

# TODO Boltzmann: precompute gen func, modulus
# TODO breadth first search: precompute list of paths

from alphabet.letter import Letter


class Expression(object):
    def __init__(self):
        self.children = list()


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
