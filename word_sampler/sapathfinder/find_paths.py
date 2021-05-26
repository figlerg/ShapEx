from collections import deque

from typing import Set, Tuple

from alphabet.letter import Letter
from parse.se2sa.automaton.automaton import ShapeAutomaton
from parse.se2sa.automaton.transition import Transition


def find_paths(aut: ShapeAutomaton, n: int) -> Set[Transition]:

    initials = aut.initial_locations

    paths = set()
    finished_paths = set()

    # similar to breadth first search
    edge_q = deque()
    for start in initials:
        edge_q += deque([edge for edge in aut.outgoing(start, include_dead_ends=False)])
        # this adds all transition from all initial locations to a queue

        paths.update(set([(edge,) for edge in aut.outgoing(start, include_dead_ends=False)]))
        finished_paths.update(set(path for path in paths if path[0].target.is_final))

    while edge_q and (len(paths_transition2letter(finished_paths)) <= n):
        # stops once there are no discoverable nodes OR it has enough samples/valid paths

        single_discovered = edge_q.popleft()  # this is the oldest discovered edge
        # now the lists are continued/remade
        additional_paths = set()

        for path in paths:

            if path[-1].target == single_discovered.source:  # means edges are adjacent

                new_path = path + (single_discovered,)
                additional_paths.add(new_path)

                # if edge.target.is_final and new_path not in paths:
                if single_discovered.target.is_final:
                    finished_paths.add(new_path)

        paths.update(additional_paths)

        # for edge in aut.outgoing(single_discovered, include_dead_ends= False):
        for edge in aut.outgoing(single_discovered.target, include_dead_ends=False):

            edge_q.append(edge)

    # letters have practically the same information as transitions, at least for generating
    letter_paths = paths_transition2letter(finished_paths)


    short_first = sorted(letter_paths, key=len, reverse=False)
    # slicing takes care of returning the right number, should it overshoot

    return short_first[0:n]


# helper function so I can easily check how many different letter sequences have been made at any given time
def paths_transition2letter(paths: Set[Tuple[Transition]]) -> Set[Tuple[Letter]]:
    letter_paths = set()
    for path in paths:
        letter_path = tuple([transition.letter for transition in path])
        letter_paths.add(letter_path)

    return letter_paths
