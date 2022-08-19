import pandas as pd 


df = pd.read_csv('./starbucks_store_info_america_3.csv')

print(df.duplicated('Store Number').count)

df.drop_duplicates(['Store Number'],keep = 'first',inplace=True)

df.to_csv("./starbucks_store_info_america_3.csv",index=False)

# print(df)