import pandas as pd 


df = pd.read_csv('./another.csv')

df.drop_duplicates(['Country'],keep = 'first',inplace=True)

print(df['Country'])


df.to_csv("country.csv")
# print(df)