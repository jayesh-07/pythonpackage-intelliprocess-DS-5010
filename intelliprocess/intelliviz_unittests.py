import unittest
import pandas as pd
from intelliviz import IntelliViz, IntelliVizError
from intelliproc import IntelliProcess, IntelliProcessError
import timeit
import numpy as np
import json
import csv

filepath = open('/Users/s.hussey/shane_workspace/DS5010_Spring2023/Project/Testing_Datasets/testing_datasets.json').read()
path = '/Users/s.hussey/shane_workspace/DS5010_Spring2023/Project'
testing_datasets = json.loads(filepath)





class IntelliViz_init(unittest.TestCase):
    '''
    Unit tests for the IntelliViz class

    '''
    def data_config(self):
        self.data = {'A': [1, 2, 3, 4, 5],
                     'B': [4, 5, 6, 7, 8],
                     'C': [7, 8, 9, 10, 11]}
        df = pd.DataFrame(data)



    def test_init_load_df(self):
        i = IntelliViz(self.df)


    def test_init_no_df_given(self):
        self.assertRaises(IntelliViz(),IntelliVizError)

class IntelliViz___str__(unittest.TestCase):
    def test_correlation_matrix(self):
        pass


class IntelliViz_get_columns(unittest.TestCase):
    def test_correlation_matrix(self):
        pass

class IntelliViz_get_df(unittest.TestCase):
    def test_correlation_matrix(self):
        pass

class IntelliViz_set_df(unittest.TestCase):
    def test_correlation_matrix(self):
        pass

class IntelliViz_correlation_matrix(unittest.TestCase):
    def test_correlation_matrix(self):
        pass

class IntelliViz_correlation_heatmap(unittest.TestCase):
    def test_correlation_heatmap_sonar(self):
        ''' perform visual inspection of each graph using sonar dataset in testing_datasets.json '''
        df = pd.read_csv(path + str(testing_datasets["data"]["sonar"]["datafile"]))
        i = IntelliViz(df)
        i.correlation_matrix_heatmap(save=False)

        # comments:


    def test_correlation_heatmap_employee_attrition_test(self):
        ''' perform visual inspection of each graph using employee_attrition_test dataset in testing_datasets.json '''
        df = pd.read_csv(path + str(testing_datasets["data"]["employee_attrition_test"]["datafile"]))
        i = IntelliViz(df)
        i.correlation_matrix_heatmap(save=False)

        # comments:
        # check why there are whole white lines


    def test_correlation_heatmap_migraine_classification(self):
        ''' perform visual inspection of each graph using migraine-classification dataset in testing_datasets.json '''
        df = pd.read_csv(path + str(testing_datasets["data"]["migraine-classification"]["datafile"]))
        i = IntelliViz(df)
        i.correlation_matrix_heatmap(save=False)

        # comments:

    def test_correlation_heatmap_iris(self):
        ''' perform visual inspection of each graph using iris dataset in testing_datasets.json'''
        df = pd.read_csv(path + str(testing_datasets["data"]["iris"]["datafile"]))
        i = IntelliViz(df)
        i.correlation_matrix_heatmap(save=False)

        # comments:

    def test_correlation_heatmap_higher_ed(self):
        '''
        perform visual inspection of each graph using higher-education-predictors-of-student-retention
        dataset in testing_datasets.json
        '''
        df = pd.read_csv(path +
                         str(testing_datasets["data"]["higher-education-predictors-of-student-retention"]["datafile"]))
        i = IntelliViz(df)
        i.correlation_matrix_heatmap(save=False)

        # comments:
        # this looks pretty good, everything is shown colored (has a value)
        # text well spaced


    def test_correlation_heatmap_internet_advert(self):
        ''' perform visual inspection of each graph using internet-advertisements-data-set dataset in testing_datasets.json'''
        df = pd.read_csv(path + str(testing_datasets["data"]["internet-advertisements-data-set"]["datafile"]))
        i = IntelliViz(df)
        i.correlation_matrix_heatmap(save=False)

        # comments:


    def test_correlation_heatmap_HepatitisCdata(self):
        ''' perform visual inspection of each graph using HepatitisCdata dataset in testing_datasets.json'''
        df = pd.read_csv(path + str(testing_datasets["data"]["HepatitisCdata"]["datafile"]))
        i = IntelliViz(df)
        i.correlation_matrix_heatmap(save=False)

        # comments:


    def test_correlation_heatmap_menstennisrankings(self):
        ''' perform visual inspection of each graph using menstennisrankings dataset in testing_datasets.json'''
        df = pd.read_csv(path + str(testing_datasets["data"]["menstennisrankings"]["datafile"]))
        i = IntelliViz(df)
        i.correlation_matrix_heatmap(save=False)

        # comments:


    def test_correlation_heatmap_housing(self):
        ''' perform visual inspection of each graph using housing dataset in testing_datasets.json'''
        df = pd.read_csv(path + str(testing_datasets["data"]["housing"]["datafile"]))
        i = IntelliViz(df)
        i.correlation_matrix_heatmap(save=False)

        # comments:
        # text well spaced,
        # total bedrooms has missing values, so it is coming up null


    def test_correlation_heatmap_toy(self):
        ''' perform visual inspection of each graph using toy dataset in testing_datasets.json'''
        df = pd.read_csv(path + str(testing_datasets["data"]["toy"]["datafile"]))
        i = IntelliViz(df)
        i.correlation_matrix_heatmap(save=False)

        # comments:


    def test_correlation_heatmap_poker_hand_training(self):
        ''' perform visual inspection of each graph using poker-hand-training dataset in testing_datasets.json'''
        df = pd.read_csv(path + str(testing_datasets["data"]["poker-hand-training"]["datafile"]))
        i = IntelliViz(df)
        i.correlation_matrix_heatmap(save=False)

        # comments:


    def test_correlation_heatmap_usedcarscatalog(self):
        ''' perform visual inspection of each graph using usedcarscatalog dataset in testing_datasets.json'''
        df = pd.read_csv(path + str(testing_datasets["data"]["usedcarscatalog"]["datafile"]))
        i = IntelliViz(df)
        i.correlation_matrix_heatmap(save=False)

        # comments:



class IntelliViz_columns_scatter(unittest.TestCase):
    def test_correlation_matrix(self):
        pass
class IntelliViz_violin_plot(unittest.TestCase):
    def test_correlation_matrix(self):
        pass
class IntelliViz_pie_chart(unittest.TestCase):
    def test_correlation_matrix(self):
        pass

class IntelliViz_histogram(unittest.TestCase):
    def test_correlation_matrix(self):
        pass

class IntelliViz_qqplot(unittest.TestCase):
    def test_correlation_matrix(self):
        pass




if __name__ == '__main__':
    #unittest.main(verbosity=3)

    df = pd.read_csv(path + str(testing_datasets["data"]["sonar"]["datafile"]))
    ip = IntelliProcess(df)
    #check __str__ method()
    print(ip)
    #check column_list function
    print(ip.column_list())
    # check get_data function
    print(ip.get_data())
    # check get_data function
    print(ip.select_num())
    # print nan_frequency
    print(ip.nan_frequency())
    # test fill_missing_values
    print(ip.fill_missing_values())
    # check datatype frequency functin
    print(ip.datatype_frequency())
    print(ip.feature_type_frequency())
    print(ip.suggest_encoding())
    print(ip.encode_data('label'))
    print(ip.outlier_removal_IQR_method())











    """
    df = pd.read_csv("sonar.csv")
    i = IntelliViz(df)
    columns = i.get_columns()
    print(columns)
    corr = i.pearsons_r(df["attribute_60"],df["attribute_60"])
    print(corr)
    corr_matrix = i.pearson_corr_matrix()
    print(corr_matrix.to_string())
    #fig = i.correlation_matrix_heatmap()
    fig, ax = i.boxplot()
    """


    '''
    s = """
import pandas as pd
from intelliviz import IntelliViz
df = pd.read_csv("sonar.csv")
i = IntelliViz(df)
i.pearson(df["attribute_1"], df["attribute_2"])
        """
    # time_r = timeit.timeit(s, number=10000)
    # print(time_r)
    s = """
import pandas as pd
from intelliviz import IntelliViz
df = pd.read_csv("sonar.csv")
i = IntelliViz(df)
i.pearson_pyarrow(df["attribute_1"], df["attribute_2"])
        """
    time_r = timeit.timeit(s, number=10000)
    print(time_r)
    s = """
import pandas as pd
from intelliviz import IntelliViz
df = pd.read_csv("sonar.csv")
i = IntelliViz(df)
df.corr()
    """
    time_pandas = timeit.timeit(s, number=10000)
    print(time_pandas)
    '''



