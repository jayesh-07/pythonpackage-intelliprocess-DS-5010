import pandas as pd
import matplotlib.pyplot as plt

def datatype_frequency(df):
    """
    Finds the frequency of data types in the data set features.
    INPUT: Pandas DataFrame Object.
    Returns: A nested list that has 1st element as data type 
             and 2nd element the count of data type. 
    """
    dtypes_counts = df.dtypes.value_counts().reset_index()
    dtypes_counts.columns = ['Data Type', 'Count']
    result = dtypes_counts.values.tolist()

    # Create a bar plot using Matplotlib
    fig, ax = plt.subplots(figsize=(6,6))
    ax.bar([str(item[0]) for item in result], [item[1] for item in result])
    ax.set_xlabel('Data Type')
    ax.set_ylabel('Count')
    ax.set_title('Data Type Frequency')
    plt.show()
    return result

def feature_type_frequency(df):
    """
    Finds the frequency of categorical or numerical features.
    INPUT:Pandas DataFrame object.
    Return:A nested list with 1st element as the type of variable
           (Categorical/Numerical) and 2nd element as the count of the variable.
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
    result=[]
    for i in range(len(features)):
        temp=[]
        temp.append(features[i])
        temp.append(values[i])
        result.append(temp)
    return(result)

def nan_frequency(df):
    """
    Finds the frequency of NaN values in the data set.
    INPUT: Pandas DataFrame Object.
    Returns: A nested list that has 1st element as feature name and
             2nd element the count of NaN Values.
             If no NaN values present returns an empty list.
    """
    nan_counts = df.isna().sum()
    if nan_counts.sum() == 0:
        print("NO NaN VALUES IN DATA SET")
        k=[]
        return(k)
    else:
        nan_frequency_list = [[col_name, nan_counts[col_name]] for col_name in nan_counts.index]
        
        # Create a horizontal bar chart using Matplotlib
        fig, ax = plt.subplots(figsize=(10,6))
        ax.barh([item[0] for item in nan_frequency_list], [item[1] for item in nan_frequency_list])
        ax.set_xlabel('Frequency of NaN Values')
        ax.set_title('NaN Value Frequency')
        plt.show()

        return nan_frequency_list