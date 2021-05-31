from typing import Tuple, Dict

from anyHR.constraint.Constraint import Constraints
from anyHR.constraint.node.Node import *
from anyHR.constraint.node.substitute import substitute

from shapex.alphabet.const_letter import ConstLetter
from shapex.alphabet.exp_letter import ExpLetter
from shapex.alphabet import LineLetter
from shapex.alphabet import SincLetter
from shapex.alphabet import SineLetter
from shapex.misc.Error import *
from shapex.parse.generated import ShapeExpressionParser
from shapex.parse.generated import ShapeExpressionVisitor
from shapex.parse.expression2aut.automaton.interval import IntervalObject


class SpecLoaderVisitor(ShapeExpressionVisitor):

    def visitShape_expression(self, ctx: ShapeExpressionParser.Shape_expressionContext) -> \
            (Expression, Tuple[Tuple], Constraints):
        # for ShapEx.add_shape_expression()
        reg_exp = self.visit(ctx.regular_expression())
        bounds_dict, constraints, singletons_hashmap = self.visit(ctx.constraints())

        bounds_dict: Dict[str, IntervalObject]

        full_exp = (reg_exp, bounds_dict, constraints, singletons_hashmap)

        return full_exp

    # get the regular expression

    def visitAtomicConstExp(self, ctx):
        self.visitChildren(ctx)

        c = ctx.atomic_constant().Identifier(0).getText()

        shape_param = {c}
        l = ConstLetter(c)

        try:  # because its optional, maybe there is no Identifier(0) or Identifier(1)

            length = ctx.atomic_constant().Identifier(1).getText()
            shape_param.add(length)
            l.length = length
        except:
            pass

        return AtomicExpression(l)

    def visitAtomicLineExp(self, ctx):

        self.visitChildren(ctx)
        slope = ctx.atomic_line().Identifier(0).getText()
        offset = ctx.atomic_line().Identifier(1).getText()

        shape_param = {slope, offset}
        l = LineLetter(slope, offset)

        # optional parameter length!
        try:
            length = ctx.atomic_line().Identifier(2).getText()

            shape_param.add(length)
            l.length = length
        except:
            pass

        return AtomicExpression(l)

    def visitAtomicExponentialExp(self, ctx):
        self.visitChildren(ctx)
        a = ctx.atomic_exponential().Identifier(0).getText()
        b = ctx.atomic_exponential().Identifier(1).getText()
        c = ctx.atomic_exponential().Identifier(2).getText()

        shape_param = {a, b, c}
        l = ExpLetter(a, b, c)

        try:
            length = ctx.atomic_exponential().Identifier(3).getText()

            shape_param.add(length)
            l.length = length

        except:
            pass

        return AtomicExpression(l)

    def visitAtomicSineExp(self, ctx):
        self.visitChildren(ctx)
        a = ctx.atomic_sine().Identifier(0).getText()
        b = ctx.atomic_sine().Identifier(1).getText()
        c = ctx.atomic_sine().Identifier(2).getText()
        d = ctx.atomic_sine().Identifier(3).getText()

        shape_param = {a, b, c, d}
        l = SineLetter(a, b, c, d)

        try:
            length = ctx.atomic_sine().Identifier(4).getText()

            shape_param.add(length)
            l.length = length

        except:
            pass

        return AtomicExpression(l)

    def visitAtomicSincExp(self, ctx):
        self.visitChildren(ctx)
        a = ctx.atomic_sinc().Identifier(0).getText()
        b = ctx.atomic_sinc().Identifier(1).getText()
        c = ctx.atomic_sinc().Identifier(2).getText()
        d = ctx.atomic_sinc().Identifier(3).getText()

        shape_param = {a, b, c, d}
        l = SincLetter(a, b, c, d)

        try:
            length = ctx.atomic_sinc().Identifier(4).getText()

            shape_param.add(length)
            l.length = length

        except:
            pass

        return AtomicExpression(l)

    def visitConcatExp(self, ctx: ShapeExpressionParser.ConcatExpContext):

        exp_1 = self.visit(ctx.regular_expression(0))
        exp_2 = self.visit(ctx.regular_expression(1))

        return ConcatExpression(exp_1, exp_2)

    def visitUnionExp(self, ctx: ShapeExpressionParser.UnionExpContext):

        exp_1 = self.visit(ctx.regular_expression(0))
        exp_2 = self.visit(ctx.regular_expression(1))

        return UnionExpression(exp_1, exp_2)

    def visitKleeneExp(self, ctx: ShapeExpressionParser.KleeneExpContext):

        exp = self.visit(ctx.regular_expression())

        return KleeneExpression(exp)

    def visitParenExp(self, ctx: ShapeExpressionParser.ParenExpContext):

        exp_in_parens = self.visit(ctx.regular_expression())

        return exp_in_parens

    # param declaration visitors
    def visitParam_declaration(self, ctx: ShapeExpressionParser.Param_declarationContext) -> (str, IntervalObject):
        name = ctx.Identifier().getText()
        interval = self.visit(ctx.interval())

        return name, interval

    def visitInterval(self, ctx: ShapeExpressionParser.IntervalContext) -> IntervalObject:
        start = self.visit(ctx.literal(0))
        end = self.visit(ctx.literal(1))

        interval = IntervalObject(start, end, is_discrete=False)

        return interval

    def visitDuration_declaration(self, ctx: ShapeExpressionParser.Duration_declarationContext) -> (
            str, IntervalObject):
        name = ctx.Identifier().getText()
        interval = self.visit(ctx.discrete_interval())

        return name, interval

    def visitDiscrete_interval(self, ctx: ShapeExpressionParser.Discrete_intervalContext) -> IntervalObject:
        start = self.visit(ctx.literal(0))
        end = self.visit(ctx.literal(1))

        interval = IntervalObject(start, end, is_discrete=True)

        return interval

    # get all constraints
    def visitConstraints(self, ctx: ShapeExpressionParser.ConstraintsContext):

        bounding_box_dict = {}

        duplicate_check_set = set()
        for child in ctx.children:
            if isinstance(child, (ShapeExpressionParser.Duration_declarationContext,
                                  ShapeExpressionParser.Param_declarationContext)):
                param_interval: tuple = self.visit(child)
                bounding_box_dict.update((param_interval,))

                param = param_interval[0]

                # Multiple declarations for one param are illegal
                if param in duplicate_check_set:
                    raise IllegalSpecError(message='Please check input file for parameter declaration duplicates')
                duplicate_check_set.update(param)

        bounding_box_dict = dict(sorted(bounding_box_dict.items()))  # sort by key

        # parameters with intervals of the type (x,x) are later substituted and are searched here
        singletons = []
        singletons_hashmap = dict()
        for item in bounding_box_dict.items():
            interval: IntervalObject = item[1]
            if interval.is_singleton():
                singletons.append(item[0])
                singletons_hashmap[item[0]] = item[1].start

        # in the final constraints object only non singular values will appear
        var_name_list = sorted(set(bounding_box_dict.keys()) - set(singletons))

        constraints = Constraints(var_name_list)

        var_checkup_set = set()
        for child in ctx.children:
            if isinstance(child, ShapeExpressionParser.Constraint_declarationContext):
                constraint_tree: Node = self.visit(child)

                substitute(node=constraint_tree, var_val_pairs=singletons_hashmap)
                # constraint tree now has all singleton values as concrete values

                var_checkup_set.update(constraint_tree.get_vars())

                constraints.add_constraint(constraint_tree)

        assert var_checkup_set.issubset(var_name_list), 'Some variables have not been properly declared. ' \
                                                        'Check for implicitly declared variables in constraints.'

        # delete all the obsolete variables (constants).
        # This is unnecessary and only done to make sure none of them remain
        for var in singletons:
            bounding_box_dict.pop(var)

        bounds_ordered = dict()  # same as bounding_box_dict just with same order as var_name_list
        for var in var_name_list:
            bounds_ordered[var] = bounding_box_dict[var]

        return bounds_ordered, constraints, singletons_hashmap

    def visitConstraint_declaration(self, ctx: ShapeExpressionParser.Constraint_declarationContext):
        return self.visit(ctx.constraint())

    # All the visitor definitions for a constraint (same as in anyHR)
    def visitLRA_LEQ(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return LEQ(exp_1, exp_2)

    def visitLRA_GEQ(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return GEQ(exp_1, exp_2)

    def visitLRA_Less(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return Less(exp_1, exp_2)

    def visitLRA_Greater(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return Greater(exp_1, exp_2)

    def visitLRA_Eq(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return EQ(exp_1, exp_2)

    def visitLRA_Neq(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return NEQ(exp_1, exp_2)

    def visitLRA_In(self, ctx):
        exp = self.visit(ctx.expression(0))
        exp_low = self.visit(ctx.expression(1))
        exp_up = self.visit(ctx.expression(2))
        return In(exp, exp_low, exp_up)

    def visitExpressionVariable(self, ctx) -> Node:
        var_name = ctx.Identifier().getText()
        var = Variable(var_name)
        return var

    def visitExpressionConstant(self, ctx) -> Node:
        value = float(ctx.literal().getText())
        constant = Constant(value)
        return constant

    def visitExpressionAddition(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))

        exp = Addition(exp_1, exp_2)

        return exp

    def visitExpressionSubtraction(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return Subtraction(exp_1, exp_2)

    def visitExpressionMultiplication(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return Multiplication(exp_1, exp_2)

    def visitExpressionExponential(self, ctx) -> Node:
        exp = self.visit(ctx.expression())
        return Exponential(exp)

    def visitExpressionParenthesis(self, ctx):
        return self.visit(ctx.expression())

    def visitLiteral(self, ctx: ShapeExpressionParser.LiteralContext):
        return float(ctx.getText())


if __name__ == '__main__':
    from antlr4 import *
    from shapex.parse.generated import ShapeExpressionLexer
    from shapex.parse import HardSyntaxErrorStrategy

    input_stream = FileStream(r"C:\Users\giglerf\Documents\dev\ShapEx\examples\example_after_refactoring.sx")
    lexer = ShapeExpressionLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ShapeExpressionParser(stream)
    parser._errHandler = HardSyntaxErrorStrategy()
    ctx = parser.shape_expression()

    # translate to automaton
    visitor = SpecLoaderVisitor()
    exp, bounding_box, constraint = visitor.visitShape_expression(ctx)
