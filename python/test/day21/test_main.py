import unittest

from src.day21.main import part_one, part_two


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(5, part_one('test1.txt'))
        self.assertEqual(2061, part_one('input.txt'))

    def test_part_two(self):
        self.assertEqual("mxmxvkd,sqjhc,fvjkl", part_two('test1.txt'))
        self.assertEqual(
            "cdqvp,dglm,zhqjs,rbpg,xvtrfz,tgmzqjz,mfqgx,rffqhl", part_two('input.txt'))


if __name__ == '__main__':
    unittest.main()
