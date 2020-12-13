import unittest

from src.day13.main import part_one, part_two


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(295, part_one('test1.txt'))

    def test_part_two(self):
        self.assertEqual(1068781, part_two('test1.txt'))
        self.assertEqual(3417, part_two('test2.txt'))
        self.assertEqual(754018, part_two('test3.txt'))
        self.assertEqual(779210, part_two('test4.txt'))
        self.assertEqual(1261476, part_two('test5.txt'))
        self.assertEqual(626670513163231, part_two('input.txt'))


if __name__ == '__main__':
    unittest.main()
