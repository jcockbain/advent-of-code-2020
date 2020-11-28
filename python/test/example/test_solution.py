import unittest

from src.common.file_utils import get_path
from src.example.solution import part_one

class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual([1, 2, 3, 4, 5], part_one(get_path(__file__, 'input.txt')))


if __name__ == '__main__':
    unittest.main()