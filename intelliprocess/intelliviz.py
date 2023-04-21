import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import datetime


class IntelliVizError(Exception):
    pass


class IntelliViz():
    '''
    class for data visualization methods
    :param df: pandas dataframe
    '''
    def __init__(self, df=None):
        '''
        The constructor for IntelliViz class.
        :param df: pandas dataframe
        :return: instance of IntelliViz object
        '''

        if df is not None:
            self.df = df
        else:
            raise IntelliVizError("No pandas dataframe has been provided.")

    def __str__(self):
        '''
        string method which returns self.df as a string using pandas to_string() function
        :return: string
        '''
        df_string = self.df.to_string()
        return df_string


    def get_columns(self):
        '''
        This function returns the column names of the dataframe.
        :return: list of column names
        '''

        columns = self.df.columns
        return columns


    def get_df(self):
        '''
        This function returns the dataframe itself (self.df).
        :return: pandas dataframe (self.df)
        '''
        df = self.df
        return df


    def set_df(self, df=None):
        '''
        This function updates the self.df attribute
        :param df: pandas dataframe
        :raises IntelliVizError: If df is None.
        :return: None
        '''
        if df is not None:
            self.df = df
        else:
            raise IntelliVizError("No pandas dataframe provided.")

    def get_df_numeric(self):
        '''
        function to extract only numerical dtypes from a dataframe (self.df) and
        returns a dataframe of the extracted series with only numerical dtypes
        :return: pandas dataframe
        '''
        # ensure updated dtypes (redo auto-detect)
        df = pd.DataFrame(self.df)
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        df_numeric = df.select_dtypes(include=numerics)
        return df_numeric

    def pearsons_r(self,x,y):
        '''
        this function calculates the Pearson's correlation coefficient (Pearson's r)
        r = Σ[(x_i - µx)(y_i - µy)] / √[Σ(x_i - µx)^2 * Σ(y_i - µy)^2]
        Measures the linear relationship between two continuous variables. It ranges from -1 to 1.
        :param x:
        :param y:
        :return:
        '''
        # convert to numpy arrays with float type 32 to increase speed
        x, y = np.array(x, dtype="float32"), np.array(y,dtype="float32")

        # calculate numerator
        mean_x, mean_y = np.mean(x), np.mean(y)
        x_deviation_from_mean, y_deviation_from_mean = x - mean_x, y - mean_y
        numerator = np.sum(x_deviation_from_mean * y_deviation_from_mean)

        # calculate denominator
        x_deviation_from_mean_sqrd = x_deviation_from_mean ** 2
        y_deviation_from_mean_sqrd = y_deviation_from_mean ** 2
        denominator = np.sqrt((np.sum(x_deviation_from_mean_sqrd) *
                               np.sum(y_deviation_from_mean_sqrd)))

        # calculate Pearson's r
        r = numerator / denominator

        return r


    def pearson_corr_matrix(self):
        '''
        Calculutes and creates a pearson coorelation matrix
        :return: pandas dataframe
        '''

        df2 = self.get_df_numeric()
        # create an empty dataframe for our correlation matrix
        corr_matrix = pd.DataFrame(columns=df2.columns,index=df2.columns)
        # iterate over rows
        for rowIndex, row in corr_matrix.iterrows():
            for columnIndex, value in row.items():
                corr_matrix.at[columnIndex, rowIndex] = self.pearsons_r(df2[columnIndex],df2[rowIndex])

        final_df = pd.DataFrame(corr_matrix, dtype="float64")
        return final_df



    def correlation_matrix_heatmap(self, colors='coolwarm',
                                   show_values=False,
                                   save=False,
                                   filename="intelliviz_correlation_matrix_heatmap"):
        '''
        This code creates a heatmap dataset using pandas DataFrame, calculates the
        correlation matrix, and then uses matplotlib to create .
        :param colors:
        :raises: IntelliVizError if no pandas dataframe has been provided
        :return: None
        '''

        # should I add a save functionality?
        if self.df is not None:
            # Compute the correlation matrix
            corr_matrix = self.pearson_corr_matrix()
            corr_matrix.convert_dtypes()

            # Create a heatmap of the correlation matrix
            num_columns = len(self.df.columns)
            fig_scale_factor = num_columns / 5
            if fig_scale_factor < 5.0:
                fig_scale_factor = 5.0
            fig, ax = plt.subplots(figsize=(fig_scale_factor,fig_scale_factor))
            cax = ax.matshow(corr_matrix, cmap=colors)

            # Add colorbar and axis labels
            fig.colorbar(cax)
            ax.set_xticks(np.arange(len(corr_matrix.columns)))
            ax.set_yticks(np.arange(len(corr_matrix.columns)))
            ax.set_xticklabels(corr_matrix.columns)
            ax.set_yticklabels(corr_matrix.columns)

            # Rotate the x-axis labels
            plt.xticks(rotation=90)
            if show_values is True:
                # Add correlation values to each square in the heatmap
                for i in range(len(corr_matrix.columns)):
                    for j in range(len(corr_matrix.columns)):
                        ax.text(j, i, round(corr_matrix.iloc[i, j], 2),
                                       ha="center", va="center", color="black", fontsize=12)
            # save figure to working directory if save is True using timestamp for filename uniqueness
            if save is True:
                timestamp = str(datetime.datetime.now()).replace(" ", "_")
                filename = filename + "_" + timestamp + ".png"
                plt.savefig(filename,dpi=400)

            plt.show()

            return fig, ax

        else:
            raise IntelliVizError("No pandas dataframe has been provided.")


    def coefficient_of_determination(self, x, y):
        '''
        This functions calculates the coefficient of determination (R²)
        specificly for simple linear regressions.
        :param x:
        :param y:
        :return:
        '''

        r = self.pearsons_r(x, y)
        r_squared = r ** 2
        return r_squared

    def boxplot(self,save=False,
                filename="intelliviz_boxplot"):
        '''
        creates a boxplot of all numerical dtypes in a dataframe (self.df)
        :param save:
        :param filename:
        :return:
        '''

        # extract only numeric values for inclusion into the boxplot
        df_numeric = self.get_df_numeric()

        # reverse the order so that columns are in order from top to bottom
        reversed_columns = df_numeric.columns[::-1]
        reversed_data = df_numeric[reversed_columns]

        # created scales based on number of columns
        num_columns = len(reversed_data)
        fig_scale_factor = num_columns / 10
        if fig_scale_factor < 5.0:
            fig_scale_factor = 5.0
        # create the boxplot
        # do we want to be able to select columns to include or just include all? git issue #13
        fig, ax = plt.subplots(figsize=(10,fig_scale_factor))
        ax.boxplot(reversed_data, labels=reversed_columns, vert=False)
        plt.title("Boxplot")
        plt.xlabel("Columns")
        plt.xticks(rotation=90)
        plt.ylabel("Values")


        if save is True:
            timestamp = str(datetime.datetime.now()).replace(" ", "_")
            filename = filename + "_" + timestamp + ".png"
            plt.savefig(filename, dpi=400)

        plt.show()

        return fig, ax

    def columns_scatter(self,target_var=None):
        '''
        This function creates scatter plots of each variable against the target variable.
        :param target_var: A string representing the target variable.
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

    def qqplot(self,array=None, line_type='45',show=True):
        '''
        This function creates a QQ plot of the data using statsmodels.
        further documentation = https://www.statsmodels.org/stable/api.html
        :param array: An array-like object representing the data to be plotted.
        :param line: A string representing the line to be plotted on the QQ plot.
        :param show: A boolean representing whether or not to display the plot.
        :return: fig (statsmodels QQPlot): The statsmodels QQPlot object representing the plot.
        '''
        if array is None:
            print("Please provide an array-like object to be plotted.")
            return

        fig = sm.qqplot(array,line=line_type)
        if show is True:
            plt.show()
        return fig

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




