import unittest

from src.day12.main import part_one, part_two


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(25, part_one('test1.txt'))
        self.assertEqual(2297, part_one('input.txt'))

    def test_part_two(self):
        self.assertEqual(286, part_two('test1.txt'))
        self.assertEqual(89984, part_two('input.txt'))


if __name__ == '__main__':
    unittest.main()
