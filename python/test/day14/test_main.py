import unittest

from src.day14.main import part_one, part_two


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(165, part_one('test1.txt'))
        self.assertEqual(9628746976360, part_one('input.txt'))

    def test_part_two(self):
        self.assertEqual(208, part_two('test2.txt'))
        self.assertEqual(4574598714592, part_two('input.txt'))


if __name__ == '__main__':
    unittest.main()
