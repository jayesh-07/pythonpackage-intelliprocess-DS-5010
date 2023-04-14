import unittest
import pandas as pd
from intelliviz import IntelliViz
import timeit
import numpy as np



class IntelliViz_init(unittest.TestCase):
    def test_init_load_df(self):
        df = pd.read_csv("sonar.csv")
        i = IntelliViz(df)

    def test_init_no_df_given(self):
        pass

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
class IntelliViz_correlation_matrix_heatmap(unittest.TestCase):
    def test_correlation_matrix(self):
        pass
class IntelliViz_find_multicollinear_pairs(unittest.TestCase):
    def test_correlation_matrix(self):
        pass
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

    df = pd.read_csv("sonar.csv")
    i = IntelliViz(df)
    columns = i.get_columns()
    print(columns)
    corr = i.pearsons_r(df["attribute_60"],df["attribute_60"])
    print(corr)
    corr_matrix = i.pearson_corr_matrix()
    print(corr_matrix.to_string())
    fig = i.correlation_matrix_heatmap()

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



