import unittest
import pandas as pd
from intelliviz import IntelliViz



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
    i.qqplot(df["attribute_49"],line_type='s')


