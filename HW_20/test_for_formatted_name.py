import unittest
from formatted_name import formatted_name

class TestFormattedName(unittest.TestCase):
    def test_first_last_name(self):
        results = formatted_name(first_name='Admin', last_name='AdminLastName')
        self.assertEqual(results, ('Admin Adminlastname'))

    def test_first_last_middle_name(self):
        results = formatted_name(first_name='Admin', last_name='AdminLastName', middle_name='AdminName')
        self.assertEqual(results, ('Admin Adminname Adminlastname'))

    def test_empty_middle_name(self):
        results = formatted_name(first_name='Admin', last_name='Adminlastname', middle_name='')
        self.assertEqual(results, ('Admin Adminlastname'))

