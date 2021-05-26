from alphabet.letter import Letter

from expression.ExpressionVisitor import ExpressionVisitor
from parse.se2sa.se2sa import letter_to_aut, concat_to_aut, kleene_to_aut, union_to_aut


class RE2SAVisitor(ExpressionVisitor):
    # creates an automaton object that represents the expression

    def __init__(self, expression):
        self.node = expression

    def calculate_gen_func(self):
        return self.visit(self.node, None)

    def visitAtomicExpression(self, node, args):
        return letter_to_aut(node.letter)

    def visitConcatExpression(self, node, args):
        return concat_to_aut(self.visit(node.children[0],args),self.visit(node.children[1],args))

    def visitUnionExpression(self, node, args):
        return union_to_aut(self.visit(node.children[0],args),self.visit(node.children[1],args))

    def visitKleeneExpression(self, node, args):
        return kleene_to_aut(self.visit(node.children[0],args))