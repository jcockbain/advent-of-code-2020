import unittest

from src.day16.main import part_one, part_two


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(71, part_one('test1.txt'))
        self.assertEqual(20091, part_one('input.txt'))

    def test_part_two(self):
        self.assertEqual(2325343130651, part_two('input.txt'))


if __name__ == '__main__':
    unittest.main()
