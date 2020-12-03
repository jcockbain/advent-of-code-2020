import unittest

from src.day3.main import part_one, part_two


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(289, part_one('input.txt'))

    def test_part_two(self):
        self.assertEqual(5522401584, part_two('input.txt'))


if __name__ == '__main__':
    unittest.main()
