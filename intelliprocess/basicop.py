import pandas as pd

df_housing=pd.read_csv('housing.csv')
df_toy=pd.read_csv('toy.csv')
df_iris=pd.read_csv('iris.csv')

def Datatype_frequency(df):
    """
    Finds the frequency of data types in the data set features
    INPUT: Pandas DataFrame Object
    Returns: A nested list that has 1st element as data type and 2nd element the count of data type 
    """
    dtypes_counts = df.dtypes.value_counts().reset_index()
    dtypes_counts.columns = ['Data Type', 'Count']
    result = dtypes_counts.values.tolist()
    print(result)
 
Datatype_frequency(df_housing)
Datatype_frequency(df_toy)
Datatype_frequency(df_iris)