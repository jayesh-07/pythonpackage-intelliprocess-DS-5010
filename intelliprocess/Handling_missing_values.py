import pandas as pd
import numpy as np

def fill_missing_values(df, method='mean'):
    """
    Iterates through the columns of a DataFrame, checks for NaN values, and replaces them with either the mean or mode
    of the column, depending on the user's choice. Handles all data types including numeric, boolean, categorical,
    string, datetime, and timedelta.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame to be filled with missing values.
    method (str): The method used to fill the missing values. Can be 'mean' or 'mode'. Defaults to 'mean'.
    
    Returns:
    pandas.DataFrame: The DataFrame with missing values filled.
    """
    
    # Loop through each column of the DataFrame
    for column in df.columns:
        
        # Check the data type of the column
        dtype = str(df[column].dtype)
        
        # If the column is numeric
        if dtype.startswith('float') or dtype.startswith('int'):
            
            # If the user selected 'mean', fill missing values with the mean of the column
            if method == 'mean':
                mean = df[column].mean()
                df[column] = df[column].fillna(mean)
            
            # If the user selected 'mode', fill missing values with the mode of the column
            elif method == 'mode':
                mode = df[column].mode()[0]
                df[column] = df[column].fillna(mode)
        
        # If the column is boolean
        elif dtype == 'bool':
            
            # Fill missing values with the mode of the column
            mode = df[column].mode()[0]
            df[column] = df[column].fillna(mode)
        
        # If the column is categorical
        elif dtype == 'category':
            
            # Fill missing values with the mode of the column
            mode = df[column].mode()[0]
            df[column] = df[column].fillna(mode)
        
        # If the column is a string or object
        elif dtype.startswith('str') or dtype.startswith('object'):
            
            # Fill missing values with the most common value of the column
            most_common = df[column].value_counts().index[0]
            df[column] = df[column].fillna(most_common)
            
        # If the column is a datetime or timedelta
        elif dtype.startswith('datetime') or dtype.startswith('timedelta'):
            
            # Fill missing values with the median of the column
            median = df[column].median()
            df[column] = df[column].fillna(median)
            
        # If the column is any other data type
        else:
            
            # Fill missing values with the mode of the column
            mode = df[column].mode()[0]
            df[column] = df[column].fillna(mode)
    
    return df