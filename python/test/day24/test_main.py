import unittest

from src.day24.main import part_one, part_two, process_line


class TestDay01(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(10, part_one('test1.txt'))
        self.assertEqual(228, part_one('input.txt'))

    def test_part_two(self):
        self.assertEqual(2208, part_two('test1.txt'))
        self.assertEqual(3672, part_two('input.txt'))


if __name__ == '__main__':
    unittest.main()
