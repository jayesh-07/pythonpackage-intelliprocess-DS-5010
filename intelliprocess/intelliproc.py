import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import csv
import os
import datetime

class IntelliProcessError(Exception):
    pass

class IntelliProcess:
    '''

    '''
    def __init__(self, data=None):
        # try loading as dataframe
        if data is not None:
            self.data = pd.DataFrame(data)
        else:
            raise IntelliProcessError("No pandas dataframe has been provided.")

    def __str__(self):
        """
        String method which returns a string version of
        an instance of self.
        :return: string
        """
        data_string = self.data.to_string()
        return data_string

    def __setitem__(self, key, value):
        """
        Sets the key and value for a given instance of self.
        :param key: an entry for the key identifier.
        :param value: an entry for the value of the given key.
        :return: None
        """
        self.data[key] = value
        return None

    def __getitem__(self, key):
        """
        Returns an instance of self.
        :param key: the given key value
        :return: instance of self
        """
        return self.data[key]

    def column_list(self):
        """
        Creates a list of column names for a given dataset.
        :param data: a pandas data frame
        :return:a list of the data's column names
        """
        columns_names = self.data.columns
        column_names_list = columns_names.tolist()
        return column_names_list

    def get_data(self):
        """
        Returns an instance of a pandas data frame.
        :return: instance of a pandas data frame
        """
        data = self.data
        return data

    def set_data(self, data=None):
        """
        Updates an instance of self.
        :param data: pandas data frame
        :return: None
        """
        if data is not None:
            self.data = data
        else:
            raise IntelliProcessError("No pandas dataframe provided.")

    def select_num(self):
        """
        Creates a subset of a given dataset, sampling
        only the numeric variables.
        :return:a pandas data frame containing all columns
        in which numeric values are identified.
        """
        data = self.data.copy()
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        data_numeric = data.select_dtypes(include=numerics)
        return data_numeric

    def run_process(self):
        '''
        function that will run all of the code
        :return:
        '''
        pass

    def nan_frequency(self):
        """
        Finds the frequency of NaN values in the data set.
        :return: A nested list that has 1st element as feature name and
        2nd element the count of NaN Values.
        If no NaN values present returns an empty list.
        """
        df = self.data.copy()
        nan_counts = df.isna().sum()
        if nan_counts.sum() == 0:
            print("NO NaN VALUES IN DATA SET")
            k = []
            return (k)
        else:
            nan_frequency_list = [[col_name, nan_counts[col_name]] for col_name in nan_counts.index]

            # Create a horizontal bar chart using Matplotlib
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.barh([item[0] for item in nan_frequency_list], [item[1] for item in nan_frequency_list])
            ax.set_xlabel('Frequency of NaN Values')
            ax.set_title('NaN Value Frequency')
            plt.show()

            return nan_frequency_list

    def fill_missing_values(self):
        """
        Checks for NA values and replaces them with imputed
        values based on the data type of the column.
        :return: df: data frame with imputed values
        """
        df = self.data.copy()
        # Loop through each column of the DataFrame
        for column in df.columns:

            # Check the data type of the column
            dtype = str(df[column].dtype)

            # If the column is numeric or boolean
            if dtype.startswith('float') or dtype.startswith('int') or dtype == 'bool':

                # Fill missing values with the mean of the column
                mean = df[column].mean()
                df[column] = df[column].fillna(mean)

            # If the column is categorical
            elif dtype == 'category':

                # Fill missing values with the mean of the column
                mean = df[column].mean()
                df[column] = df[column].fillna(mean)

            # If the column is a string or object
            elif dtype.startswith('str') or dtype.startswith('object'):

                # Fill missing values with the most common value of the column
                most_common = df[column].value_counts().index[0]
                df[column] = df[column].fillna(most_common)

            # If the column is a datetime or timedelta
            elif dtype.startswith('datetime') or dtype.startswith('timedelta'):

                # Fill missing values with the mean of the column
                mean = df[column].mean()
                df[column] = df[column].fillna(mean)

            # If the column is any other data type
            else:

                # Fill missing values with the mean of the column
                mean = df[column].mean()
                df[column] = df[column].fillna(mean)

        # should prob add option to save this to self.data and output as csv

        return df

    def datatype_frequency(self):
        """
        Finds the frequency of data types in the data set features.
        :return: A nested list that has 1st element as data type
        and 2nd element the count of data type.
        """
        df = self.data.copy()
        dtypes_counts = df.dtypes.value_counts().reset_index()
        dtypes_counts.columns = ['Data Type', 'Count']
        result = dtypes_counts.values.tolist()

        # Create a bar plot using Matplotlib
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.bar([str(item[0]) for item in result], [item[1] for item in result])
        ax.set_xlabel('Data Type')
        ax.set_ylabel('Count')
        ax.set_title('Data Type Frequency')
        plt.show()
        return result

    def feature_type_frequency(self):
        """
        Finds the frequency of categorical or numerical features.
        :return: A nested list with 1st element
        as the type of variable. (Categorical/Numerical) and 2nd
        element as the count of the variable.
        """
        df = self.data.copy()
        categorical_count = 0
        numerical_count = 0
        for column in df.columns:
            if df[column].dtype == 'object' or pd.api.types.is_categorical_dtype(df[column].dtype):
                categorical_count += 1
            elif pd.api.types.is_numeric_dtype(df[column].dtype):
                numerical_count += 1
        features = ["Categorical", "Numerical"]
        values = [categorical_count, numerical_count]
        plt.bar(features, values)
        plt.title("Feature Type Frequency Plot")
        plt.show()
        result = []
        for i in range(len(features)):
            temp = []
            temp.append(features[i])
            temp.append(values[i])
            result.append(temp)
        return (result)

    def suggest_encoding(self):
        """
        Suggests the appropriate encoding method to use for the data.

        Returns:
            str: The suggested encoding method ('label', 'one-hot', or 'binary').
        """
        categorical_cols = []
        numeric_cols = []

        for col in self.data.columns:
            if isinstance(self.data[col][0], str):
                categorical_cols.append(col)
            else:
                numeric_cols.append(col)

        if len(categorical_cols) == 0:
            print("All columns are numeric. No encoding required.")
            return None

        elif len(categorical_cols) == 1:
            print("Single categorical column found. Suggesting Label Encoding.")
            return 'label'

        else:
            num_unique_vals = self.data[categorical_cols].apply(set).apply(len)
            if (num_unique_vals / len(self.data)).mean() >= 0.5:
                print("Many categorical columns found. Suggesting One-Hot Encoding.")
                return 'one-hot'
            else:
                print("Few categorical columns found. Suggesting Binary Encoding.")
                return 'binary'

    def encode_data(self, encoding_type):
        """
        Encodes the data using the specified encoding method.

        Parameters:
            encoding_type (str): The encoding method to use ('label', 'one-hot', or 'binary').

        Returns:
            pandas.DataFrame: The encoded data.
        """
        if encoding_type == 'label':
            encoded_data = self.data.copy()
            label_encoders = {}
            for col in encoded_data.columns:
                if isinstance(encoded_data[col][0], str):
                    labels = list(set(encoded_data[col]))
                    label_encoders[col] = {label: idx for idx, label in enumerate(labels)}
                    encoded_data[col] = encoded_data[col].apply(lambda x: label_encoders[col][x])
            print("Label Encoding successful.")
            return encoded_data

        elif encoding_type == 'one-hot':
            encoded_data = []
            for col in self.data.columns:
                if isinstance(self.data[col][0], str):
                    labels = list(set(self.data[col]))
                    for label in labels:
                        new_col = [int(x == label) for x in self.data[col]]
                        encoded_data.append(new_col)
                else:
                    encoded_data.append(list(self.data[col]))
            encoded_data = pd.DataFrame(encoded_data).transpose()
            print("One-Hot Encoding successful.")
            return encoded_data

        elif encoding_type == 'binary':
            encoded_data = self.data.copy()
            for col in encoded_data.columns:
                if isinstance(encoded_data[col][0], str):
                    labels = list(set(encoded_data[col]))
                    for label in labels:
                        new_col = [int(x == label) for x in encoded_data[col]]
                        new_col_name = col + '_' + label
                        encoded_data[new_col_name] = new_col
                    encoded_data = encoded_data.drop(col, axis=1)
            print("Binary Encoding successful.")
            return encoded_data

        else:
            print("Invalid encoding type.")
            return None

    # Outlier Detection and Removal
    # Enables IQR method
    def outlier_removal_IQR_method(self, save=True, filename="intelliprocess_outliers_iqr_file"):
        """
        Removes outliers based on inter quartile range
        and provides a csv file output.
        :return: updated_data: a new csv file with outlier
        observations removed.
        """
        data_numeric = self.data.copy()
        Q3 = data_numeric.quantile(0.75)
        Q1 = data_numeric.quantile(0.25)
        IQR = (Q3 - Q1)

        updated_data = data_numeric[~(
                (data_numeric < (Q1 - 1.5 * IQR)) | (data_numeric > (Q3 + 1.5 * IQR)))]

        if save is True:
            timestamp = str(datetime.datetime.now()).replace(" ", "")
            filename = filename + "" + timestamp + ".csv "
            updated_data.to_csv(filename)

        # potentially add option to save
        return updated_data

    def select_x(self, x_name):
        """
        Creates a subset containing a single variable in a
        given dataset, when provided the dataset's
        filepath and column name of the chosen variable.
        :param x_name: string indicating the name of
        the requested column to subset.
        :return:data frame of data subset
        """
        data = self.select_num()
        df = data[x_name].copy().to_numpy()
        return df

    def skew(self):
        """
        Creates an associative array containing all column
        names of a given dataset and their calculated
        Fisher-Pearson skew value.
        :return:skewness: a dictionary containing the
        column names as keys and associated skewness numbers
        as values.
        """
        data_numeric = self.select_num()
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

    def scaling_box_cox(self, x_column):
        """
        Transforms a single column of values based on
        a fitted lambda value and provides two plots, one of the
        original data and one of the transformed.
        :param x_column: a subset of a single variable
        from a given dataset
        :return: transformed: transformed data
        """
        transformed, fitted_lambda = stats.boxcox(x_column)
        fig, axes = plt.subplots(1, 2)

        sns.histplot(x_column, kde=True, ax=axes[0],
                     label="Original Data", color="black")
        sns.histplot(transformed, kde=True, ax=axes[1],
                     label="Transformed Data", color="black")
        print(f"Lambda value used for Transformation: {fitted_lambda}")
        plt.show()
        return transformed


    # Log Transformation for a Given Column
    # Progressing - Incomplete
    # incorporate with scatterplot fcn (shane)
    def scaling_log(self, x_column):
        """
        Transforms a single column of values based on
        a log base 10 and provides two plots, one of the
        original data and one of the transformed.
        :param x_column: a subset of a single variable
        from a given dataset.
        :return: data_output:data frame of transformed data.
        """
        values = np.log10(x_column)
        data_output = pd.DataFrame(values)
        fig, axes = plt.subplots(1, 2)

        sns.histplot(x_column, kde=True, ax=axes[0],
                     label="Original Data", color="black")
        sns.histplot(data_output, kde=True, ax=axes[1],
                     label="Transformed Data", color="black")
        plt.show()
        return data_output


