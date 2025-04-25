import pandas as pd 
l=list(input("").split())
s = pd.Series (l)
for val in s:
    print(val.upper())
    print(val.lower())
    print(len(val))