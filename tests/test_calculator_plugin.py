import unittest

from amrikyyai import CalculatorPlugin

class TestCalculatorPlugin(unittest.TestCase):
    def test_addition(self):
        plugin = CalculatorPlugin()
        result = plugin.execute({'a': 5, 'b': 3})
        self.assertEqual(result, {'result': 8})

