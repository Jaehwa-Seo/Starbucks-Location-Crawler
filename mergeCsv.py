import pandas as pd

df = pd.read_csv('./seoul1.csv')

allData = []

allData.append(df)

df2 = pd.read_csv('./starbucks_store_info_seoul_2.csv')

allData.append(df2)

dataCombine = pd.concat(allData, axis=1, ignore_index = True)

# dataCombine = (dataCombine.sum(axis=1))/3

dataCombine.to_csv("./seoul.csv",index = False)