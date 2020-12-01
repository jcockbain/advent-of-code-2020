import unittest

from src.template.main import part_one, part_two


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(15, part_one('input.txt'))

    def test_part_two(self):
        self.assertEqual(5, part_two('input.txt'))


if __name__ == '__main__':
    unittest.main()
