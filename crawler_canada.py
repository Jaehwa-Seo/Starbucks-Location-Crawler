from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd 
import time

# x = -172.4
# y = -27.9

x = -82.47000000000037
y = 57.058799999999856

# x = -84+0.01
# y = 32+0.01

data = []

columns = ["Store Name","Street Address","Store Number","Country","Ownership Type","City","Postcode","phoneNumber","Longitude","Latitude"]

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

while x < -52.5395:
    while y < 70.1795:
        url = "https://www.starbucks.com/store-locator?map="+str(y)+","+str(x)+",13z"
        driver.get(url)
        time.sleep(2)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        if driver.execute_script("return window.__BOOTSTRAP['storeLocator']['locationState']['locations']") == None:
            driver.get(url)
            time.sleep(3)

        all_store = driver.execute_script("return window.__BOOTSTRAP['storeLocator']['locationState']['locations']")

        for i in all_store:
            name = i['name']
            address = ""
            for j in i['addressLines']:
                address += str(j) + " "
            storenumber = i['storeNumber']
            countryCode = i['address']['countryCode']
            ownershiptype = i['ownershipTypeCode']
            city = i['address']['city']
            postcode = i['address']['postalCode']
            phoneNumber = i['phoneNumber']
            longitude = i['coordinates']['longitude']
            latitude = i['coordinates']['latitude']
            data.append([name,address,storenumber,countryCode,ownershiptype,city,postcode,phoneNumber,longitude,latitude])
        print("-------------------------------------------------------------------")
        print(str(y) + "," + str(x))
        print(len(data))
        y += 0.3

        df = pd.DataFrame(data,columns= columns)

        df.to_csv("starbucks_store_info_canada_11.csv")

        # df.drop_duplicates(['매장번호'],keep = 'first',inplace=True)

        # writer = pd.ExcelWriter('starbucks_store_info.xlsx',engine="xlsxwriter")

        # df.to_excel(writer, sheet_name='starbucks')

        # writer.save()
    x += 0.3
    y = 41.7588







