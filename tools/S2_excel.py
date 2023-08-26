# pandas 操作 excel

import pandas as pd

df = pd.read_excel('test.xlsx')
print(df.shape)
print(df.columns.values)
print(df.index.values)
print(df.loc[0]["First Name"])
df.loc[0,"First Name"] = 'Anna'
#df['First Name'][2] = 'Anna'
#df['Location'] = [1,2,3,4,5,6,7,8,9]
print(df)
df.to_excel("test2.xlsx")
