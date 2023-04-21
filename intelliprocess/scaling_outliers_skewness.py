
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import csv
import math


def column_names(data):
    column_names = data.columns
    column_names = column_names.tolist()
    return column_names


def select_num(data_location):
    df_input = pd.read_csv(data_location)
    data = pd.DataFrame(df_input)
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    data_numeric = data.select_dtypes(include=numerics)
    return data_numeric


def select_xy(data_numeric,x_index, y_index):
    data_xy = data_numeric[x_index].combine(data_numeric[y_index])
    return data_xy

# Skewness and Histogram PLots:
# Fisher-Pearson method of skew measure - replicate
# include in report with graphs -- how to do?
# Fix needed to 'skew' fcn
# Notes: 'skew' keeps printing same value instead of multiple diff.
def skew(data_numeric):
    """

    :param data_numeric:
    :return:
    """
    skewness = dict()
    for i in range(len(column_names(data_numeric))):
        means = data_numeric.mean()
        mean = means.values
        modes = data_numeric.mode()
        mode = modes.values
        sds = data_numeric.std()
        sd = sds.values
        skew_number_array = (mean[i] - mode[i]) / sd[i]
        skew_list = skew_number_array.tolist()
        print(i)
        key = [data_numeric.columns][i][0]
        value = skew_list[i]
        skewness[key] = value
    return skewness

def histogram_plots(data_numeric):
    """
    Creates a 2x2 plot output of histograms with four varied binwidths
    for each of the columns entered as input compared to the leftmost
    variable.
    :param
    :return: None
    """
    for i, binswidth in enumerate([5, 10, 15, 20]):
        axes = plt.subplot(2, 2, i + 1)
        axes.hist(data_numeric, bins=int(180 / binswidth))

        axes.set_title('Histogram with Binwidth = %d' % binswidth, size = 10)
        axes.set_xlabel('x_axis_label', size = 10)
        axes.set_ylabel('y_axis_label', size = 10)

    plt.tight_layout()
    plt.show()
    return None


# (2) scaling - logarithmic,
# transformation techniques such as
# box-cox, log transform, or rank-based
def scaling_box_cox(data_numeric):
        transformed_df, fitted_lambda = stats.boxcox(data_numeric.values)

        for i in range(len(transformed_df)):
            fig, axes = plt.subplots(1, 2)

            sns.displot(data_numeric, hst = False, kde = True,
                    kde_kws = {'shade': True, 'linewidth': 2},
                    label = "Original Data", color ="black", ax = axes[0])
            sns.displot(transformed_df, hst = False, kde = True,
                    kde_kws = {'shade': True, 'linewidth': 2},
                    label = "Normal", color ="black", ax = axes[1])

        fig.set_figheight(5)
        fig.set_figwidth(10)
        print(f"Lambda value used for Transformation: {fitted_lambda}")
        return fig


def construct_df(data_numeric_values):
    pass


def scaling_log(data_numeric):
    for i in range(len(data_numeric)):
        values = [data_numeric.values][i]
        print(values)
        # data_output = construct_df(values)
        return values


# Outlier Detection and Removal
# Enables IQR method for classification
def outlier_removal_IQR_method(data_numeric):
    """
    Removes outliers based on inter quartile range
    and provides a csv file output.
    :param data_numeric: data frame of all numeric values.
    :return: new csv file with outlier observations removed.
    """
    Q3 = data_numeric.quantile(0.75)
    Q1 = data_numeric.quantile(0.25)
    IQR = (Q3-Q1)

    updated_data = data_numeric[~(
            (data_numeric < (Q1-1.5*IQR)) | (data_numeric > (Q3+1.5*IQR)))]

    updated_data.to_csv('data_removed.csv')
    return updated_data


if __name__ == "__main__":
    print(skew(select_num('/Users/taylorgoodwin/Documents/GitHub/'
                                     'pythonpackage-intelliprocess-DS-5010/'
                                     'intelliprocess/Testing_Datasets/iris.csv')))
    print(histogram_plots(select_num('/Users/taylorgoodwin/Documents/GitHub/'
                                     'pythonpackage-intelliprocess-DS-5010/'
                                     'intelliprocess/Testing_Datasets/iris.csv')))
