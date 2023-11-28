import pandas as pd

df = pd.read_csv('d:\house.csv')

print(df.to_string()) 
print(df.dropna())
