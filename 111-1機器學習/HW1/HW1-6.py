import requests
from bs4 import BeautifulSoup

years = 2021
stockNo = 2330
#https://www.twse.com.tw/exchangeReport/FMSRFK?response=html&date=20210101&stockNo=2330
url = "https://www.twse.com.tw/exchangeReport/FMSRFK?response=html&date={}0101&stockNo={}".format(years,stockNo)
Response_obj = requests.get(url)

print(Response_obj.text)

web_content = BeautifulSoup(Response_obj.text,'html.parser')

print(web_content)