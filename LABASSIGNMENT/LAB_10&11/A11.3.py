import pandas as pd
l=list(map(int,input("").split()))
p=list(map(int,input("").split()))
asking = pd.Series (l)
paid = pd.Series (p)
good=asking.where(asking<paid).dropna().index.tolist()
print(good)