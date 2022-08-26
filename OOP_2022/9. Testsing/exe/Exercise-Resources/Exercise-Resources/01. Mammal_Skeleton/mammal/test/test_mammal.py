import unittest
from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    name = "Test"
    mammal_type = "Type_test"
    sound = "test_sound"
    kingdom = "animals"

    def setUp(self) -> None:
        self.test_mammal = Mammal(self.name, self.mammal_type, self.sound)


    def test_mammal_init(self):

        self.assertEqual("Test", self.test_mammal.name)
        self.assertEqual("Type_test", self.test_mammal.type)
        self.assertEqual("test_sound", self.test_mammal.sound)
        self.assertEqual("animals", self.test_mammal._Mammal__kingdom)


    def test_make_sound(self):

        actual_result = self.test_mammal.make_sound()
        expected_result = f"{self.name} makes {self.sound}"
        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom(self):

        actual_result = self.test_mammal.get_kingdom()
        expected_result = self.kingdom
        self.assertEqual(expected_result, actual_result)

    def test_info(self):

        actual_result = self.test_mammal.info()
        expected_result = f"{self.name} is of type {self.mammal_type}"
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
