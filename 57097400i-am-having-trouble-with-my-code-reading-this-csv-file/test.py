import pandas as pd 

data = pd.read_csv("nani.csv", encoding='latin-1', index_col = 'Team')
data.fillna('None', inplace=True)

print(data.head())