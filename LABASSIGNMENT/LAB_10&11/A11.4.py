import pandas as pd
df = pd.DataFrame({
    'John': [True, False, True, False, True, False, True, False, False, True],
    'Judy': [True, True, False, True, True, False, True, False, True, True]
})
df['party']=df['John']&df['Judy']
df['daystillparty']=None
for i in range(len(df)):
    count=0
    found=False
    for j in range(i,len(df)):
        if df['party'][j]:
            df.at[i,'daystillparty']=count
            found=True
            break
        count+=1
        if not found:
            df.at[i,'daystillparty']=None
print(df)            
