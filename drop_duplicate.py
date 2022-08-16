import pandas as pd 


df = pd.read_csv('./starbucks_store_info.csv')

print(df.duplicated('Store Number'))

df.drop_duplicates(['Store Number'],keep = 'first',inplace=True)

df.to_csv("test.csv")

# print(df)