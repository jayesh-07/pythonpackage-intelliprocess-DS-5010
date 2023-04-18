import pandas as pd

df=pd.read_csv('Testing_Datasets\\BreastCancer.csv')

print(df.shape)
print(df.info())
print(df.columns)