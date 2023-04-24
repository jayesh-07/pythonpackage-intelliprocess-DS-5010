import unittest
import pandas as pd
import numpy as np
from io import StringIO
from unittest.mock import patch
import matplotlib.pyplot as plt
from intelliproc import IntelliProcess

class TestIntelliProcess(unittest.TestCase):
    
    def setUp(self):
        # set up a pandas DataFrame
        data = StringIO('''A,B,C,D
                            1,2,3,4
                            5,6,7,8
                            9,10,11,12
                            13,14,15,NaN''')
        self.df = pd.read_csv(data)
        self.obj = IntelliProcess(self.df)
        
    def test_constructor(self):
        # Test initialization with valid pandas DataFrame
        self.assertTrue(isinstance(self.obj.data, pd.DataFrame))
        
        # Test initialization with non-pandas DataFrame object
        with self.assertRaises(IntelliProcessError):
            IntelliProcess([])
        
        # Test initialization with no input data
        with self.assertRaises(IntelliProcessError):
            IntelliProcess()
    
    def test_str(self):
        # Test string representation of object
        expected = "    A   B   C     D\n0   1   2   3   4.0\n1   5   6   7   8.0\n2   9  10  11  12.0\n3  13  14  15   NaN"
        self.assertEqual(str(self.obj), expected)
    
    def test_setitem(self):
        # Test setting an existing column
        self.obj["A"] = [2, 4, 6, 8]
        self.assertTrue(np.array_equal(self.obj.data["A"], [2, 4, 6, 8]))
        
        # Test setting a new column
        self.obj["E"] = [1, 2, 3, 4]
        self.assertTrue(np.array_equal(self.obj.data["E"], [1, 2, 3, 4]))
    
    def test_getitem(self):
        # Test getting an existing column
        col = self.obj["A"]
        self.assertTrue(np.array_equal(col, [1, 5, 9, 13]))
        
        # Test getting a non-existing column
        with self.assertRaises(KeyError):
            self.obj["X"]
    
    def test_column_list(self):
        # Test getting a list of column names
        expected = ["A", "B", "C", "D"]
        self.assertEqual(self.obj.column_list(), expected)
    
    def test_get_data(self):
        # Test getting the underlying DataFrame object
        self.assertTrue(isinstance(self.obj.get_data(), pd.DataFrame))
    
    def test_set_data(self):
        # Test updating the underlying DataFrame object
        new_data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        self.obj.set_data(new_data)
        self.assertTrue(np.array_equal(self.obj.data["A"], [1, 2, 3]))
        self.assertTrue(np.array_equal(self.obj.data["B"], [4, 5, 6]))
        
        # Test updating with non-pandas DataFrame object
        with self.assertRaises(IntelliProcessError):
            self.obj.set_data([])
    
    def test_select_num(self):
        # Test selecting only numeric columns
        expected = pd.DataFrame({"A": [1, 5, 9, 13], "B": [2, 6, 10, 14], "C": [3, 7, 11, 15]})
        self.assertTrue('col1' in num_df.columns)
        self.assertTrue('col2' in num_df.columns)
        self.assertTrue('col4' in num_df.columns)
        self.assertTrue('col5' not in num_df.columns)



    def test_nan_frequency(self):
        expected_output = {
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0,
            'E': 0
        }
        self.assertEqual(self.processor.nan_frequency(), expected_output)

    def test_fill_missing_values(self):
        self.processor.fill_missing_values()
        self.assertFalse(self.processor.df.isnull().values.any())

    def test_datatype_frequency(self):
        expected_output = {
            'int64': 1,
            'object': 2,
            'float64': 1,
            'bool': 1
        }
        self.assertEqual(self.processor.datatype_frequency(), expected_output)

    def test_feature_type_frequency(self):
        expected_output = {
            'categorical': 2,
            'numerical': 3
        }
        self.assertEqual(self.processor.feature_type_frequency(), expected_output)

    def test_suggest_encoding(self):
        expected_output = {
            'B': 'one-hot',
            'D': 'label',
            'E': 'label'
        }
        self.assertEqual(self.processor.suggest_encoding(), expected_output)

    def test_encode_data(self):
        expected_output = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B_a': [1, 0, 0, 0, 0],
            'B_b': [0, 1, 0, 0, 0],
            'B_c': [0, 0, 1, 0, 0],
            'B_d': [0, 0, 0, 1, 0],
            'B_e': [0, 0, 0, 0, 1],
            'C': [0.1, 0.2, 0.3, 0.4, 0.5],
            'D': [1, 0, 1, 0, 1],
            'E': [1, 0, 1, 0, 1]
        })
        self.processor.encode_data('one-hot')
        pd.testing.assert_frame_equal(self.processor.df, expected_output)

    def test_outlier_removal_IQR_method(self):
        expected_output = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': ['a', 'b', 'c', 'd', 'e'],
            'C': [0.1, 0.2, 0.3, 0.4, 0.5],
            'D': ['yes', 'no', 'yes', 'no', 'yes'],
            'E': [True, False, True, False, True]
        })
    
if __name__ == '__main__':
    unittest.main()
