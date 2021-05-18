from typing import Tuple, List, Dict
from se2sa.automaton.alphabet import letter
import numpy as np


class RelationObject:

    def __init__(self, coeff: List[float], param: List[str], b_i: float, is_lowerequal: bool):
        # this is a relation defined by vectors coeff and param, scalar b_i: dot(a,x)<=b_i
        # each row of the matrix needed for volesti will be given as one of these

        # the boolean handles the multiplication of both sides with (-1), should there be a greater-equal sign

        assert len(param) == len(coeff), 'invalid relation input: constructor needs same nr of params and coeffs'
        assert len(param) == len(
            set(param)), 'all parameter IDs must be unique, automatic simplification is not supported'

        if is_lowerequal:
            self.param = param
            self.coeff = coeff
            self.b_i = b_i
        else:
            # this takes care of differing inequalities:
            self.param = param
            self.coeff = list(-np.asarray(coeff))
            self.b_i = -b_i

    def __str__(self):
        # this creates a string for a line in .ine format for volesti
        # TODO check if param is in the right order

        # return(str(self.b_i) + " ".join([p for p in self.param]))
        # THIS STYLE IS NOT USEFUL, since internally the relation doesn't know the full list of params
        #  -> there could be more (some coeff == 0), need to fix an order!

        # instead: TODO let __str__ return a "mathematical" notation, a1x1 + a2x2 + ... <= b_i

        signs = np.sign(self.coeff)
        plus_minus_string = ''
        for i in range(len(signs)):
            if signs[i] == 1:
                plus_minus_string += '+'
            elif signs[i] == -1:
                plus_minus_string += '-'
            elif signs[i] == 0:
                plus_minus_string += '+' # np.sign returns 0 for 0, this messes with things later
            else:
                print('this should be unreachable, check __str__ of relation')

        coeff_str_abs = [str(abs(a)) for a in self.coeff]

        coeff_with_signs = list(zip(plus_minus_string, coeff_str_abs))

        # print(coeff_with_signs)
        n = len(self.param)
        # TODO The '*' is really not nice to look at, but is needed for the z3 syntax. Might do a nicer str for user
        #  output as separate function
        return " ".join(
            [coeff_with_signs[i][0] + coeff_with_signs[i][1] + '*' + self.param[i] for i in range(n)]) + ' <= ' + str(
            self.b_i)

    def eliminate_variable(self, variable: str, value: float):
        # this is the simplest form of an equality constraint and it should be easy to handle:
        # say we know that for this relation a1*x1 + ... + an*xn <= b we also know that xm = c
        # now it is easy to reformulate this relation as
        # a1*x1 + ... a(m-1)*x(m-1) + a(m+1)*x(m+1)+ .. + an*xn <= b - am*c
        # TODO this elimination should also be possible for general subrooms, right?

        try:
            idx = self.param.index(variable)

            if len(self.coeff) == 1:
                # it could be the case that this is the last variable of the relation. This way we can check whether
                #  the value inserted can satisfy the constraint. If not, it throws.
                #  Otherwise the relation is not necessary anymore and will be left empty
                #  (should be no problem in volesti?)
                assert self.coeff[0] * value <= self.b_i, \
                    "Elimination of constant variables failed: " \
                    "Maybe there are constant values that are incompatible with given relational constraints?"
                # TODO does this need to do something else?

        except ValueError:
            return 0

        self.b_i = self.b_i - self.coeff[idx] * value
        del self.coeff[idx]
        del self.param[idx]

        return 1

    @property
    def coeff(self):
        return self.__coeff

    @coeff.setter
    def coeff(self, coeff: Tuple[float]):
        self.__coeff = coeff

    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param):
        self.__param = param

    @property
    def b_i(self):
        return self.__b_i

    @b_i.setter
    def b_i(self, b_i):
        self.__b_i = b_i

    def append(self, pair: tuple):
        # helper to add a single pair (x, xcoeff)
        assert len(pair) == 2, 'append function for relation class requires a pair of param and coeff in tuple form, ' \
                               'like (x,1) '
        print('WARNING: This function is deprecated because it is dangerous when there are greater-equal inequalities '
              'involved.')
        self.param.append(pair[0])
        self.coeff.append(pair[1])

    def lookup_coeff(self, lookup_param: str):
        assert lookup_param in self.param, 'this parameter is not in the parameter list of this relation'
        idx = self.param.index(lookup_param)
        return self.coeff[idx]

    def sat(self, values: Dict):
        assert set(self.param) == set(values.keys())
        lhs = 0
        # sorted_values = values.sort(key=lambda parameter: values.keys.find(parameter))
        for i, parameter in enumerate(self.param):
            lhs += values[parameter] * self.coeff[i]
            # adds up everything on the left hand side

        return lhs <= self.b_i


if __name__ == '__main__':
    testcoeff = [1, 3., 5]
    testparam = ['a', 'b', 'c']
    b_i = 3
    is_lowerequal = True

    testrel = RelationObject(testcoeff, testparam, b_i, is_lowerequal)
    #
    # print(testrel)
    #
    # addition = ('d',5.7)
    #
    # testrel.append(addition)
    #
    # print(testrel)

    print(testrel.sat({'c': 1 / 5, 'a': 2, 'b': 0}))

    print(testrel)
    testrel.eliminate_variable('c', 12)
    print(testrel)
