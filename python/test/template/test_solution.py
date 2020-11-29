import unittest

from src.common.file_utils import get_path
from src.template.solution import part_one, part_two


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(15, part_one(get_path(__file__, 'input.txt')))

    def test_part_two(self):
        self.assertEqual(5, part_two(get_path(__file__, 'input.txt')))


if __name__ == '__main__':
    unittest.main()
