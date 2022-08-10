from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd 
import time

x = -180+0.01
y = -90+0.01

data = []

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

while x < 180:
    y = -90+0.01
    while y < 90:
        url = "https://www.starbucks.com/store-locator?map="+str(y)+","+str(x)+",10z"
        driver.get(url)
        time.sleep(1)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        all_store = driver.execute_script("return window.__BOOTSTRAP['storeLocator']['locationState']['locations']")

        for i in all_store:
            name = i['name']
            address = str(i['address']['streetAddressLine1']) + str(i['address']['streetAddressLine2']) + str(i['address']['streetAddressLine3'])
            storenumber = i['storeNumber']
            data.append([name,address,storenumber])

        y += 1
    x += 1




columns = ["매장명","주소","매장번호"]
df = pd.DataFrame(data,columns= columns)
writer = pd.ExcelWriter('starbucks_store_info.xlsx',engine="xlsxwriter")


df.to_excel(writer, sheet_name='starbucks')

writer.save()



