import unittest

from src.day19.main import part_one, part_two, Solver, path


class TestDay01(unittest.TestCase):

    def test_solver(self):
        s = Solver(path('test1.txt'))

        self.assertEqual({0: (1, ['4 1 5']), 1: (1, ['2 3', '3 2']), 2: (
            1, ['4 4', '5 5']), 3: (1, ['4 5', '5 4']), 4: (0, ['a']), 5: (0, ['b'])}, s.rules)

        self.assertEqual(["a"], s.get_possible_messages(4))
        self.assertEqual(["b"], s.get_possible_messages(5))
        self.assertEqual(["ab", "ba"], s.get_possible_messages(3))
        self.assertEqual(["aa", "bb"], s.get_possible_messages(2))
        expected = [
            "aaab",
            "aaba",
            "bbab",
            "bbba",
            "abaa",
            "abbb",
            "baaa",
            "babb",
        ]
        self.assertEqual(expected, s.get_possible_messages(1))

    def test_part_one(self):
        self.assertEqual(2, part_one('test1.txt'))
        self.assertEqual(3, part_one('test2.txt'))
        self.assertEqual(187, part_one('input.txt'))

    def test_part_two(self):
        self.assertEqual(12, part_two('test2.txt'))
        self.assertEqual(392, part_two('input.txt'))


if __name__ == '__main__':
    unittest.main()
