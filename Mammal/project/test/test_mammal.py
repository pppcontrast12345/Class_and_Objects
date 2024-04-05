from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = (
            Mammal("Mike",
                   "elephant",
                   "some sound",
                   )
        )

    def test_correct_init(self):
        self.assertEqual("Mike", self.mammal.name)
        self.assertEqual("elephant", self.mammal.type)
        self.assertEqual("some sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_correct_string(self):
        self.assertEqual("Mike makes some sound", self.mammal.make_sound())

    def test_get_kingdom_correct_string(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_correct_string(self):
        self.assertEqual("Mike is of type elephant", self.mammal.info())

if __name__ == "__main__":
    main()