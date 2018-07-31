import pandas as pd 


input=pd.read_csv("36kr.csv")
print(input.info())
print(input.iloc[:,3])
