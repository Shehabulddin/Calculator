
import unittest
from calculator import calc

class TestCalculator(unittest.TestCase):

    def test_string_returns_zero(self):
        # Given
        input_string = ""
        expected_result = 0

        # When
        result = calc(input_string)

        # Then
        self.assertEqual(result, expected_result)


    def test_single_number_returns_value(self):
        # Given
        input_string = "5"
        expected_result = 5

        # When
        result = calc(input_string)

        # Then
        self.assertEqual(result, expected_result)

    def test_two_numbers_comma_return_sum(self):
        # Given
        input_string = "1,2"
        expected_result = 3

        # When
        result = calc(input_string)

        # Then
        self.assertEqual(result, expected_result)
    def test_two_newline_return_sum(self):
        # Given
        input_string = "1\n2"
        expected_result = 3

        # When
        result = calc(input_string)

        # Then
        self.assertEqual(result, expected_result)

    def test_three_numbers_delimited_either_way_returns_sum(self):
        # Given
        input_string = "1,2\n3"
        expected_result = 6

        # When
        result = calc(input_string)

        # Then
        self.assertEqual(result, expected_result)

    def test_negative_numbers_throw_exception(self):
        # Given
        input_string = "1,-2,3"

        # When & Then (Expecting an Exception)
        with self.assertRaises(ValueError) as context:
            calc(input_string)

        # Ensure the exception message contains the negative number
        self.assertIn("Negatives not allowed: -2", str(context.exception))
    def test_number_greater_than_1000_ignored(self):
        #Given
        input_string = "1,2,1000"
        expected_result = 3

        #When
        result = calc(input_string)

        #then
        self.assertEqual(result, expected_result)

    def test_single_char_delimiter_defined_first_line(self):
        #Given
        input_string = "//#\n1#2#1000"
        expected_result = 3

        #When
        result = calc(input_string)

        #then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()

