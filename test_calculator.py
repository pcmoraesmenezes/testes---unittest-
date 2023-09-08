import unittest
from calculator import sum, minus


class CalculatorSumTest(unittest.TestCase):
    def test_sum_5_and_5_must_return_10(self):
        self.assertEqual(sum(5, 5), 10)

    def test_sum_negative_5_and_5_must_return_0(self):
        self.assertEqual(sum(-5, 5), 0)

    def test_multiple_entry(self):
        x_y_outputs = (
            (10, 20, 30),
            (1.5, 2.5, 4.0),
            (1.3, 2.8, 4.1),
            (-5, -5, -10),
            (0, 0, 0),
        )

        for x_y_output in x_y_outputs:
            with self.subTest(x_y_output=x_y_output):
                x, y, output = x_y_output
                self.assertEqual(sum(x, y), output)

    def test_sum_x_not_int_or_float_must_return_assertion_error(self):
        with self.assertRaises(AssertionError):
            sum('a', 0)

    def test_sum_y_not_int_or_float_must_return_assertion_error(self):
        with self.assertRaises(AssertionError):
            sum(0, 'b')


class CalculatorMinusTest(unittest.TestCase):
    def test_5_minus_5_must_return_0(self):
        self.assertAlmostEqual(minus(5, 5), 0)

    def test_negative_five_minus_five_must_return_10(self):
        self.assertAlmostEqual(minus(-5, 5), -10)

    def test_multiple_entry(self):
        x_y_outputs = (
            (10, 20, -10),
            (-7.5, 2.5, -10),
            (0, 0, 0),
            (-5, -5, 0),
        )

        for x_y_output in x_y_outputs:
            with self.subTest(x_y_output=x_y_output):
                x, y, output = x_y_output
                self.assertEqual(minus(x, y), output)

    def test_minus_x_not_int_or_float_must_return_assertion_error(self):
        with self.assertRaises(AssertionError):
            minus('a', 0)

    def test_minus_y_not_int_or_float_must_return_assertion_error(self):
        with self.assertRaises(AssertionError):
            minus(1, 'b')


unittest.main(verbosity=2)
