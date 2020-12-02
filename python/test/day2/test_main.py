import unittest

from src.day2.main import part_one, part_two


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(622, part_one('input.txt'))

    def test_part_two(self):
        self.assertEqual(263, part_two('input.txt'))


if __name__ == '__main__':
    unittest.main()
