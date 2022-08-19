import pandas as pd

df = pd.read_csv('./csv/allcountry.csv')

index1 = df[df['Country'] == "KR"].index

df.drop(index1,inplace=True)

df.to_csv("./csv/allcountry.csv",index=False)