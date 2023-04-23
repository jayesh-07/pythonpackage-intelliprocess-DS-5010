import pandas as pd
import numpy as np
import unittest
from Handling_missing_values import fill_missing_values

class TestHandlingMissingValues(unittest.TestCase):
	def test_fill_missing_values_numeric(self):
		df = pd.DataFrame({'A': [3, 2, np.nan, 4], 'B': [1.0, np.nan, 1.0, 1.0]})
		expected_output = pd.DataFrame({'A': [3, 2, 3.0, 4], 'B': [1.0, 1.0, 1.0, 1.0]})
		self.assertTrue(fill_missing_values(df).equals(expected_output))

	def test_fill_missing_values_boolean(self):
		df = pd.DataFrame({'A': [True, True, np.nan], 'B': [np.nan, False, False]})
		expected_output = pd.DataFrame({'A': [True, True, True], 'B': [False, False, False]})
		self.assertTrue(fill_missing_values(df).equals(expected_output))

	def test_fill_missing_values_categorical(self):
		df = pd.DataFrame({'A': ['red', 'blue', 'green', np.nan], 'B': ['large', 'small', 'medium', 'small']})
		expected_output = pd.DataFrame({'A': ['red', 'blue', 'green', 'red'], 'B': ['large', 'small', 'medium', 'small']})
		self.assertTrue(fill_missing_values(df).equals(expected_output))

	def test_fill_missing_values_string(self):
		df = pd.DataFrame({'A': ['apple', 'banana', np.nan, 'apple'], 'B': ['John', 'John', 'Sam', np.nan]})
		expected_output = pd.DataFrame({'A': ['apple', 'banana', 'apple', 'apple'], 'B': ['John', 'John', 'Sam', 'John']})
		self.assertTrue(fill_missing_values(df).equals(expected_output))

if __name__ == '__main__':
    unittest.main()