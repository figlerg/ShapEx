import matplotlib.pyplot as plt
import networkx as nx

from .transition import Transition


class ShapeAutomaton:
    def __init__(self):
        self.locations = set()
        self.transitions = set()
        self.initial_locations = set()
        self.final_locations = set()
        #self.parameters = set()

    def deepcopy_own(self):
        clone = ShapeAutomaton()

        d = dict()


        for location in self.locations:
            tmp = location.deepcopy_own()
            clone.add_location(tmp)
            # d[tmp.name] = location #this ensures that i can ceep track of originals, so I can keep the original structure
            d[location.name] = tmp

        for transition in self.transitions:
            cloned_source = d[transition.source.name]
            cloned_target = d[transition.target.name]
            cloned_letter = transition.letter.deepcopy_own()

            clone.add_transition(Transition(transition.name, cloned_source, cloned_target, cloned_letter))

        # for parameter in self.parameters:
        #     clone.add_parameter(parameter)
        return clone
    #for easier handling in se2sa

    def accept(self, visitor):
        visitor.visit_automaton(self)
        pass

    def undo_initial(self, location):
        if location in self.locations:
            location.is_initial = False

        if location in self.initial_locations:
            self.initial_locations.remove(location)

    def undo_final(self, location):
        if location in self.locations:
            location.is_final = False

        if location in self.final_locations:
            self.final_locations.remove(location)

    #aux fct for set of all incoming transitions
    def incoming(self,location):
        out = set()

        for transition in self.transitions:
            if transition.target == location:
                out.add(transition)
        return out

    def outgoing(self, location, include_dead_ends = True):
        out = set()

        for transition in self.transitions:
            if transition.source == location:
                if include_dead_ends:
                    out.add(transition)

                #additional condition for skipping dead ends
                elif not include_dead_ends:
                    if self.outgoing(transition.target) or transition.target.is_final:
                        out.add(transition)
                else:
                    raise Exception('2nd argument has to be boolean')
        return out


    #use this if you want the nodes instead of the edges
    def adjacent(self, location, include_dead_ends = True):
        #returns next layer of nodes, by default includes even nonfinal dead ends
        adjacent_nodes = set()

        for transition in self.outgoing(location, include_dead_ends):
            adjacent_nodes.add(transition.target)

        return adjacent_nodes




    def visualize(self):
        G = nx.DiGraph()

        for location in self.locations:
            G.add_node(location)

        for transition in self.transitions:
            G.add_edge(transition.source, transition.target, weight = 5)
            #G.edges[transition.source, transition.target]['weight'] = 5

        pos = nx.spring_layout(G)
        plt.subplot(111)

        ## fits better, but without info on final/initial
        # nx.draw(G, pos, edge_color = 'cyan', with_labels=True, node_color ='pink',
        #         labels={location:location.name for location in self.locations})


        nx.draw(G, pos, edge_color = 'black', node_color = 'cyan', with_labels=True)

        nx.draw_networkx_edge_labels(G, pos, edge_labels={(edge.source, edge.target):str(edge.letter)
                                                          for edge in self.transitions}, font_color='green')
        plt.axis('off')
        plt.tight_layout()
        plt.show()

    #aux for set of locations in the layer adjacent to the final locations (used in se2sa.kleene)
    def last_nonfinal_layer(self):
        out = set()
        for final_location in self.final_locations:
            for transition in final_location.incoming():
                out.add(transition.source)
        return out

    #transition
    def add_transition(self,transition):
        self.transitions.add(transition)

    def remove_transition(self,transition):
        self.transitions.remove(transition)

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, transitions):
        self.__transitions = transitions

#location
    def add_location(self,location):
        self.locations.add(location)

        if location.is_initial:
            self.initial_locations.add(location)

        if location.is_final:
            self.final_locations.add(location)

    def remove_location(self, location):
        self.locations.remove(location)

        if location.is_initial:
            self.initial_locations.remove(location)

        if location.is_final:
            self.final_locations.remove(location)



    @property
    def locations(self):
        return self.__locations

    @locations.setter
    def locations(self, locations):
        self.__locations = locations
        for location in locations:
            if location.is_initial:
                self.initial_locations.add(location)

            if location.is_final:
                self.final_locations.add(location)

    @property
    def initial_locations(self):
        return self.__initial_locations

    @initial_locations.setter
    def initial_locations(self, initial_locations):
        self.__initial_locations = initial_locations

    @property
    def final_locations(self):
        return self.__final_locations

    @final_locations.setter
    def final_locations(self, final_locations):
        self.__final_locations = final_locations


# #parameter
#     def add_parameter(self,parameter):
#         self.parameters.add(parameter)
#
#     @property
#     def parameters(self):
#         return self.__parameters
#
#     @parameters.setter
#     def parameters(self, parameters):
#         self.__parameters = parameters

    def __str__(self):
        out = ''
        for s in self.locations:
            out = out + str(s) + '\n'
        for t in self.transitions:
            out = out + str(t) + '\n'
        return out
    #TODO for prettier printing one could easily print initial locations first, then normal one, then final ones

