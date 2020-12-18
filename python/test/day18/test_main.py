import unittest

from src.day18.main import part_one, part_two, evaluate, evaluate_exp1,  evaluate_exp2


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(71, evaluate("1 + 2 * 3 + 4 * 5 + 6", evaluate_exp1))
        self.assertEqual(26, evaluate("2 * 3 + (4 * 5)", evaluate_exp1))
        self.assertEqual(51, evaluate(
            "1 + (2 * 3) + (4 * (5 + 6))", evaluate_exp1))
        self.assertEqual(437, evaluate(
            "5 + (8 * 3 + 9 + 3 * 4 * 3)", evaluate_exp1))
        self.assertEqual(12240, evaluate(
            "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", evaluate_exp1))
        self.assertEqual(13632, evaluate(
            "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", evaluate_exp1))
        self.assertEqual(4491283311856, part_one('input.txt'))

    def test_part_two(self):
        self.assertEqual(231, evaluate(
            "1 + 2 * 3 + 4 * 5 + 6", evaluate_exp2))
        self.assertEqual(51, evaluate(
            "1 + (2 * 3) + (4 * (5 + 6))", evaluate_exp2))
        self.assertEqual(1445, evaluate(
            "5 + (8 * 3 + 9 + 3 * 4 * 3)", evaluate_exp2))
        self.assertEqual(669060, evaluate(
            "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", evaluate_exp2))
        self.assertEqual(23340, evaluate(
            "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", evaluate_exp2))


if __name__ == '__main__':
    unittest.main()
