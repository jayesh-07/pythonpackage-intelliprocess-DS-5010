import pandas as pd
import matplotlib.pyplot as plt

df_housing=pd.read_csv('housing.csv')
df_toy=pd.read_csv('toy.csv')
df_iris=pd.read_csv('iris.csv')

def datatype_frequency(df):
    """
    Finds the frequency of data types in the data set features
    INPUT: Pandas DataFrame Object
    Returns: A nested list that has 1st element as data type and 2nd element the count of data type 
    """
    dtypes_counts = df.dtypes.value_counts().reset_index()
    dtypes_counts.columns = ['Data Type', 'Count']
    result = dtypes_counts.values.tolist()
    print(result)
 
datatype_frequency(df_housing)
datatype_frequency(df_toy)
datatype_frequency(df_iris)

print("\n")

def feature_type_frequency(df):
    """
    Finds the frequency of categorical or numerical features.
    INPUT:Data Frame
    Return:A bar plot of categorical and numerical features.
    """
    categorical_count = 0
    numerical_count = 0
    for column in df.columns:
        if df[column].dtype == 'object' or pd.api.types.is_categorical_dtype(df[column].dtype):
            categorical_count += 1
        elif pd.api.types.is_numeric_dtype(df[column].dtype):
            numerical_count += 1
    features=["Categorical","Numerical"]
    values=[categorical_count,numerical_count]
    plt.bar(features,values)
    plt.title("Feature Type Frequency Plot")
    plt.show()

feature_type_frequency(df_housing)
feature_type_frequency(df_toy)
feature_type_frequency(df_iris)