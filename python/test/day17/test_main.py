import unittest

from src.day17.main import part_one, part_two, Board

from src.common.file_utils import get_path, read_lines


class TestDay01(unittest.TestCase):
    def test_board(self):
        board = Board([".#.", "..#", "###"])
        board.print()
        self.assertEqual(5, board.count_neighbours((1, 1, 0)))
        self.assertEqual(1, board.count_neighbours((0, 0, 0)))
        self.assertEqual(2, board.count_neighbours((2, 2, 0)))
        board.cycle()
        self.assertEqual(11, board.count_alive())

    def test_part_one(self):
        self.assertEqual(112, part_one('test1.txt'))
        self.assertEqual(255, part_one('input.txt'))

    def test_part_two(self):
        self.assertEqual(848, part_two('test1.txt'))
        self.assertEqual(2340, part_two('input.txt'))


if __name__ == '__main__':
    unittest.main()
