import unittest

from src.day9.main import part_one, part_two


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(127, part_one('test1.txt', 5))
        self.assertEqual(57195069, part_one('input.txt', 25))

    def test_part_two(self):
        self.assertEqual(62, part_two('test1.txt', 5))
        self.assertEqual(7409241, part_two('input.txt', 25))


if __name__ == '__main__':
    unittest.main()
