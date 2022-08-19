import pandas as pd 
import json

df = pd.read_csv('./csv/allcountry.csv')

nftName = "Metatwin country";
description = "Description";
imgUrl = "hahahah";
totalNum = 100;



i = 0

countryCode = {"US" : "United States",
    "CA" : "Canada",
    "MX" : "Mexico",
    "GT" : "Guatemala",
    "SV" : "El Salvador",
    "CR" : "Costa Rica",
    "KY" : "Cayman Islands",
    "PE" : "Peru",
    "JM" : "Jamaica",
    "BS" : "Bahamas",
    "CO" : "Colombia",
    "CL" : "Chile",
    "PA" : "Panama",
    "TC" : "Tursk and Caicos Islands",
    "AW" : "Aruba",
    "DO" : "Dominican Republic",
    "CW" : "Curacao",
    "PR" : "Puerto Rico",
    "BO" : "Bolivia",
    "AR" : "Argentina",
    "TT" : "Trinidad and Tobago",
    "BB" : "Barbados",
    "BR" : "Brazil",
    "ES" : "Spain",
    "PT" : "Portugal",
    "IE" : "Ireland",
    "MA" : "Morocco",
    "GB" : "United Kingdom",
    "FR" : "France",
    "AD" : "Andorra",
    "BE" : "Belgium",
    "NL" : "Netherlands",
    "DE" : "Germany",
    "CH" : "Switzerland",
    "LU" : "Luxembourg",
    "MC" : "Monaco",
    "IT" : "Italy",
    "AT" : "Austria",
    "CZ" : "Czech Republic",
    "MT" : "Malta",
    "PL" : "Poland",
    "SK" : "Slovakia",
    "HU" : "Hungary",
    "GR" : "Greece",
    "RS" : "Serbia",
    "RO" : "Romania",
    "BG" : "Bulgaria",
    "TR" : "Turkey",
    "ZA" : "South Africa",
    "EG" : "Egypt",
    "CY" : "Cyprus",
    "JO" : "Jordan",
    "LB" : "Lebanon",
    "SA" : "Saudi Arabia",
    "KW" : "Kuwait",
    "AZ" : "Azerbaijan",
    "QA" : "Qatar",
    "BH" : "Bahrain",
    "AE" : "United Arab Emirates",
    "OM" : "Oman",
    "KZ" : "Kazakhstan",
    "IN" : "India",
    "ID" : "Indonesia",
    "TH" : "Thailand",
    "CN" : "China",
    "MY" : "Malaysia",
    "KH" : "Cambodia",
    "SG" : "Singapore",
    "VN" : "Viet Nam",
    "MO" : "Macau",
    "BN" : "Brunei Darussalam",
    "HK" : "Hong Kong",
    "TW" : "Taiwan",
    "PH" : "Philippines",
    "JP" : "Japan",
    "KR" : "Korea"}

# print(countryCode["KR"])

while i < len(df.index):
    jsonString = '{"name":"' + nftName + '","description":"' + description + '","image":"' + imgUrl + '","attributes":['
    jsonString += '{"trait_type" : "Country","value" : "' + countryCode[df.loc[i]["Country"]] +'"},'
    jsonString += '{"trait_type" : "City","value" : "' + df.loc[i]["City"] + '"}]}'
    fileName = "./json/"+str(i+1)+".json"

    file = open(fileName, "w")
    file.write(jsonString)
    file.close()
    i+=1



# try {
#     for (let i = 1; i <= totalNum; i++) {
#         let json = `{"name":"${nftName} #${i}","description":"${description}","image":"${hiddenImgUrl}","attributes":[{"trait_type": "Unknown","value": "Unknown"}]}`;
#         let fs = require("fs");
#         fs.writeFile(`json/${i}.json`, json, "utf8", (e)=>(e));
#     }
#     console.log("complete!");
# } catch (error) {
#     console.log(error);
# }