import unittest

from src.day22.main import part_one, part_two


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(306, part_one('test1.txt'))
        self.assertEqual(32448, part_one('input.txt'))

    def test_part_two(self):
        self.assertEqual(291, part_two('test1.txt'))
        self.assertEqual(32949, part_two('input.txt'))


if __name__ == '__main__':
    unittest.main()
