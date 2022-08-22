import pandas as pd 


df = pd.read_csv('./csv/UK.csv')

df.drop_duplicates(['Country'],keep = 'first',inplace=True)

print(df['Country'])


# df.to_csv("country.csv")
# print(df)