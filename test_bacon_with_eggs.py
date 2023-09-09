"""
TDD - Test Driven Development
Step 1 -> Create a test and check it fail (Red)
Step 2 -> Create a code and see test pass (Green)
Step 3 -> Upgrade code (Refactor)
"""
from bacon_with_eggs import bacon_with_eggs
import unittest


class TestBaconWithEggs(unittest.TestCase):
    def test_bacon_with_eggs_must_raise_assertion_error_if_not_recieve_int(self):  # noqa
        with self.assertRaises(AssertionError):
            bacon_with_eggs('')

    def test_bacon_with_eggs_must_return_bacon_with_eggs_if_entry_is_multiple_3_and_5(self):  # noqa
        entrys = (15, 30, 45, 60)
        output = 'Bacon with eggs'

        for entry in entrys:
            with self.subTest(entry=entry, output=output):
                self.assertEqual(bacon_with_eggs(entry), output)

    def test_bacon_with_eggs_must_return_hungry_if_is_not_multiple_3_and_5(self):  # noqa
        entrys = (1, 2, 4, 11, 7, 8)
        output = 'Hungry'

        for entry in entrys:
            with self.subTest(entry=entry, output=output):
                self.assertEqual(bacon_with_eggs(entry), output)

    def test_bacon_with_eggs_must_return_bacon_if_is_multiple_3(self):  # noqa
        entrys = (3, 6, 9, 12, 18, 21)
        output = 'Bacon'

        for entry in entrys:
            with self.subTest(entry=entry, output=output):
                self.assertEqual(bacon_with_eggs(entry), output)

    def test_bacon_with_eggs_must_return_eggs_if_is_multiple_5(self):  # noqa
        entrys = (5, 10, 20, 25, 35, 40)
        output = 'Eggs'

        for entry in entrys:
            with self.subTest(entry=entry, output=output):
                self.assertEqual(bacon_with_eggs(entry), output)


unittest.main(verbosity=2)
