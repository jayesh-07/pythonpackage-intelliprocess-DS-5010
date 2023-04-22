import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import csv
import os
import datetime


def column_list(data):
    """
    Creates a list of column names for a given dataset.
    :param data: a pandas data frame
    :return:a list of the data's column names
    """
    columns_names = data.columns
    column_names_list = columns_names.tolist()
    return column_names_list


def select_num(data_location):
    """
    Creates a subset of a given dataset, sampling
    only the numeric variables.
    :param data_location: string indicating file path
    for a given dataset.
    :return:a pandas data frame containing all columns
    in which numeric values are identified.
    """
    df_input = pd.read_csv(data_location)
    data = pd.DataFrame(df_input)
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    data_numeric = data.select_dtypes(include=numerics)
    return data_numeric


def select_x(data_location, x_name):
    """
    Creates a subset containing a single variable in a
    given dataset, when provided the dataset's
    filepath and column name of the chosen variable.
    :param data_location: filepath
    :param x_name: string indicating the name of
    the requested column to subset.
    :return:data frame of data subset
    """
    data = select_num(data_location)
    df = data[x_name].copy().to_numpy()
    return df


# Skewness and Histogram PLots:
# Fisher-Pearson method of Skew Measure
def skew(data_numeric):
    """
    Creates an associative array containing all column
    names of a given dataset and their calculated
    Fisher-Pearson skew value.
    :param data_numeric: a dataset of only numerics
    :return:skewness: a dictionary containing the
    column names as keys and associated skewness numbers
    as values.
    """
    skewness = dict()
    data_cols = column_list(data_numeric)
    for i in range(len(data_cols)):
        means = data_numeric.mean()
        mean = means.values
        modes = data_numeric.mode()
        mode = modes.values
        sds = data_numeric.std()
        sd = sds.values
        skew_number_array = (mean[i] - mode[i]) / sd[i]
        skew_list = skew_number_array.tolist()
        for j in range(len(data_cols)):
            skewness[data_cols[j]] = skew_list[j]
        return skewness


def histogram_plots(data_numeric):
    """
    Creates a 2x2 plot of histograms, each utilizes one of
    four varied binwidths (5, 10, 15, 20) and contain a
    different colored histogram  for each of the columns
    in a given numeric dataset.
    :param data_numeric:  a dataset of only numerics
    :return: None
    """
    for i, binswidth in enumerate([5, 10, 15, 20]):
        axes = plt.subplot(2, 2, i + 1)
        axes.hist(data_numeric, bins=int(180 / binswidth))

        axes.set_title('Histogram with Binwidth = %d' % binswidth, size=10)
        axes.set_xlabel('x_axis_label', size=10)
        axes.set_ylabel('y_axis_label', size=10)

    plt.tight_layout()
    plt.show()
    return None


# Scaling/ Transforming Data:
# Progressing - Need to check once 'select_x' fcn is complete
def scaling_box_cox(x_column):
    """

    :param x_column:
    :return: None
    """
    transformed, fitted_lambda = stats.boxcox(x_column)
    fig, axes = plt.subplots(1, 2)

    sns.histplot(x_column, kde = True, ax = axes[0],
                    label="Original Data", color="black")
    sns.histplot(values,kind = "hist", kde = True, ax = axes[1],
                    label ="Transformed Data", color="black")
    print(f"Lambda value used for Transformation: {fitted_lambda}")
    plt.show()
    return transformed


# Log Transformation for a Given Column
# Progressing - Incomplete
# incorporate with scatterplot fcn (shane)
def scaling_log(x_column):
    """
    Transforms a single column of values based on
    a log base 10 and provides two plots
    :param x_column: a subset of a single variable
    from a given dataset.
    :return: data_output:
    """
    values = np.log10(x_column)
    data_output = pd.DataFrame(values)
    fig, axes = plt.subplots(1, 2)

    sns.histplot(x_column, kde = True, ax = axes[0],
                    label="Original Data", color="black")
    sns.histplot(values,kind = "hist", kde = True, ax = axes[1],
                    label ="Transformed Data", color="black")
    plt.show()
    return data_output


# Outlier Detection and Removal
# Enables IQR method
def outlier_removal_IQR_method(data_numeric, save = True, filename = "intelliprocess_outliers_iqr_file"):
    """
    Removes outliers based on inter quartile range
    and provides a csv file output.
    :param data_numeric: data frame of all numeric values.
    :return: updated_data: a new csv file with outlier
    observations removed.
    """
    Q3 = data_numeric.quantile(0.75)
    Q1 = data_numeric.quantile(0.25)
    IQR = (Q3 - Q1)

    updated_data = data_numeric[~(
            (data_numeric < (Q1 - 1.5 * IQR)) | (data_numeric > (Q3 + 1.5 * IQR)))]

    if save is True:
        timestamp = str(datetime.datetime.now()).replace(" ", "")
        filename = filename + "" + timestamp + ".csv "
        updated_data.to_csv(filename)
    return updated_data


if __name__ == "__main__":
    # Works
    print(scaling_box_cox(select_x('/Users/taylorgoodwin/Documents/GitHub/'
                                   'pythonpackage-intelliprocess-DS-5010/'
                                   'intelliprocess/Testing_Datasets/iris.csv', 'sepal_width')))

    # Works
    print(scaling_log(select_x('/Users/taylorgoodwin/Documents/GitHub/'
                          'pythonpackage-intelliprocess-DS-5010/'
                          'intelliprocess/Testing_Datasets/iris.csv', 'sepal_width')))

    # Works
    print(skew(select_num('/Users/taylorgoodwin/Documents/GitHub/'
                          'pythonpackage-intelliprocess-DS-5010/'
                          'intelliprocess/Testing_Datasets/iris.csv')))
    # Works
    outlier_removal_IQR_method(select_num('/Users/taylorgoodwin/Documents/GitHub/'
                                                'pythonpackage-intelliprocess-DS-5010/'
                                                'intelliprocess/Testing_Datasets/iris.csv'))
    # Works
    print(histogram_plots(select_num('/Users/taylorgoodwin/Documents/GitHub/'
                                     'pythonpackage-intelliprocess-DS-5010/'
                                     'intelliprocess/Testing_Datasets/iris.csv')))
