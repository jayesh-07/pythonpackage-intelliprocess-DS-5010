import pandas as pd
import numpy as np

def fill_missing_values(df):
    """
    Iterates through the columns of a DataFrame, checks for NaN values, and replaces them with the mean of the column.
    Handles all data types including numeric, boolean, categorical, string, datetime, and timedelta.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame to be filled with missing values.
    
    Returns:
    pandas.DataFrame: The DataFrame with missing values filled.
    """
    
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
    
    return df
