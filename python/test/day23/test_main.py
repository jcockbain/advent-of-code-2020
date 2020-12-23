import unittest

from src.day23.main import part_one, part_two, calc_one, calc_two, move


class TestDay01(unittest.TestCase):
    # def test_move(self):
    #     self.assertEqual([3, 2, 8, 9, 1, 5, 4, 6, 7],
    #                      move([3, 8, 9, 1, 2, 5, 4, 6, 7], 0, 9, 1)[0])

    def test_part_one(self):
        self.assertEqual("92658374", calc_one("389125467", 10))
        self.assertEqual("27956483", part_one("input.txt"))

    def test_part_two(self):
        self.assertEqual(149245887792, calc_two('389125467', 10000000))


if __name__ == '__main__':
    unittest.main()
