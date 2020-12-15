import unittest

from src.day15.main import part_one, part_two


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(436, part_one([0, 3, 6]))

    # def test_part_two(self):
    #     self.assertEqual(175594, part_two([0, 3, 6]))
    #     self.assertEqual(955, part_two([7, 14, 0, 17, 11, 1, 2]))


if __name__ == '__main__':
    unittest.main()
