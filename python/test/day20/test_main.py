import unittest

from src.day20.main import part_one, part_two, Tile, parse_input, path


class TestDay01(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(20899048083289, part_one('test1.txt'))
        # self.assertEqual(12519494280967, part_one('input.txt'))

    # def test_part_two(self):
    #     self.assertEqual(5, part_two('input.txt'))


if __name__ == '__main__':
    unittest.main()
