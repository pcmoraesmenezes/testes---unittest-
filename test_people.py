import unittest
from unittest.mock import patch
from people import People


class TestPeople(unittest.TestCase):
    def setUp(self):
        self.people = People('Paulo', 'César')

    def test_people_attr_name_have_correct_value(self):
        self.assertEqual(self.people.name, 'Paulo')

    def test_people_attr_name_is_string(self):
        self.assertIsInstance(self.people.name, str)

    def test_people_attr_last_name_have_correct_value(self):
        self.assertEqual(self.people.last_name, 'César')

    def test_people_attr_last_name_is_string(self):
        self.assertIsInstance(self.people.last_name, str)

    def test_people_attr_data_obtained_start_false(self):
        self.assertFalse(self.people.data_obtained)

    def test_obtain_all_data_with_sucess_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.people.obtain_all_data(), 'Connected')

    def test_obtain_all_data_failed(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.people.obtain_all_data(), 'Error 404')


if __name__ == "__main__":
    unittest.main(verbosity=2)
