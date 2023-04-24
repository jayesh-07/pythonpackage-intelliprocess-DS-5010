import unittest
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from intelliproc import IntelliProcess, IntelliProcessError
import timeit
import numpy as np
import json
import csv
import os
from io import StringIO



class TestIntelliProcess(unittest.TestCase):
    '''
    Unit tests for the Intelliproc class methods
    '''
    
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
        self.data = pd.DataFrame({
            'a': [1, 2, 3],
            'b': [4.0, 5.0, 6.0],
            'c': ['cat', 'dog', 'bird']
        })
        intelli_process = IntelliProcess(self.data)
        result = intelli_process.select_num()
        expected_result = pd.DataFrame({
            'a': [1, 2, 3],
            'b': [4.0, 5.0, 6.0]
        })
        pd.testing.assert_frame_equal(result, expected_result)


    def test_nan_frequency(self):
        # Test that the `nan_frequency` method correctly returns a nested list that has 1st element as feature name and 2nd element the count of NaN Values.
        data = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6], 'C': [7, 8, 9]})
        process = IntelliProcess(data)
        nan_frequency_list = process.nan_frequency()
        assert nan_frequency_list == [['A', 1], ['B', 1], ['C', 0]]

    def test_fill_missing_values(self):
        # create a dataframe with missing values
        df = pd.DataFrame({
            'numeric_col': [1, 2, 3, None, 5],
            'categorical_col': ['a', 'b', None, 'a', 'c'],
            'string_col': ['foo', 'bar', 'baz', None, 'qux'],
            'datetime_col': pd.to_datetime(['2021-01-01', '2021-01-02', '2021-01-03', None, '2021-01-05']),
            'timedelta_col': pd.to_timedelta(['1 days', '2 days', None, '4 days', '5 days'])
        })

        # create an IntelliProcess object with the dataframe
        ip = IntelliProcess(data=df)

        # fill missing values
        filled_df = ip.fill_missing_values()

        # check that there are no missing values in the filled dataframe
        self.assertFalse(filled_df.isnull().values.any())

    def test_datatype_frequency(self):
        # create test dataframe
        data = StringIO("name,age,salary\njohn,30,50000\njane,25,60000\nbob,35,70000")
        df = pd.read_csv(data)

        # create instance of IntelliProcess class
        ip = IntelliProcess(df)

        # call datatype_frequency method
        result = ip.datatype_frequency()

        # check if the result is a nested list with the correct elements
        assert isinstance(result, list)
        assert len(result) == 3
        assert all(isinstance(i, list) and len(i) == 2 for i in result)

        # check if the plot is created
        assert plt.fignum_exists(1)

        # check if the plot has the correct title, x and y labels
        ax = plt.gca()
        assert ax.get_title() == 'Data Type Frequency'
        assert ax.get_xlabel() == 'Data Type'
        assert ax.get_ylabel() == 'Count'

        # check if the plot bars represent the correct data types and counts
        assert ax.patches[0].get_height() == 3
        assert ax.patches[1].get_height() == 3

        # check if the plot x ticks represent the correct data types
        assert ax.get_xticklabels()[0].get_text() == "int64"
        assert ax.get_xticklabels()[1].get_text() == "object"

    def test_feature_type_frequency(self):
        self.data = pd.DataFrame({
            'a': ['foo', 'bar', 'foo', 'bar', 'foo', 'foo', 'bar', 'foo'],
            'b': [1, 2, 3, 4, 5, 6, 7, 8],
            'c': ['spam', 'ham', 'spam', 'ham', 'spam', 'spam', 'ham', 'spam']
        })
        self.processor = IntelliProcess(self.data)
        expected_result = [['Categorical', 2], ['Numerical', 1]]
        result = self.processor.feature_type_frequency()
        self.assertEqual(result, expected_result)

    def test_suggest_encoding(self):
        self.df_label = pd.DataFrame({'A': ['foo', 'bar', 'baz', 'bar'], 
                                'B': [1, 2, 3, 4], 
                                'C': [0.1, 0.2, 0.3, 0.4]})
        self.df_onehot = pd.DataFrame({'A': ['foo', 'bar', 'baz', 'bar'], 
                                'B': [1, 2, 3, 4], 
                                'C': [0.1, 0.2, 0.3, 0.4]})
        self.df_binary = pd.DataFrame({'A': ['foo', 'bar', 'baz', 'bar'], 
                                'B': [1, 2, 3, 4], 
                                'C': [0.1, 0.2, 0.3, 0.4]})
        ip_label = IntelliProcess(self.df_label)
        self.assertEqual(ip_label.suggest_encoding(), 'label')
        ip_one = IntelliProcess(self.df_onehot)
        self.assertEqual(ip_one.suggest_encoding(), 'one-hot')
        ip_binary = IntelliProcess(self.df_binary)
        self.assertEqual(ip_binary.suggest_encoding(), 'binary')
    
    def test_encode_data_label(self):
        # Test label encoding
        self.df = pd.DataFrame({'A': ['foo', 'bar', 'baz', 'bar'], 
                                'B': [1, 2, 3, 4], 
                                'C': [0.1, 0.2, 0.3, 0.4]})
        processor = IntelliProcess(self.df)
        encoded_data = processor.encode_data('label')
        self.assertIsInstance(encoded_data, pd.DataFrame)
        self.assertListEqual(list(encoded_data.columns), ['A', 'B', 'C'])
        self.assertListEqual(list(encoded_data['A']), [0, 1, 2, 1])

    def test_encode_data_one_hot(self):
        # Test one-hot encoding
        self.df = pd.DataFrame({'A': ['foo', 'bar', 'baz', 'bar'], 
                                'B': [1, 2, 3, 4], 
                                'C': [0.1, 0.2, 0.3, 0.4]})
        processor = IntelliProcess(self.df)
        encoded_data = processor.encode_data('one-hot')
        self.assertIsInstance(encoded_data, pd.DataFrame)
        self.assertListEqual(list(encoded_data.columns), ['foo', 'bar', 'baz', 'B', 'C'])
        self.assertListEqual(list(encoded_data['foo']), [1, 0, 0, 0])
        self.assertListEqual(list(encoded_data['bar']), [0, 1, 0, 1])
        self.assertListEqual(list(encoded_data['baz']), [0, 0, 1, 0])

    def test_encode_data_binary(self):
        # Test binary encoding
        self.df = pd.DataFrame({'A': ['foo', 'bar', 'baz', 'bar'], 
                                'B': [1, 2, 3, 4], 
                                'C': [0.1, 0.2, 0.3, 0.4]})
        processor = IntelliProcess(self.df)
        encoded_data = processor.encode_data('binary')
        self.assertIsInstance(encoded_data, pd.DataFrame)
        self.assertListEqual(list(encoded_data.columns), ['A_foo', 'A_bar', 'A_baz', 'B', 'C'])
        self.assertListEqual(list(encoded_data['A_foo']), [1, 0, 0, 0])
        self.assertListEqual(list(encoded_data['A_bar']), [0, 1, 0, 1])
        self.assertListEqual(list(encoded_data['A_baz']), [0, 0, 1, 0])

    def test_encode_data_invalid(self):
        # Test invalid encoding type
        self.df = pd.DataFrame({'A': ['foo', 'bar', 'baz', 'bar'], 
                                'B': [1, 2, 3, 4], 
                                'C': [0.1, 0.2, 0.3, 0.4]})
        processor = IntelliProcess(self.df)
        encoded_data = processor.encode_data('invalid')
        self.assertIsNone(encoded_data)

    def test_outlier_removal_IQR_method(self):
        expected_output = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': ['a', 'b', 'c', 'd', 'e'],
            'C': [0.1, 0.2, 0.3, 0.4, 0.5],
            'D': ['yes', 'no', 'yes', 'no', 'yes'],
            'E': [True, False, True, False, True]
        })

    def test_select_x(self):
        self.df = pd.DataFrame({
            'x1': [1, 2, 3, 4],
            'x2': [5, 6, 7, 8],
            'x3': [9, 10, 11, 12]
        })
        self.processor = IntelliProcess(self.df)

        x_name = 'x1'
        expected_output = np.array([1, 2, 3, 4])
        np.testing.assert_array_equal(self.processor.select_x(x_name), expected_output)

    def test_skew(self):
        data = {'A': [1, 2, 3, 4, 5],
            'B': [6, 7, 8, 9, 10],
            'C': [11, 12, 13, 14, 15]}
        df = pd.DataFrame(data)
        intelli = IntelliProcess(df)
        skewness = intelli.skew()
        expected_skewness = {'A': -1.264911064067352,
                            'B': -1.264911064067352,
                            'C': -1.264911064067352}
        self.assertEqual(skewness, expected_skewness)


    def test_scaling_box_cox(self):
        # Create a sample data set
        data = {'x': np.random.normal(loc=10, scale=2, size=100)}
        df = pd.DataFrame(data)

        # Create an instance of IntelliProcess and call scaling_box_cox on x
        processor = IntelliProcess(df)
        transformed = processor.scaling_box_cox(df['x'])

        # Ensure that transformed has the same length as x
        assert len(transformed) == len(df['x'])

        # Ensure that the lambda value is not null
        #assert isinstance(processor.fitted_lambda, float)
        
        # Ensure that the transformed data has a normal distribution
        assert stats.normaltest(transformed).pvalue > 0.05

        # Ensure that the plots are displayed
        assert plt.gcf()

    def test_scaling_log(self):
        # create a sample dataframe with positive values
        data = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [6, 7, 8, 9, 10]
        })
        intelli_process = IntelliProcess(data)
        
        # test on column 'A'
        x_column = data['A']
        data_output = intelli_process.scaling_log(x_column)
        
        # assert that transformed values are correct
        assert np.array_equal(data_output, pd.DataFrame(np.log10(x_column)))

    
if __name__ == '__main__':
    unittest.main(verbosity=3)
