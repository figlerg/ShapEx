from shapex.parse import ShapeAutomaton
from shapex.parse import Location
from shapex.parse import Transition


def letter_to_aut(letter):
    aut = ShapeAutomaton()
    s1 = Location('s1', True, False)
    s2 = Location('s2', False, True)

    t = Transition('t', s1, s2, letter)

    aut.add_location(s1)
    aut.add_location(s2)
    aut.add_transition(t)

    return aut


def union_to_aut(aut1, aut2):
    aut = ShapeAutomaton()
    locs1 = aut1.locations
    locs2 = aut2.locations

    for s in locs1:
        s.name = '1_' + s.name

    for s in locs2:
        s.name = '2_' + s.name

    aut.locations = aut.locations.union(locs1)
    aut.locations = aut.locations.union(locs2)

    trans1 = aut1.transitions
    trans2 = aut2.transitions

    for t in trans1:
        t.name = '1_' + t.name

    for t in trans2:
        t.name = '2_' + t.name

    aut.transitions = aut.transitions.union(trans1)
    aut.transitions = aut.transitions.union(trans2)

    return aut


def concat_to_aut(aut1, aut2):
    aut = ShapeAutomaton()

    # copies so I can freely change them --> do not use setters on originals!
    aut1_new = aut1.deepcopy_own()
    aut2_new = aut2.deepcopy_own()

    for s in aut1_new.locations:
        s.name = '1_' + s.name

    for s in aut2_new.locations:
        s.name = '2_' + s.name

    aut.locations = aut1_new.locations.union(aut2_new.locations)
    aut.transitions = aut1_new.transitions.union(aut2_new.transitions)

    # these are the transitions between former aut1 and former aut2
    for final_location in aut1_new.final_locations:
        for transition in aut1_new.incoming(final_location):
            for initial_b in aut2_new.initial_locations:
                detour = Transition('detour_' + transition.name, transition.source,
                                    initial_b, transition.letter)
                aut.add_transition(detour)

    for former_final in aut1_new.final_locations:
        aut.undo_final(former_final)

    for former_initial in aut2_new.initial_locations:
        aut.undo_initial(former_initial)

    aut.initial_locations = aut1_new.initial_locations

    return aut


def kleene_to_aut(aut_input):
    aut = aut_input.deepcopy_own()

    for final_location in aut.final_locations:
        for transition in aut.incoming(final_location):
            for initial_location in aut.initial_locations:
                loop_transition = Transition('loop_' + transition.name,
                                             transition.source,
                                             initial_location,
                                             transition.letter)
                aut.add_transition(loop_transition)

    for initial_location in aut.initial_locations:
        initial_location.is_final = True

    return aut
