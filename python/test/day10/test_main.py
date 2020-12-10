import unittest

from src.day10.main import part_one, part_two


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(35, part_one('test1.txt'))
        self.assertEqual(220, part_one('test2.txt'))
        self.assertEqual(1856, part_one('input.txt'))

    def test_part_two(self):
        self.assertEqual(8, part_two('test1.txt'))
        self.assertEqual(19208, part_two('test2.txt'))
        self.assertEqual(2314037239808, part_two('input.txt'))


if __name__ == '__main__':
    unittest.main()
