import pandas as pd 


df = pd.read_csv('./starbucks_store_info.csv')

print(df.duplicated('매장번호'))

df.drop_duplicates(['매장번호'],keep = 'first',inplace=True)

df.to_csv("test.csv")

print(df)