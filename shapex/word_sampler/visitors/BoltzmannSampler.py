import numpy as np
from numpy.polynomial import Polynomial as P

from shapex.expression.ExpressionVisitor import ExpressionVisitor


class GenFuncVisitor(ExpressionVisitor):
    # creates an automaton object that represents the expression

    def __init__(self, expression):
        from shapex.expression import Expression
        self.root_node: Expression = expression

    def calculate_gen_func(self):
        return self.visit(self.root_node, None)

    def visitAtomicExpression(self, node, args):
        p_enum = P([0, 1])
        p_denom = P([1])

        out = (p_enum, p_denom)

        node._gen_func = out

        return out

    def visitConcatExpression(self, node, args):
        p1_enum, p1_denom = self.visit(node.children[0], None)
        p2_enum, p2_denom = self.visit(node.children[1], None)

        out = (p1_enum * p2_enum, p1_denom * p2_denom)

        node._gen_func = out

        return out

    def visitUnionExpression(self, node, args):
        p1_enum, p1_denom = self.visit(node.children[0], None)
        p2_enum, p2_denom = self.visit(node.children[1], None)

        out = (p1_enum * p2_denom + p2_enum * p1_denom, p1_denom * p2_denom)

        node._gen_func = out

        return out

    def visitKleeneExpression(self, node, args):
        p_enum, p_denom = self.visit(node.children[0], None)

        out = (p_denom, p_denom - p_enum)

        node._gen_func = out

        return out


class BoltzmannVisitor(ExpressionVisitor):
    def __init__(self, expression):

        from shapex.expression import Expression
        self.root_node: Expression = expression

    def sample(self):
        return self.visit(self.root_node, None)

    def visitAtomicExpression(self, node, args):
        return [node.letter, ]

    def visitConcatExpression(self, node, args):

        l1 = self.visit(node.children[0], None)
        l2 = self.visit(node.children[1], None)

        return l1 + l2

    def visitUnionExpression(self, node, args):
        l1 = self.visit(node.children[0], None)
        l2 = self.visit(node.children[1], None)

        g_enum, g_denom = node._gen_func
        g1_enum, g1_denom = node.children[0]._gen_func
        g2_enum, g2_denom = node.children[1]._gen_func
        z = self.root_node.word_sampler_mem['z']

        u = np.random.uniform()

        g1 = lambda x: g1_enum(x) / g1_denom(x)
        g = lambda x: g_enum(x) / g_denom(x)

        # g1/g = g1_enum * g_denom / (g1_denom * g_enum)

        if u < g1(z) / g(z):
            return l1
        else:
            return l2

    def visitKleeneExpression(self, node, args):

        g_psi_enum, g_psi_denom = node._gen_func
        g_psi = lambda x: g_psi_enum(x) / g_psi_denom(x)

        z = self.root_node.word_sampler_mem['z']

        # the recursion below has too many recursions for python- this is the equivalent loop
        out = []
        while (np.random.uniform() > 1 / (g_psi(z))):
            l1 = self.visit(node.children[0], None)
            out += l1
        else:
            return out

        # if np.random.uniform() < 1 / (g_psi(z)):
        #     return []
        # else:
        #     l1 = self.visit(node.children[0], None)
        #     return l1 + self.visit(node, None)
