import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest

from plugin_example import CalculatorPlugin

class TestCalculatorPlugin(unittest.TestCase):
    def test_addition(self):
        plugin = CalculatorPlugin()
        result = plugin.execute({'a': 5, 'b': 3})
        self.assertEqual(result, {'result': 8})
