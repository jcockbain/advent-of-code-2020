import unittest

from src.day4.main import part_two, check_byr, check_iyr, check_eyr, check_hgt, check_hcl, check_ecl, check_pid


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(0, part_two('test_input_1.txt'))

    def test_part_two(self):
        self.assertEqual(4, part_two('test_input_2.txt'))

    def test_byr(self):
        tests_true = [
            "2002",
            "2000",
            "1990",
        ]
        for v in tests_true:
            self.assertTrue(check_byr(v))

        tests_false = [
            "2003",
            "1919",
            "123",
            "12"
        ]
        for v in tests_false:
            self.assertFalse(check_byr(v))
   
    def test_iry(self):
        tests_true = [
            "2015",
            "2020",
            "2010",
        ]
        for v in tests_true:
            self.assertTrue(check_iyr(v))

        tests_false = [
            "2003",
            "2009",
        ]
        for v in tests_false:
            self.assertFalse(check_iyr(v))
    
    def test_eyr(self):
        tests_true = [
            "2020",
            "2030",
            "2022",
        ]
        for v in tests_true:
            self.assertTrue(check_eyr(v))

        tests_false = [
            "2003",
            "2032",
            "2019",
        ]
        for v in tests_false:
            self.assertFalse(check_eyr(v))
   
    def test_hgt(self):
        tests_true = [
            "60in",
            "190cm"
        ]
        tests_false = [
            "190in",
            "190",
            "123abc",
            "123abg",
            "123abce",
        ]
        for test in tests_true:
            self.assertTrue(check_hgt(test))
        
        for test in tests_false:
            self.assertFalse(check_hgt(test))

    def test_ecl(self):
        tests_true = [
            "amb",
            "blu",
            "brn",
            "gry",
            "grn",
            "hzl",
            "oth",
        ]
        tests_false = [
            "#asd",
            "asx",
            "sss",
        ]
        for test in tests_true:
            self.assertTrue(check_ecl(test))
        
        for test in tests_false:
            self.assertFalse(check_ecl(test))
    
    def test_hcl(self):
        tests_true = [
            "#123abc",
            "#123abe",
        ]
        tests_false = [
            "123abz",
        ]
        for test in tests_true:
            self.assertTrue(check_hcl(test))
        
        for test in tests_false:
            self.assertFalse(check_hcl(test))

    def test_pid(self):
        tests_true = [
            "000000001",
            "001234567"
        ]
        tests_false = [
            "1234567891",
        ]
        for test in tests_true:
            self.assertTrue(check_pid(test))
        
        for test in tests_false:
            self.assertFalse(check_pid(test))


if __name__ == '__main__':
    unittest.main()
