from sympy import StrictLessThan, StrictGreaterThan, LessThan, GreaterThan
from sympy import Lt, Le, Gt, Ge
from typing import Set

import sympy
import re

def str2sympy(raw_text:str):
    # this function creates a sympy object according to a general inequality
    # for example, the string "a*b+7 >= 10" will be transformed to Le((-a*b+7) +10, 0) (so some standardization happens as well)

    # the following was created because i did not know that function sympify existed (would have been much easier).
    # I keep it for checking that
    # the __constraint indeed has exactly one inequality
    rel_types = ['<=', '>=', '<', '>']
    found = {}
    tmp = raw_text
    for rel in rel_types:
        # see https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
        idx = [m.start() for m in re.finditer(rel, tmp)]
        assert len(idx) <= 1, "Chained inequalities not allowed in nonlin __constraint."
        if idx:
            tmp = tmp[:idx[0]] + ' '*len(rel) + tmp[idx[0] + len(rel):]
            # replace every rel found with spaces in order to avoid duplicates in case of '<','<=' while still
            # maintaining the right length
            found[rel] = idx[0]

    assert len(found) == 1, "Nonlinear __constraint '" + raw_text +\
                            "' is invalid, there needs to be exactly one inequality."

    rel_str = list(found.keys())[0]
    idx = found[rel_str]



    # this is where the actual relation is created with sympify
    rel = sympy.sympify(raw_text)

    # TODO right now, everything is transformed to <=.
    #  I think, this is implied in hit-and-run? not sure if equality is allowed or not allowed....

    # transform to g(x) <= 0:
    # if rel_str == '<=':
    #     rel = Le(rel.lhs-rel.rhs, 0)
    # elif rel_str == '>=':
    #     rel = Le(rel.rhs-rel.lhs, 0) # automatically flip
    # elif rel_str == '<':
    #     rel = Le(rel.lhs-rel.rhs, 0)
    #     # rel = Lt(rel.lhs-rel.rhs, 0) # not sure if strict is ok?
    # elif rel_str == '>':
    #     rel = Le(rel.rhs-rel.lhs, 0) # automatically flip
    #     # rel = Lt(rel.rhs-rel.lhs, 0) # not sure if strict is ok?

    return rel


if __name__ == '__main__':
    input = 'a*b > 22'

    rel = str2sympy(input)

    print(rel)

    print(rel.subs({'a':3,'b':7}))
    print(rel.lhs.subs({'a':3,'b':7}))




