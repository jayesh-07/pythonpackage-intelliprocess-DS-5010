

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


class DataError(TypeError):
    pass


class IntelliViz():
    '''

    '''
    def __init__(self, df=None):
        self.df = df

    def get_columns(self):
        '''

        :return:
        '''
        return self.df.columns

    def get_df(self):
        '''

        :return:
        '''
        return self.df

    def set_df(self, df=None):
        '''

        :param df:
        :return:
        '''
        if df is None:
            pass # raise custome error
        else:
            self.df = df

    def correlation_matrix(self):
        '''
        returns the correlation matrix of the self.df
        :return: correlation matrix of the self.df
        '''
        return self.df.corr()

    def correlation_matrix_heatmap(self,df=None, colors='coolwarm'):
        '''
        This code creates a sample dataset using pandas DataFrame, calculates the
        correlation matrix, and then uses matplotlib to create a heatmap.
        :param df:
        :return:
        '''

        # Compute the correlation matrix
        corr_matrix = self._compute_corr_matrix()

        # Create a heatmap of the correlation matrix
        fig, ax = plt.subplots()
        cax = ax.matshow(corr_matrix, cmap=colors)

        # Add colorbar and axis labels
        fig.colorbar(cax)
        ax.set_xticks(np.arange(len(corr_matrix.columns)))
        ax.set_yticks(np.arange(len(corr_matrix.columns)))
        ax.set_xticklabels(corr_matrix.columns)
        ax.set_yticklabels(corr_matrix.columns)

        # Rotate the x-axis labels
        plt.xticks(rotation=45)

        # Add correlation values to each square in the heatmap
        for i in range(len(corr_matrix.columns)):
            for j in range(len(corr_matrix.columns)):
                text = ax.text(j, i, round(corr_matrix.iloc[i, j], 2),
                               ha="center", va="center", color="black", fontsize=12)

        plt.show()

    def find_multicollinear_pairs(self, threshold=0.8) -> list:
        '''

        :param threshold:
        :return: multicollinear_pairs
        '''
        # Compute the correlation matrix
        corr_matrix = self.correlation_matrix()

        # Find pairs of multicollinear variables
        multicollinear_pairs = []

        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                if abs(corr_matrix.iloc[i, j]) >= threshold:
                    multicollinear_pairs.append((corr_matrix.columns[i],
                                                 corr_matrix.columns[j]))

        if len(multicollinear_pairs) > 0:
            print("Multicollinear variable pairs:")
            for pair in multicollinear_pairs:
                print(pair)
            return multicollinear_pairs
        else:
            print("No multicollinear variable pairs detected.")

    def columns_scatter(self,target_var=None):
        '''

        :param target_var:
        :return:
        '''

        # Create scatter plots for each variable against the target variable
        for col in df.columns:
            if col != target_var:
                plt.scatter(df[col], df[target_var])
                plt.xlabel(col)
                plt.ylabel(target_var)
                plt.title(f'Scatter plot of {col} vs {target_var}')
                plt.show()

    def violin_plot(self, x=None, y=None,title="Violin Plot",xlabel=None,ylabel=None,show=True):
        '''

        :param x:
        :param y:
        :param title:
        :param xlabel:
        :param ylabel:
        :param show:
        :return:
        '''

        data = sns.load_dataset("tips")
        fig = sns.violinplot(x=x, y=y, data=self.df)
        if x_label is not None:
            plt.xlabel(xlabel)
        if y_label is not None:
            plt.ylabel(ylabel)

        plt.title(title)
        if show is True:
            plt.show()

        return fig

    def pie_chart(self,labels=None,title="Pie Chart",axis='equal',show=True):
        '''

        :return:
        '''
        # need to handle sizes
        sizes = [12, 20, 15, 25, 10]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title(title)
        plt.axis(axis)
        if show is True:
            plt.show()

    def histogram(self,bins=10, show=True):
        '''

        :param bins:
        :param show:
        :return:
        '''
        plt.hist(self.df, bins=bins)
        plt.xlabel("Values")
        plt.ylabel("Frequency")
        plt.title("Histogram")
        if show is True:
            plt.show()

    def qqplot(self,array=None,line='45',show=True):
        '''

        further documentation = https://www.statsmodels.org/stable/api.html
        :param array:
        :return:
        '''
        fig = sm.qqplot(array,line=line)
        if show is True:
            plt.show()
        return fig
