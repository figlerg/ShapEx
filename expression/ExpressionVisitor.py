from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."


class ExpressionVisitor:
    __metaclass__ = ABCMeta

    def visit(self, node, args):
        out = None

        from expression.Expression import AtomicExpression,ConcatExpression,UnionExpression,KleeneExpression

        if isinstance(node, AtomicExpression):
            out = self.visitAtomicExpression(node, args)
        elif isinstance(node, ConcatExpression):
            out = self.visitConcatExpression(node, args)
        elif isinstance(node, UnionExpression):
            out = self.visitUnionExpression(node, args)
        elif isinstance(node, KleeneExpression):
            out = self.visitKleeneExpression(node, args)
        else:
            raise Exception('Expression Visitor: unexpected method called.')
        return out

    @abstractmethod
    def visitAtomicExpression(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitConcatExpression(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitUnionExpression(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitKleeneExpression(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

