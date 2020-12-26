import unittest

from src.day25.main import part_one, get_loop_size


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(8, get_loop_size(5764801))
        self.assertEqual(11, get_loop_size(17807724))
        self.assertEqual(14897079, part_one('test1.txt'))

if __name__ == '__main__':
    unittest.main()