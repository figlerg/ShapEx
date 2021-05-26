from alphabet import ConstLetter
from alphabet.exp_letter import ExpLetter
from alphabet import LineLetter
from alphabet import SincLetter
from alphabet import SineLetter
from parse.se2sa.automaton.automaton_container import ShapeAutomatonContainer
from parse.se2sa.interval import IntervalObject
from parse.se2sa.automaton.relation import RelationObject
from parse.generated.ShapeExpressionParser import ShapeExpressionParser
from parse.generated.ShapeExpressionVisitor import ShapeExpressionVisitor
from parse.se2sa.se2sa import *

from parse.se2sa.eliminate_var_nonlin import eliminate_var_nonlin

from sympy import StrictLessThan, LessThan, StrictGreaterThan, GreaterThan


# TODO won't work after refactoring of grammar- create new visitor for "expression" objects

class SEToSAVisitor(ShapeExpressionVisitor):
    def visitShape_expression(self, ctx: ShapeExpressionParser.Shape_expressionContext):
        # self.visitChildren(ctx)

        container: ShapeAutomatonContainer = self.visit(ctx.expression())
        letters = [transition.letter for transition in container.automaton.transitions]

        tuples = []
        durations_tuples = []

        relations = []  # this is the collection of relations, to be stored in new "relations" attribute of the container

        nr_of_normal_param = 0
        nr_of_discrete_param = 0

        nr_of_relations = 0
        nr_of_str_relations = 0

        for i in range(ctx.getChildCount()):
            if isinstance(ctx.children[i], ShapeExpressionParser.Param_declarationContext):
                pair = self.visit(ctx.param_declaration(nr_of_normal_param))
                nr_of_normal_param += 1
                tuples.append(pair)
                # nondiscrete case
            if isinstance(ctx.children[i], ShapeExpressionParser.Duration_declarationContext):
                pair = self.visit(ctx.duration_declaration(nr_of_discrete_param))
                nr_of_discrete_param += 1
                durations_tuples.append(pair)
                # discrete case
            if isinstance(ctx.children[i], ShapeExpressionParser.RelationContext):
                # addition for relation-object. 03.2020. (Felix)
                rel = self.visit(ctx.relation(nr_of_relations))
                nr_of_relations += 1
                relations.append(rel)
            if isinstance(ctx.children[i], ShapeExpressionParser.Relation_stringContext):
                # addition for user defined relations (to include nonlinear ones). 10.2020 (Felix)
                rel = self.visit(ctx.relation_string(nr_of_str_relations))
                nr_of_str_relations += 1
                relations.append(rel)





        params_list = [visited_param for (visited_param,_) in tuples + durations_tuples]
        assert len(params_list) == len(set(params_list)), "Only a single interval is allowed for each parameter, " \
                                                          "check specification! "
        # multiple intervals for a single parameter are most likely an error in the specification and are illegal




        # have to do it like this because I do not know which child is discrete, real, or even shape exp

        container.relations = relations

        # now to load the lengths:

        # This is the first return value, a dict mapping a parameter to its interval
        parameter_intervals:dict = dict([*tuples, *durations_tuples])
        container.intervals = parameter_intervals


        # addition 10/2020 to support relations together with singleton/constant parameters (param x in [3,3])
        for param in container.intervals.keys():
            interval:IntervalObject = container.intervals[param]
            if interval.is_singleton():

                # in all relations i substitute the constant variable, both for my own linear objects as well as the
                # sympy ones that are used for nonlinear
                # TODO to decrease complexity i could ditch my relation object and just use the sympy ones everywhere

                redundant_indices = []
                for i, relation in enumerate(container.relations):
                    if isinstance(relation,RelationObject):
                        relation:RelationObject

                        relation.eliminate_variable(param, interval.start)
                    if isinstance(relation, (StrictLessThan, LessThan, StrictGreaterThan, GreaterThan)):
                        relation, redundant_flag = eliminate_var_nonlin(relation, param, interval.start)
                        if redundant_flag:
                            redundant_indices.append(i)

                redundant_indices.reverse()

                # removes things like "1<10"
                for i in redundant_indices:
                    del container.relations[i]






        # for the path to trace functions I now need {letter:duration}:
        letter_duration_pairs = []
        for letter in letters:
            letter_duration_pairs.append((letter, parameter_intervals[letter.length]))
        letters_durations_dict = {}
        letters_durations_dict.update(letter_duration_pairs)

        return container, letters_durations_dict

    # TODO maybe the dependencies between visitors can be improved

    def visitRelation(self, ctx: ShapeExpressionParser.RelationContext):
        # this is an addition to the grammar to enable relational parameter declarations (convex polytopes like Ax<=b)
        # print(ctx.summand(0).number().getText())
        n = len(ctx.summand())

        # b_i = self.visit(ctx.number()) # TODO write a separate visitor instead of casting text directly to float
        b_i = float(ctx.number().getText())

        test = ctx.getChild(1)

        # is_lowerequal = (ctx.INEQ().getText() == '<=')

        comp = ctx.COMP_OP().getText()

        assert comp in ['<=', '>='], "'" + comp + "'" + " not yet implemented."

        is_lowerequal = (comp == '<=')  # this might be problematic should i decide to support "=="
        # this parameter is needed to automatically flip signs for greater_equal specification
        # (to be compatible with volesti)

        summands = [self.visit(ctx.summand(i)) for i in range(n)]
        param = [summands[i][0] for i in range(n)]
        coeff = [summands[i][1] for i in range(n)]
        relation = RelationObject(coeff=coeff, param=param, b_i=b_i,
                                  is_lowerequal=is_lowerequal)  # initialize a relation object without params

        # print(relation)

        return relation

    def visitRelation_string(self, ctx:ShapeExpressionParser.Relation_stringContext):
        # TODO refactor name if i decide to switch to sympy relations completely!
        # return str2sympy(ctx.getText()[6:-1])
        # add .replace('e','E')) to automatically eliminate stuff when using dejan's format?
        # return str2sympy(ctx.getText()[6:-1]) # return normal sympy _expression
        return ctx.getText()[6:-1] # exclude keyword and ';', just text
        # return ctx.getText()[7:-2] # TODO temporary exclude keyword, string parens and ';'

    def visitSummand(self, ctx: ShapeExpressionParser.SummandContext):
        # should return coefficient and parameter ID to relation
        param = ctx.ID().getText()

        # the following is needed for common inputs like "+y", "-y" or "y"
        try:
            coeff = float(ctx.number().getText())
            try:
                if ctx.SIGN().getText() == '-':
                    coeff = -coeff
            except AttributeError:
                pass
        except AttributeError:
            try:
                sign_string = ctx.SIGN().getText()

                if sign_string == '-':
                    coeff = -1.
                elif sign_string == '+':
                    coeff = 1.
            except AttributeError:
                coeff = 1.

        return (param, coeff)

    def visitParam_declaration(self, ctx):
        # self.visitChildren(ctx) #interesting tokens are being visited explicitly
        param = ctx.ID().getText()

        try:  # need exception for param declarations without explicit interval
            param_interval = self.visit(ctx.interval())
            return (param, param_interval)
        except:
            param_interval = IntervalObject()
            return (param, param_interval)

    def visitDuration_declaration(self, ctx: ShapeExpressionParser.Duration_declarationContext):
        param = ctx.ID().getText()

        try:  # need exception for param declarations without explicit interval
            param_interval = self.visit(ctx.discrete_interval())
            return (param, param_interval)
        except:
            param_interval = IntervalObject(2, float('inf'), is_discrete=True)
            # this is the default, durations only make sense >2
            return (param, param_interval)

    def visitInterval(self, ctx):
        self.visitChildren(ctx)

        # start = ctx.number(0).getText()
        # end = ctx.number(1).getText()
        start = float(ctx.number(0).getText())
        end = float(ctx.number(1).getText())

        interval = IntervalObject(start, end)

        return interval

    def visitDiscrete_interval(self, ctx: ShapeExpressionParser.Discrete_intervalContext):
        self.visitChildren(ctx)
        non_integer = False
        corrective_index_int = 0 # this one's necessary t know which index has to be used in second try.
        corrective_index_float = 0

        try:
            # this is the original version with only integer lengths.
            start = int(ctx.INT(0).getText())
            corrective_index_int = 1
        except AttributeError:
            # in case it doesn't find an INT, non integer duration mode is invoked
            non_integer = True
            corrective_index_float = 1
            start = float(ctx.DOUBLE(0).getText())

        # two try statements so mixed intervals are possible
        try:
            end = int(ctx.INT(corrective_index_int).getText())
        except AttributeError:
            non_integer = True
            end = float(ctx.DOUBLE(corrective_index_float).getText())

        # here it does not yet matter whether these are actually int or float, class constructor does not check for
        # it. However, if floats are detected, it is to be assumed that there is a non-trivial timestep and the
        # interval gets an appropriate attribute "timestep" for that.
        interval = IntervalObject(start, end, is_discrete=True, timestep=non_integer)

        return interval

    def visitAtomicConstExp(self, ctx):
        self.visitChildren(ctx)

        c = ctx.atomic_constant().ID(0).getText()

        shape_param = {c}
        l = ConstLetter(c)

        try:  # because its optional, maybe there is no ID(0) or ID(1)

            length = ctx.atomic_constant().ID(1).getText()
            shape_param.add(length)
            l.length = length
        except:
            pass

        aut = letter_to_aut(l)

        container = ShapeAutomatonContainer(aut, shape_param)

        return container

    def visitAtomicLineExp(self, ctx):

        self.visitChildren(ctx)
        slope = ctx.atomic_line().ID(0).getText()
        offset = ctx.atomic_line().ID(1).getText()

        shape_param = {slope, offset}
        l = LineLetter(slope, offset)

        # optional parameter length!
        try:
            length = ctx.atomic_line().ID(2).getText()

            shape_param.add(length)
            l.length = length
        except:
            pass

        aut = letter_to_aut(l)

        container = ShapeAutomatonContainer(aut, shape_param)

        return container

    def visitAtomicExponentialExp(self, ctx):
        self.visitChildren(ctx)
        a = ctx.atomic_exponential().ID(0).getText()
        b = ctx.atomic_exponential().ID(1).getText()
        c = ctx.atomic_exponential().ID(2).getText()

        shape_param = {a, b, c}
        l = ExpLetter(a, b, c)

        try:
            length = ctx.atomic_exponential().ID(3).getText()

            shape_param.add(length)
            l.length = length

        except:
            pass

        aut = letter_to_aut(l)

        container = ShapeAutomatonContainer(aut, shape_param)

        return container

    def visitAtomicSineExp(self, ctx):
        self.visitChildren(ctx)
        a = ctx.atomic_sine().ID(0).getText()
        b = ctx.atomic_sine().ID(1).getText()
        c = ctx.atomic_sine().ID(2).getText()
        d = ctx.atomic_sine().ID(3).getText()

        shape_param = {a, b, c, d}
        l = SineLetter(a, b, c, d)

        try:
            length = ctx.atomic_sine().ID(4).getText()

            shape_param.add(length)
            l.length = length

        except:
            pass

        aut = letter_to_aut(l)

        container = ShapeAutomatonContainer(aut, shape_param)

        return container

    def visitAtomicSincExp(self, ctx):
        self.visitChildren(ctx)
        a = ctx.atomic_sinc().ID(0).getText()
        b = ctx.atomic_sinc().ID(1).getText()
        c = ctx.atomic_sinc().ID(2).getText()
        d = ctx.atomic_sinc().ID(3).getText()

        shape_param = {a, b, c, d}
        l = SincLetter(a, b, c, d)

        try:
            length = ctx.atomic_sinc().ID(4).getText()

            shape_param.add(length)
            l.length = length

        except:
            pass

        aut = letter_to_aut(l)

        container = ShapeAutomatonContainer(aut, shape_param)

        return container

    def visitConcatExp(self, ctx):

        aut1_container = self.visit(ctx.expression(0))
        aut2_container = self.visit(ctx.expression(1))

        aut1 = aut1_container.automaton
        aut2 = aut2_container.automaton

        aut = concat_to_aut(aut1, aut2)
        parameter_set = aut1_container.shape_param.union(aut2_container.shape_param)

        container = ShapeAutomatonContainer(aut, parameter_set)

        return container

    def visitUnionExp(self, ctx):

        aut1_container = self.visit(ctx.expression(0))
        aut2_container = self.visit(ctx.expression(1))

        aut1 = aut1_container.automaton
        aut2 = aut2_container.automaton

        aut = union_to_aut(aut1, aut2)
        parameter_set = aut1_container.shape_param.union(aut2_container.shape_param)

        container = ShapeAutomatonContainer(aut, parameter_set)

        return container

    def visitKleeneExp(self, ctx):

        input_container = self.visit(ctx.expression())

        aut = kleene_to_aut(input_container.automaton)
        shape_param = input_container.shape_param

        container = ShapeAutomatonContainer(aut, shape_param)

        return container

    def visitParenExp(self, ctx):

        container_in_parens = self.visit(ctx.expression())

        return container_in_parens
