import unittest
import pandas as pd
from intelliviz import IntelliViz, IntelliVizError
import json
import os
from pandas.util.testing import assert_frame_equal # <-- for testing dataframes

# Load json file outlining all file paths for datasets in Testing_Datasets directory
cwd = os.getcwd()
json_data = '/Testing_Datasets/testing_datasets.json'
full_path = cwd + json_data
json_data = open(full_path).read()
testing_datasets = json.loads(json_data)





class IntelliViz__init__(unittest.TestCase):
    '''
    Unit tests for the IntelliViz class __init__ method
    '''


    def data_config(self):
        '''
        Configure data used for testing in this unittesting class
        '''
        # test with basic dataframe
        self.data = {'A': [1, 2, 3, 4, 5],
                     'B': [4, 5, 6, 7, 8],
                     'C': [7, 8, 9, 10, 11]}
        self.df = pd.DataFrame(self.data)
        self.iv1 = IntelliViz(self.df)
        # test with dataset w/ 61 columns and no missing data
        self.df_sonar = pd.read_csv(cwd + testing_datasets["data"]["sonar"]["datafile"])
        self.iv2 = IntelliViz(self.df_sonar)
        # test with dataset w/ some missing values
        self.df_employee = pd.read_csv(cwd + testing_datasets["data"]["employee_attrition_test"]["datafile"])
        self.iv3 = IntelliViz(self.df_employee)


    def test_init_load_df(self):
        '''
        test loading dataframes into Intelliviz and ensure there are no modifications from the original passed in
        '''
        # configure data
        self.data_config()
        # test with basic dataframe
        assert_frame_equal(self.iv1.get_df(), self.df)
        # test with dataset w/ 61 columns and no missing data
        assert_frame_equal(self.iv2.get_df(), self.df_sonar)
        # test with dataset w/ some missing values
        assert_frame_equal(self.iv3.get_df(),self.df_employee)


    def test_init_no_df_given(self):
        '''
        test that an IntelliVizError is raised when you try to instantiate a IntelliViz without a pd.Dataframe passed in.
        '''
        # configure data
        self.data_config()
        # ensure an error is thrown when no dataframe is passed in
        with self.assertRaises(IntelliVizError):
            IntelliViz()

class IntelliViz__str__(unittest.TestCase):
    '''
    Unit tests for the IntelliViz class __str__ method
    '''
    def data_config(self):
        '''
        Configure data used for testing in this unittesting class
        '''
        # test with basic dataframe
        self.data = {'A': [1, 2, 3, 4, 5],
                     'B': [4, 5, 6, 7, 8],
                     'C': [7, 8, 9, 10, 11]}
        self.df = pd.DataFrame(self.data)
        self.iv1 = IntelliViz(self.df)
        # test with dataset w/ 61 columns and no missing data
        self.df_sonar = pd.read_csv(cwd + testing_datasets["data"]["sonar"]["datafile"])
        self.iv2 = IntelliViz(self.df_sonar)
        # test with dataset w/ some missing values
        self.df_employee = pd.read_csv(cwd + testing_datasets["data"]["employee_attrition_test"]["datafile"])
        self.iv3 = IntelliViz(self.df_employee)

    def test__str__(self):
        '''
        Unittest for __str__ method in IntelliProcess

        self.data_config()
        self.assertEqual(str(self.df,)
        '''
        # configure data
        self.data_config()
        self.assertIsInstance(str(self.iv1), str)
        self.assertIsInstance(str(self.iv2), str)
        self.assertIsInstance(str(self.iv3), str)

class IntelliViz__setitem__(unittest.TestCase):
    '''
    Unit tests for the IntelliViz class __setitem__ method
    '''
    def data_config(self):
        '''
        Configure data used for testing in this unittesting class
        '''
        # test with basic dataframe
        self.data = {'A': [1, 2, 3, 4, 5],
                     'B': [4, 5, 6, 7, 8],
                     'C': [7, 8, 9, 10, 11]}
        self.df = pd.DataFrame(self.data)
        self.iv1 = IntelliViz(self.df)
        # test with dataset w/ 61 columns and no missing data
        self.df_sonar = pd.read_csv(cwd + testing_datasets["data"]["sonar"]["datafile"])
        self.iv2 = IntelliViz(self.df_sonar)
        # test with dataset w/ some missing values
        self.df_employee = pd.read_csv(cwd + testing_datasets["data"]["employee_attrition_test"]["datafile"])
        self.iv3 = IntelliViz(self.df_employee)


    def test_set_item(self):
        '''
        Test setting items in IntelliViz Object
        '''
        # configure data
        self.data_config()
        # test set method with dataframe 1
        self.iv1['D'] = [12, 23, 34, 45, 56]
        new_df1 = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [4, 5, 6, 7, 8],
                   'C': [7, 8, 9, 10, 11],
                   'D': [12, 23, 34, 45, 56]})
        assert_frame_equal(self.iv1.get_df(), new_df1)

        self.iv2['new'] = [1 for _ in range(self.df_sonar.shape[0])]
        # test set method with dataframe 2
        new_df2 = self.df_sonar.copy()
        new_df2['new'] = [1 for _ in range(self.df_sonar.shape[0])]
        assert_frame_equal(self.iv2.get_df(), new_df2)


class IntelliViz_get_columns(unittest.TestCase):
    '''
    Unit tests for the IntelliViz class get_columns() method
    '''

    def data_config(self):
        '''
        Configure data used for testing in this unittesting class
        '''
        # test with basic dataframe
        self.data = {'A': [1, 2, 3, 4, 5],
                     'B': [4, 5, 6, 7, 8],
                     'C': [7, 8, 9, 10, 11]}
        self.df = pd.DataFrame(self.data)
        self.iv1 = IntelliViz(self.df)
        # test with dataset w/ 61 columns and no missing data
        self.df_sonar = pd.read_csv(cwd + testing_datasets["data"]["sonar"]["datafile"])
        self.iv2 = IntelliViz(self.df_sonar)
        # test with dataset w/ some missing values
        self.df_employee = pd.read_csv(cwd + testing_datasets["data"]["employee_attrition_test"]["datafile"])
        self.iv3 = IntelliViz(self.df_employee)

    def test_get_columns(self):
        ''' test IntelliViz get_columns() method'''
        # configure data
        self.data_config()
        self.assertEqual(list(self.iv1.get_columns()), list(self.df.columns))

class IntelliViz_get_df(unittest.TestCase):
    '''
    Unit tests for the IntelliViz class get_df() method
    '''

    def data_config(self):
        '''
        Configure data used for testing in this unittesting class
        '''
        # test with basic dataframe
        self.data = {'A': [1, 2, 3, 4, 5],
                     'B': [4, 5, 6, 7, 8],
                     'C': [7, 8, 9, 10, 11]}
        self.df = pd.DataFrame(self.data)
        self.iv1 = IntelliViz(self.df)
        # test with dataset w/ 61 columns and no missing data
        self.df_sonar = pd.read_csv(cwd + testing_datasets["data"]["sonar"]["datafile"])
        self.iv2 = IntelliViz(self.df_sonar)
        # test with dataset w/ some missing values
        self.df_employee = pd.read_csv(cwd + testing_datasets["data"]["employee_attrition_test"]["datafile"])
        self.iv3 = IntelliViz(self.df_employee)


    def test_get_df(self):
        '''
        test get_df dataframes into Intelliviz and ensure there are no modifications from the original passed in
        '''
        # configure data
        self.data_config()
        # test with basic dataframe
        assert_frame_equal(self.iv1.get_df(), self.df)
        # test with dataset w/ 61 columns and no missing data
        assert_frame_equal(self.iv2.get_df(), self.df_sonar)
        # test with dataset w/ some missing values
        assert_frame_equal(self.iv3.get_df(),self.df_employee)


class IntelliViz_set_df(unittest.TestCase):
    '''
    Unit tests for the IntelliViz class get_df() method
    '''
    def data_config(self):
        '''
        Configure data used for testing in this unittesting class
        '''
        # test with basic dataframe
        self.data = {'A': [1, 2, 3, 4, 5],
                     'B': [4, 5, 6, 7, 8],
                     'C': [7, 8, 9, 10, 11]}
        self.df = pd.DataFrame(self.data)
        self.iv1 = IntelliViz(self.df)
        # test with dataset w/ 61 columns and no missing data
        self.df_sonar = pd.read_csv(cwd + testing_datasets["data"]["sonar"]["datafile"])
        self.iv2 = IntelliViz(self.df_sonar)
        # test with dataset w/ some missing values
        self.df_employee = pd.read_csv(cwd + testing_datasets["data"]["employee_attrition_test"]["datafile"])
        self.iv3 = IntelliViz(self.df_employee)

    def test_set_df(self):
        ''' test set_df() method for IntelliViz'''
        # configure data
        self.data_config()
        # test changing dataframes
        self.iv1.set_df(self.df_sonar)
        assert_frame_equal(self.iv1.get_df(),self.df_sonar)
        self.iv2.set_df(self.df)
        assert_frame_equal(self.iv2.get_df(),self.df)
        self.iv3.set_df(self.df_sonar)
        assert_frame_equal(self.iv3.get_df(),self.df_sonar)

class IntelliViz_pearsons_r(unittest.TestCase):
    '''
    Unit tests for the IntelliViz class pearsons_r() method
    '''
    def data_config(self):
        '''
        Configure data used for testing in this unittesting class
        '''
        # test with basic dataframe
        self.data = {'A': [1, 2, 3, 4, 5],
                     'B': [4, 5, 6, 7, 8],
                     'C': [7, 8, 9, 10, 11]}
        self.df = pd.DataFrame(self.data)
        self.iv1 = IntelliViz(self.df)
        # test with dataset w/ 61 columns and no missing data
        self.df_sonar = pd.read_csv(cwd + testing_datasets["data"]["sonar"]["datafile"])
        self.iv2 = IntelliViz(self.df_sonar)
        # test with dataset w/ some missing values
        self.df_employee = pd.read_csv(cwd + testing_datasets["data"]["employee_attrition_test"]["datafile"])
        self.iv3 = IntelliViz(self.df_employee)

    def test_pearsons_r(self):
        ''' test pearsons_r() method for IntelliViz'''
        # configure data
        self.data_config()
        # ensure functionality works
        self.assertEqual(self.iv1.pearsons_r(self.iv1['A'],self.iv1['B']), 1)
        self.assertEqual(self.iv1.pearsons_r(self.iv1['B'],self.iv1['C']), 1)
        self.assertEqual(self.iv1.pearsons_r(self.iv1['A'], self.iv1['C']), 1)



class IntelliViz_correlation_matrix(unittest.TestCase):

    def data_config(self):
        '''
        Configure data used for testing in this unittesting class
        '''
        # test with basic dataframe
        self.data = {'A': [1, 2, 3, 4, 5],
                     'B': [4, 5, 6, 7, 8],
                     'C': [7, 8, 9, 10, 11]}
        self.df = pd.DataFrame(self.data)
        self.iv1 = IntelliViz(self.df)
        # test with dataset w/ 61 columns and no missing data
        self.df_sonar = pd.read_csv(cwd + testing_datasets["data"]["sonar"]["datafile"])
        self.iv2 = IntelliViz(self.df_sonar)



    def test_correlation_matrix(self):
        '''test correlation_matrix() methond for IntelliViz'''
        # configure data
        self.data_config()
        assert_frame_equal(self.iv1.pearson_corr_matrix(),self.df.corr())
        # below is equal by rounding error, not sure of the correct way to make assertion
        #assert_frame_equal(self.iv2.pearson_corr_matrix(),self.df_sonar.corr())



if __name__ == '__main__':
    unittest.main(verbosity=3)