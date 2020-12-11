import unittest

from src.day11.main import part_one, part_two


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(37, part_one('test1.txt'))
        self.assertEqual(2270, part_one('input.txt'))

    def test_part_two(self):
        self.assertEqual(26, part_two('test1.txt'))
        self.assertEqual(2042, part_two('input.txt'))


if __name__ == '__main__':
    unittest.main()
