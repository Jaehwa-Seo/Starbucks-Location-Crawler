from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd 
import time

x = -124+0.01
y = -32+0.01

# x = -84+0.01
# y = 32+0.01

data = []

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

while x < 147:
    y = -32+0.01
    while y < 54:
        url = "https://www.starbucks.com/store-locator?map="+str(y)+","+str(x)+",10z"
        driver.get(url)
        time.sleep(2)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        all_store = driver.execute_script("return window.__BOOTSTRAP['storeLocator']['locationState']['locations']")

        for i in all_store:
            name = i['name']
            address = str(i['address']['streetAddressLine1']) +" "+ str(i['address']['streetAddressLine2']) +" "+ str(i['address']['streetAddressLine3'])
            storenumber = i['storeNumber']
            countryCode = i['address']['countryCode']
            data.append([name,address,storenumber,countryCode])
        print("-------------------------------------------------------------------")
        print(str(y) + "," + str(x))
        print(len(data))
        y += 1
    x += 1




columns = ["매장명","주소","매장번호","국가"]
df = pd.DataFrame(data,columns= columns)
writer = pd.ExcelWriter('starbucks_store_info.xlsx',engine="xlsxwriter")


df.to_excel(writer, sheet_name='starbucks')

writer.save()



