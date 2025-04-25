import pandas as pd
df = pd.DataFrame({
    'artist': ['A', 'A', 'B', 'A', 'C', 'B'],
    'venue': ['X', 'Y', 'X', 'X', 'Y', 'X'],
    'date': pd.to_datetime([
        '2022-01-05', '2022-01-10', '2022-01-15',
        '2022-02-01', '2022-01-20', '2022-02-25'
    ])
})
df['month']=df['date'].dt.to_period('M')
counts=df.groupby(['month','artist','venue']).size().reset_index(name='count')
wide=counts.pivot_table(index='month',columns=['artist','venue'],values='count',fill_value=0)
print(wide)