import unittest
from convert_data import *

class ConvertDataTestCase(unittest.TestCase):

    def test_convert_large(self):
        expected_value = 2340000000
        assert convert_large('2.34B') == expected_value

    def test_convert_small(self):
        expected_value = 2.34
        assert convert_small('2.34') == expected_value    

    def test_convert_percentages(self):
        expected_value = -23.4
        assert convert_percentages('-23.4%') == expected_value

    def test_convert(self):
        expected_value = 2340000
        assert convert('2.34M') == expected_value

unittest.main(argv=[''], verbosity=2, exit=False)