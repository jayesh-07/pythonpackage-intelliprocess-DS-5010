
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import math

def means(data_numeric):
    """
    Calculates the average value of a column of numeric data.
    :param data_numeric: column containing numeric data values
    :return: the mean value of the given column
    """
    return data_numeric.mean()


def median(data_numeric):
    """

    :param data_numeric:
    :return:
    """
    n = len(data_numeric)
    if n % 2:
        return None


def mode(data):
    """

    :param data:
    :return:
    """
    for i in range(len(data.columns)):
        if data[i] == 'numeric ':
            pass
        else:
            val_list = []
            for j in range(len(data[i])):
                if str(data[i][j]) not in val_list:
                    val_list = val_list.append(str(data[i][j]))
        return val_list


def variance(data_numeric):
    """

    :param data_numeric:
    :return:
    """
    for i in range(len(data_numeric)):
        devs = [(data_numeric[i] - data_numeric[i].mean) ** 2
                for data_numeric[i] in data_numeric]
    return sum(devs)


def sd(data_numeric):
    """

    :param data_numeric:
    :return:
    """
    var = OurClass.variance(data_numeric)
    return math.sqrt(var)



# Skewness:

# (1) Fisher-Pearson method of skew measure - replicate
# include in report with graphs
def skew_number(data_numeric):
    """

    :param data_numeric:
    :return:
    """
    for i in range(len(data_numeric.columns)):
        mean = OurClass.means(data_numeric[i])
        mode = OurClass.mode(data_numeric[i])
        sd = OurClass.sd(data_numeric[i])
        return (mean - mode) / sd


# (2) scaling - logarithmic,
# transformation techniques such as
# box-cox, log transform, or rank-based



# (3) outlier detection - method and remove from df and output new file
def outlier_removal_IQR(data_numeric):
    """

    :param data_numeric:
    :return:
    """
    Q3 = data_numeric.quantile(0.75)
    Q1 = data_numeric.quantile(0.25)
    IQR = Q3-Q1

    data_removed = data_numeric[~(
            (data_numeric < (Q1-1.5*IQR)) | (data_numeric > (Q3+1.5*IQR)))]

    # convert to csv and provide download
    data_removed.to_csv('data_removed.csv')
    return data_removed


# # need to look at kernel density plots and histograms to discern distribution.
# def histograms(data_numeric):
#     for column_name in data_numeric.columns:
#         for i, binswidth in enumerate([1, 5, 10, 15]):
#             # Set up the plot
#             ax = plt.subplot(2, 2, i + 1)
#
#             # Draw the plot
#             ax.hist(data_numeric[column_name], bins=int(180 / binswidth),
#                     color='blue', edgecolor='black')
#
#             # Title and labels
#             ax.set_title('Histogram with Binwidth = %d' % binswidth, size=30)
#             ax.set_xlabel('x_label', size=20)
#             ax.set_ylabel('y_label', size=20)
#
#     plt.tight_layout()
#     plt.show()


if __name__ == "__main__":
    df_housing = pd.read_csv('/Users/taylorgoodwin/Documents/GitHub/pythonpackage-intelliprocess-DS-5010/intelliprocess/Testing_Datasets/housing.csv')
    data = pd.DataFrame(df_housing)
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    data_numeric = data.select_dtypes(include=numerics)

    print(sd(data_numeric))
   #  facet_wrap kernel plots