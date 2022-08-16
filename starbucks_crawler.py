from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd 
import time

x = -78+0.01
y = -6+0.01

# x = -84+0.01
# y = 32+0.01

data = []

columns = ["Store Name","Street Address","Store Number","Country","Ownership Type","City","Postcode","phoneNumber","Longitude","Latitude"]

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

while x < 147:
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
        y += 1

        df = pd.DataFrame(data,columns= columns)

        df.to_csv("starbucks_store_info.csv")

        # df.drop_duplicates(['매장번호'],keep = 'first',inplace=True)

        # writer = pd.ExcelWriter('starbucks_store_info.xlsx',engine="xlsxwriter")

        # df.to_excel(writer, sheet_name='starbucks')

        # writer.save()
    x += 1
    y = -32+0.01







