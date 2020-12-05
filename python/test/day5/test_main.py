import unittest

from src.day5.main import part_one, part_two, get_seat_id


class TestDay01(unittest.TestCase):
    def test_get_seat_id(self):
        self.assertEqual(357, get_seat_id("FBFBBFFRLR"))
        self.assertEqual(567, get_seat_id("BFFFBBFRRR"))
        self.assertEqual(820, get_seat_id("BBFFBBFRLL"))
    
    def test_part_one(self):
        self.assertEqual(822, part_one('input.txt'))

    def test_part_two(self):
        self.assertEqual(503, part_two('input.txt'))



if __name__ == '__main__':
    unittest.main()
