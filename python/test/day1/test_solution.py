import unittest

from src.day1.solution import part_one, part_two


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(440979, part_one('input.txt'))

    def test_part_two(self):
        self.assertEqual(82498112, part_two('input.txt'))


if __name__ == '__main__':
    unittest.main()
