from socket import inet_aton
import requests
import numpy as np
from bs4 import BeautifulSoup

years = 2021
stockNo = 2330
#https://www.twse.com.tw/exchangeReport/FMSRFK?response=html&date=20210101&stockNo=2330
url = "https://www.twse.com.tw/exchangeReport/FMSRFK?response=html&date={}0101&stockNo={}".format(years,stockNo)
Response_obj = requests.get(url)

web_content = BeautifulSoup(Response_obj.text,'html.parser')

tbody = web_content.find("tbody")
tr = tbody.find_all("tr")


high = []
low = []




print(high)
print(low)

