import pandas as pd
import numpy as np

df = pd.read_csv("test.csv")
print(df.head(10))

for index, row in df.iterrows():
    print(row['nome'], row['anni'])
    
df = pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 120]})
