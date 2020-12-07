import unittest

from src.day7.main import part_one, part_two


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(4, part_one('test_1.txt'))
        self.assertEqual(370, part_one('input.txt'))

    def test_part_two(self):
        self.assertEqual(32, part_two('test_1.txt'))
        self.assertEqual(126, part_two('test_2.txt'))
        self.assertEqual(29547, part_two('input.txt'))


if __name__ == '__main__':
    unittest.main()
