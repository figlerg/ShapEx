from .letter_type import LetterType

class Letter:
    def get_type(self):
        return LetterType.UNDEFINED


    def __str__(self):
        return 'unknown'

    def shallow_assert_equal(self, letter:LetterType):

        return self.get_type() == letter.get_type()
        # self.assertEqual(letter.slope, self.start_end.letter.slope), "Should just consist of one repeated letter"
        # self.assertEqual(letter.offset, self.start_end.letter.offset), "Should just consist of one repeated letter"
        # self.assertEqual(letter.length, self.start_end.letter.length), "Should just consist of one repeated letter"

    def __eq__(self, other):
        other:Letter
        return tuple(self.__dict__.values()) == tuple(other.__dict__.values())
        # apparently, the docs say that tuples should be used since they are immutable. This makes a tuple of all the
        # values (strings) assigned to each attribute.
        # checks whether all self values are the same. method name __eq__ overrides "==" operator

    # the problem with defining __eq__ is that it is now unhashable, so it breaks other parts in the code.
    # Not sure if this is safe, but it works:
    def __hash__(self):
        return hash(self.__dict__.values())