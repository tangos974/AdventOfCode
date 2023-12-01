import unittest
from day1ex2 import find_first_digit
from day1ex2 import find_last_digit
from day1ex2 import find_first_and_last_digit
from day1ex2 import get_sum_of_first_and_last_digits


class TestFindFirstDigit(unittest.TestCase):
    def test_find_first_digit_digit(self):
        line = "There is a 5 in the text."
        result = find_first_digit(line)
        self.assertEqual(result, '5')

    def test_find_first_digit_several_digits(self):
        line = "There is a 5, a 7 and a 1 in the text."
        result = find_first_digit(line)
        self.assertEqual(result, '5')

    def test_find_first_digit_spelled_digit(self):
        line = "There is a seven in the text."
        result = find_first_digit(line)
        self.assertEqual(result, '7')

    def test_find_first_digit_no_digit(self):
        line = "There are no digits in the text."
        result = find_first_digit(line)
        self.assertEqual(result, '')

    def test_find_first_digit_empty_line(self):
        line = ""
        result = find_first_digit(line)
        self.assertEqual(result, '')

    def test_find_first_digit_digit_and_spelled(self):
        line = "There is a 5, a 6 and a seven in the text."
        result = find_first_digit(line)
        self.assertEqual(result, '5')

    def test_find_first_digit_spelled_and_digit(self):
        line = "There is a five, a seven and a 5 in the text."
        result = find_first_digit(line)
        self.assertEqual(result, '5')

    def test_find_first_digit_sentence_starts_with_spelled(self):
        line = "two1nine"
        result = find_first_digit(line)
        self.assertEqual(result, '2')


class TestFindLastDigit(unittest.TestCase):
    def test_find_last_digit_digit(self):
        line = "There is a 5 in the text."
        result = find_last_digit(line)
        self.assertEqual(result, '5')

    def test_find_last_digit_several_digits(self):
        line = "There is a 5, a 7 and a 1 in the text."
        result = find_last_digit(line)
        self.assertEqual(result, '1')

    def test_find_last_digit_spelled_digit(self):
        line = "There is a seven in the text."
        result = find_last_digit(line)
        self.assertEqual(result, '7')

    def test_find_last_digit_no_digit(self):
        line = "There are no digits in the text."
        result = find_last_digit(line)
        self.assertEqual(result, '')

    def test_find_last_digit_empty_line(self):
        line = ""
        result = find_last_digit(line)
        self.assertEqual(result, '')


class TestFindFirstAndLastDigit(unittest.TestCase):
    def test_find_first_and_last_digit(self):
        line = "There is a 5 in the text."
        result = find_first_and_last_digit(line)
        self.assertEqual(result, '55')

    def test_find_first_and_last_digit_several_numerical_digits(self):
        line = "There is a 5, a 7 and a 1 in the text."
        result = find_first_and_last_digit(line)
        self.assertEqual(result, '51')

    def test_find_first_and_last_digit_spelled_digit(self):
        line = "There is a seven in the text."
        result = find_first_and_last_digit(line)
        self.assertEqual(result, '77')

    def test_find_first_and_last_digit_no_digit(self):
        line = "There are no digits in the text."
        result = find_first_and_last_digit(line)
        self.assertEqual(result, '')

    def test_find_first_and_last_digit_empty_line(self):
        line = ""
        result = find_first_and_last_digit(line)
        self.assertEqual(result, '')

    def test_find_first_and_last_digit_digit_and_spelled(self):
        line = "There is a 5, a 6 and a seven in the text."
        result = find_first_and_last_digit(line)
        self.assertEqual(result, '57')

    def test_find_first_and_last_digit_spelled_and_digit(self):
        line = "There is a five, a seven and a 5 in the text."
        result = find_first_and_last_digit(line)
        self.assertEqual(result, '55')

    def test_find_first_and_last_digit_spelled_digits_overlapping(self):
        line = "eightwothreeighthreeightwoo"
        result = find_first_and_last_digit(line)
        self.assertEqual(result, '82')


class TestGetSumOfFirstAndLastDigits(unittest.TestCase):
    def test_single_line(self):
        text = "123"
        expected_sum = 13
        self.assertEqual(get_sum_of_first_and_last_digits(text), expected_sum)

    def test_given_sample(self):
        text = """two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen"""
        expected_sum = 281
        self.assertEqual(get_sum_of_first_and_last_digits(text), expected_sum)


if __name__ == '__main__':
    unittest.main(verbosity=2)
    unittest.main()
