import pandas as pd 
from googletrans import Translator

trans = Translator()


df = pd.read_csv('./csv/test4.csv')
# storename = trans.translate("시험")

# print(storename.text)
for index,row in df.iterrows():
    print(index)
    if index >= 2160:
        storename = trans.translate(row[2], dest="en")
        streetaddress = trans.translate(row[3], dest="en")
        city = trans.translate(row[7], dest="en")

        df["Store Name"][index] = storename.text
        df["Street Address"][index] = streetaddress.text
        df["City"][index] = city.text

        df.to_csv("./csv/test5.csv",index=False)


