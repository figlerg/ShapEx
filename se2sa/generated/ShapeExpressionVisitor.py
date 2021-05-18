# Generated from C:/Users/giglerf/Documents/dev/shape_gen_tool/shapes_generator_base/se2sa/grammar\ShapeExpression.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ShapeExpressionParser import ShapeExpressionParser
else:
    from ShapeExpressionParser import ShapeExpressionParser

# This class defines a complete generic visitor for a parse tree produced by ShapeExpressionParser.

class ShapeExpressionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ShapeExpressionParser#shape_expression.
    def visitShape_expression(self, ctx:ShapeExpressionParser.Shape_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#param_declaration.
    def visitParam_declaration(self, ctx:ShapeExpressionParser.Param_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#discrete_param_declaration.
    def visitDiscrete_param_declaration(self, ctx:ShapeExpressionParser.Discrete_param_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#relation.
    def visitRelation(self, ctx:ShapeExpressionParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#relation_string.
    def visitRelation_string(self, ctx:ShapeExpressionParser.Relation_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#scalar.
    def visitScalar(self, ctx:ShapeExpressionParser.ScalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#AtomicExp.
    def visitAtomicExp(self, ctx:ShapeExpressionParser.AtomicExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#KleeneExp.
    def visitKleeneExp(self, ctx:ShapeExpressionParser.KleeneExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#UnionExp.
    def visitUnionExp(self, ctx:ShapeExpressionParser.UnionExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#ParenExp.
    def visitParenExp(self, ctx:ShapeExpressionParser.ParenExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#ConcatExp.
    def visitConcatExp(self, ctx:ShapeExpressionParser.ConcatExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#AtomicConstExp.
    def visitAtomicConstExp(self, ctx:ShapeExpressionParser.AtomicConstExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#AtomicLineExp.
    def visitAtomicLineExp(self, ctx:ShapeExpressionParser.AtomicLineExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#AtomicExponentialExp.
    def visitAtomicExponentialExp(self, ctx:ShapeExpressionParser.AtomicExponentialExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#AtomicSineExp.
    def visitAtomicSineExp(self, ctx:ShapeExpressionParser.AtomicSineExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#AtomicSincExp.
    def visitAtomicSincExp(self, ctx:ShapeExpressionParser.AtomicSincExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#atomic_constant.
    def visitAtomic_constant(self, ctx:ShapeExpressionParser.Atomic_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#atomic_line.
    def visitAtomic_line(self, ctx:ShapeExpressionParser.Atomic_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#atomic_exponential.
    def visitAtomic_exponential(self, ctx:ShapeExpressionParser.Atomic_exponentialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#atomic_sine.
    def visitAtomic_sine(self, ctx:ShapeExpressionParser.Atomic_sineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#atomic_sinc.
    def visitAtomic_sinc(self, ctx:ShapeExpressionParser.Atomic_sincContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#summand.
    def visitSummand(self, ctx:ShapeExpressionParser.SummandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#interval.
    def visitInterval(self, ctx:ShapeExpressionParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#discrete_interval.
    def visitDiscrete_interval(self, ctx:ShapeExpressionParser.Discrete_intervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#number.
    def visitNumber(self, ctx:ShapeExpressionParser.NumberContext):
        return self.visitChildren(ctx)



del ShapeExpressionParser