#  generally, i want to eliminate constant parameters before doing any sampling
# e.g. the constraints
# 1)    "a*x+b < 10"
# 2)    "a = 13" (or rather "param a in [13,13]")
# should just result in the constraint  "13*x+b <10"
# meaning a IS NOT VIEWED AS A VARIABLE

# this is already done for the RelationObject class, but needs to be handled seperately for nonlinear relations (sympy)

from typing import Union
from sympy import StrictLessThan, LessThan, StrictGreaterThan, GreaterThan



def eliminate_var_nonlin(relation:Union[StrictLessThan, LessThan, StrictGreaterThan, GreaterThan], constant:str, value:float):
    # expects a sympy object like LessThan, etc

    # substituting a variable that is not present in a sympy relation does nothing! No problems there
    relation = relation.subs({constant:value}) # substitutes the variable with its value

    relation = relation.simplify()  # looks nicer afterwards

    try:
        made_redundant = bool(relation)
        assert made_redundant, "The set of constraints cannot be satisfied. Simply substituting all constants with the given value" \
                    "gives that one constraint is not satisfied. The parameter '" + constant + "' was involved in this " \
                                                                                               "assertion"
    except TypeError:
        # in this case at least one of the variables remain and the truth value cannot be determined
        # this is nowhere near as powerful as z3, but it should work for something that can be easily determined
        made_redundant = False
        pass

    # the return value is just an indicator of whether this resulted in something like 1 < 10 in which case no relation shall be added
    return relation, made_redundant