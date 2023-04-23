import unittest
import pandas as pd
from basicop import datatype_frequency, feature_type_frequency, nan_frequency

class TestBasicOp(unittest.TestCase):

    def test_datatype_frequency(self):
        data = {'A': [1, 2, 3], 'B': [4.5, 6.7, 8.9], 'C': ['foo', 'bar', 'baz'], 'D': pd.date_range('20220101', periods=3)}
        df = pd.DataFrame(data)
        result = datatype_frequency(df)
        self.assertEqual(result, [['int64', 1], ['float64', 1], ['object', 1], ['datetime64[ns]', 1]])

    def test_feature_type_frequency(self):
        data = {'A': [1, 2, 3], 'B': [4.5, 6.7, 8.9], 'C': ['foo', 'bar', 'baz'], 'D': pd.date_range('20220101', periods=3)}
        df = pd.DataFrame(data)
        result = feature_type_frequency(df)
        self.assertEqual(result, [['Categorical', 1], ['Numerical', 2]])

    def test_nan_frequency_with_NaN_values(self):
        data = {'A': [1, 2, None], 'B': [4.5, None, 8.9], 'C': ['foo', 'bar', 'baz'], 'D': pd.date_range('20220101', periods=3)}
        df = pd.DataFrame(data)
        result = nan_frequency(df)
        self.assertEqual(result, [['A', 1], ['B', 1], ['C', 0], ['D', 0]])

    def test_nan_frequency_without_NaN_values(self):
        data = {'A': [1, 2, 3], 'B': [4.5, 6.7, 8.9], 'C': ['foo', 'bar', 'baz'], 'D': pd.date_range('20220101', periods=3)}
        df = pd.DataFrame(data)
        result = nan_frequency(df)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()

