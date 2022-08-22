import pandas as pd 


df = pd.read_csv('./csv/canada.csv')

print(df.duplicated('Store Number').count)

df.drop_duplicates(['Store Number'],keep = 'first',inplace=True)

df.to_csv("./csv/canada.csv",index=False)

# print(df)