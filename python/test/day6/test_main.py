import unittest

from src.day6.main import part_one, part_two


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(11, part_one('test_1.txt'))
        self.assertEqual(6273, part_one('input.txt'))

    def test_part_two(self):
        self.assertEqual(6, part_two('test_1.txt'))
        self.assertEqual(15, part_two('test_2.txt'))
        self.assertEqual(3254, part_two('input.txt'))


if __name__ == '__main__':
    unittest.main()
