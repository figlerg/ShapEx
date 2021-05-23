import unittest

from word_sampler.sapathfinder.find_paths import find_paths
from parse.se2sa.automaton.automaton import ShapeAutomaton
from parse.se2sa.automaton.location import Location
from parse.se2sa.automaton.transition import Transition
from alphabet import LineLetter
from alphabet.exp_letter import ExpLetter
from alphabet.exp_letter import Letter
from parse.se2sa import kleene_to_aut
from parse.se2sa import concat_to_aut


class KleeneStarSearchTest(unittest.TestCase):
    def setUp(self):
        self.n = 5
        self.aut = ShapeAutomaton()
        self.letter = LineLetter(slope='a', offset='b',length='l')

        self.start_loc = Location('start', is_final=False, is_initial=True)
        self.end_loc = Location('end', is_final=True, is_initial=False)

        self.start_end = Transition('edge1', self.start_loc, self.end_loc, self.letter)

        self.aut.add_location(self.start_loc)
        self.aut.add_location(self.end_loc)

        self.aut.add_transition(self.start_end)

        self.aut = kleene_to_aut(self.aut)
        # print(self.aut)


    def tearDown(self):
        pass

    def test_just_kleene_star(self):
        # n = 5
        n = self.n
        paths = find_paths(aut=self.aut, n=n)

        self.assertEqual(len(paths), n), "Should reach n"
        for path in paths:
            for letter in path:
                # print(letter)
                self.shallow_assert_equal(letter)

    def test_more_complicated_automaton(self):
        n = self.n

        aut_2 = ShapeAutomaton()

        # add a new way to our automaton
        aut_tmp = ShapeAutomaton()
        new_start = Location('new_start', is_final=False, is_initial=True)
        new_end = Location('new_end', is_final=True, is_initial=False)
        aut_tmp.add_location(new_start)
        aut_tmp.add_location(new_end)

        letter = ExpLetter(a='a_2', b='b_2', c='c_2', length='l_2')

        edge = Transition('edge', new_start, new_end, letter)
        aut_tmp.add_transition(edge)



        # for i in [1,2,3]:
        #     aut_tmp = ShapeAutomaton() # was aut2 originally
        #     new_start = Location('new_start_'+str(i), is_final=False, is_initial=True)
        #     new_end = Location('new_end'+ str(i), is_final=True, is_initial=False)
        #     aut_tmp.add_location(new_start)
        #     aut_tmp.add_location(new_end)
        #
        #     letter = ExpLetter(a='a'+str(i),b='b'+str(i),c='c'+str(i),length='l'+str(i))
        #
        #     edge = Transition('edge'+str(i), new_start, new_end, letter)
        #     aut_tmp.add_transition(edge)
        #
        #     if i == 1:
        #         aut_tmp.add_location(self.start_loc)
        #         aut_tmp.add_transition(Transition('connex_start', self.start_loc,self.start))



        # aut2.add_location(self.end_loc)
        aut = concat_to_aut(self.aut, aut_tmp)
        # print('\n')
        # print(aut)

        paths = find_paths(aut, n)

        l = self.start_end.letter # just for brevity, l for line e for exp
        e = edge.letter

        # TODO this is not the only criterion! The paths returned should be the shortest!
        for path in paths:
            for letter in path[0:-1]:
                shallow_assert_equality_2_letters(letter, l)
            shallow_assert_equality_2_letters(path[-1], e)














    def shallow_assert_equal(self, letter):
        self.assertEqual(letter.slope, self.start_end.letter.slope), "Should just consist of one repeated letter"
        self.assertEqual(letter.offset, self.start_end.letter.offset), "Should just consist of one repeated letter"
        self.assertEqual(letter.length, self.start_end.letter.length), "Should just consist of one repeated letter"

# move this to class members maybe
def shallow_assert_equality_2_letters(letter1:Letter, letter2:Letter):
    assert letter1.get_type() == letter2.get_type(), 'not even the same letter type'

    if letter1.get_type() == 'line':

        assert letter1.slope == letter2.slope, 'these letters should be the same'
        assert letter1.offset == letter2.offset, 'these letters should be the same'
        assert letter1.length == letter2.length, 'these letters should be the same'
    elif letter1.get_type() == 'exponential':
        assert letter1.a == letter2.a, 'these letters should be the same'
        assert letter1.b == letter2.b, 'these letters should be the same'
        assert letter1.c == letter2.c, 'these letters should be the same'
        assert letter1.length == letter2.length, 'these letters should be the same'


if __name__ == '__main__':
    unittest.main()
