from anyHR.constraint.Constraint import Constraints
from anyHR.constraint.node.Node import *
from typing import Tuple, Dict

from expression.Expression import *
from parse.Error import *
from parse.generated.ShapeExpressionParser import ShapeExpressionParser
from parse.generated.ShapeExpressionVisitor import ShapeExpressionVisitor
from parse.se2sa.interval import *

from anyHR.constraint.node.substitute import substitute




class SpecLoaderVisitor(ShapeExpressionVisitor):

    def visitShape_expression(self, ctx: ShapeExpressionParser.Shape_expressionContext) -> \
            (Expression, Tuple[Tuple], Constraints):
        # for ShapEx.add_shape_expression()
        reg_exp = self.visit(ctx.regular_expression())
        bounds_dict, constraints = self.visit(ctx.constraints())

        bounds_dict : Dict[str, IntervalObject]
        print(constraints)

        full_exp = (reg_exp, bounds_dict, constraints)

        return full_exp

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

        for child in ctx.children:
            if isinstance(child, ShapeExpressionParser.ConstraintContext):
                constraint_tree: Node = self.visit(child)
                test = type(constraint_tree)
                substitute(node=constraint_tree, var_val_pairs=singletons_hashmap)
                # constraint tree now has all singleton values as concrete values

                constraints.add_constraint(constraint_tree)

        # delete all the obsolete variables (constants).
        # This is unnecessary and only done to make sure none of them remain
        for var in singletons:
            bounding_box_dict.pop(var)

        bounds_ordered = dict() # same as bounding_box_dict just with same order as var_name_list
        for var in var_name_list:
            bounds_ordered[var] = bounding_box_dict[var]

        return bounds_ordered, constraints

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

    # All the visitor definitions for a constraint (same as in anyHR)
    def visitLRA_LEQ(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return LEQ(exp_1, exp_2)

    def visitLRA_GEQ(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        print(type(GEQ))
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
    from parse.generated.ShapeExpressionLexer import ShapeExpressionLexer
    from parse.se2sa.SyntaxError import MyErrorStrategy

    input_stream = FileStream(r"C:\Users\giglerf\Documents\dev\ShapEx\examples\example_after_refactoring.sx")
    lexer = ShapeExpressionLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ShapeExpressionParser(stream)
    parser._errHandler = MyErrorStrategy()
    ctx = parser.shape_expression()

    # translate to automaton
    visitor = SpecLoaderVisitor()
    exp, bounding_box, constraint = visitor.visitShape_expression(ctx)
