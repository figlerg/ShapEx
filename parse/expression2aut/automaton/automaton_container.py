from collections import OrderedDict
from typing import List

from parse.expression2aut.automaton import RelationObject
from parse.expression2aut.automaton.automaton import ShapeAutomaton


class ShapeAutomatonContainer:
    def __init__(self, aut: ShapeAutomaton, shape_param: set,
                 interval_hashmap: dict = None, relations: List[RelationObject] = None):
        self.shape_param = shape_param
        self.automaton = aut
        self.intervals: OrderedDict = OrderedDict()

        # in case of a set of intervals as input, this set gets added to hashmap. default interval is [-inf,inf]
        if interval_hashmap != None:
            self.intervals.update(interval_hashmap)

        # 03/2020, extension for relational constraints
        self.relations: List[RelationObject] = relations

    def __str__(self):
        parameter_string = [par + ' in ' + str(self.intervals[par]) for par in sorted(self.shape_param)]
        # TODO revise this to include relations

        out = 'shape parameters: ' + ', '.join(map(str, parameter_string)) + '\n' + str(self.automaton)
        return out

    def visualize(self):
        self.automaton.visualize()

    def accept(self, visitor):
        # visitor.visit(self)
        self.automaton.accept(visitor)
        # self.interval.accept(visitor)

    # TODO write sat method when needed, already have corresponding methods for intervals and relations

    @property
    def automaton(self):
        return self.__automaton

    @automaton.setter
    def automaton(self, aut: ShapeAutomaton):
        self.__automaton = aut

    @property
    def shape_param(self):
        return self.__shape_param

    @shape_param.setter
    def shape_param(self, shape_param: set):
        self.__shape_param = shape_param

    @property
    def intervals(self):
        return self.__intervals

    @intervals.setter
    def intervals(self, new_intervals: set):
        self.__intervals = new_intervals

    @property
    def relations(self):
        return self.__relations

    @relations.setter
    def relations(self, new_relations: set):
        self.__relations = new_relations
