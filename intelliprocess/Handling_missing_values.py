import pandas as pd

df=pd.read_csv('Testing_Datasets\\BreastCancer.csv')

k=df.isnull()
print(k)