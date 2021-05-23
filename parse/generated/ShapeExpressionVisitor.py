# Generated from C:/Users/giglerf/Documents/dev/ShapEx/parse/grammar\ShapeExpression.g4 by ANTLR 4.9.1
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


    # Visit a parse tree produced by ShapeExpressionParser#constraints.
    def visitConstraints(self, ctx:ShapeExpressionParser.ConstraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#param_declaration.
    def visitParam_declaration(self, ctx:ShapeExpressionParser.Param_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#duration_declaration.
    def visitDuration_declaration(self, ctx:ShapeExpressionParser.Duration_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#LRA_LEQ.
    def visitLRA_LEQ(self, ctx:ShapeExpressionParser.LRA_LEQContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#LRA_GEQ.
    def visitLRA_GEQ(self, ctx:ShapeExpressionParser.LRA_GEQContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#LRA_Less.
    def visitLRA_Less(self, ctx:ShapeExpressionParser.LRA_LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#LRA_Greater.
    def visitLRA_Greater(self, ctx:ShapeExpressionParser.LRA_GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#LRA_Eq.
    def visitLRA_Eq(self, ctx:ShapeExpressionParser.LRA_EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#LRA_Neq.
    def visitLRA_Neq(self, ctx:ShapeExpressionParser.LRA_NeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#LRA_In.
    def visitLRA_In(self, ctx:ShapeExpressionParser.LRA_InContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#ExpressionParanthesis.
    def visitExpressionParanthesis(self, ctx:ShapeExpressionParser.ExpressionParanthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#ExpressionMultiplication.
    def visitExpressionMultiplication(self, ctx:ShapeExpressionParser.ExpressionMultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#ExpressionSubtraction.
    def visitExpressionSubtraction(self, ctx:ShapeExpressionParser.ExpressionSubtractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#ExpressionAddition.
    def visitExpressionAddition(self, ctx:ShapeExpressionParser.ExpressionAdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#ExpressionVariable.
    def visitExpressionVariable(self, ctx:ShapeExpressionParser.ExpressionVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#ExpressionConstant.
    def visitExpressionConstant(self, ctx:ShapeExpressionParser.ExpressionConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#ExpressionExponential.
    def visitExpressionExponential(self, ctx:ShapeExpressionParser.ExpressionExponentialContext):
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


    # Visit a parse tree produced by ShapeExpressionParser#interval.
    def visitInterval(self, ctx:ShapeExpressionParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#discrete_interval.
    def visitDiscrete_interval(self, ctx:ShapeExpressionParser.Discrete_intervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShapeExpressionParser#literal.
    def visitLiteral(self, ctx:ShapeExpressionParser.LiteralContext):
        return self.visitChildren(ctx)



del ShapeExpressionParser