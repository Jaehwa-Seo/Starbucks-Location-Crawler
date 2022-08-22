import pandas as pd

df = pd.read_csv('./csv/singapore.csv')

index1 = df[df['Country'] != "SG"].index

df.drop(index1,inplace=True)

df.to_csv("./csv/singapore.csv",index=False)