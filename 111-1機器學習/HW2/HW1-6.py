from socket import inet_aton
import requests
import numpy as np
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

years = 2021
stockNo = 2330
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
#https://www.twse.com.tw/exchangeReport/FMSRFK?response=html&date=20210101&stockNo=2330
url = "https://www.twse.com.tw/exchangeReport/FMSRFK?response=html&date={}0101&stockNo={}".format(years,stockNo)
Response_obj = requests.get(url,headers = headers)

web_content = BeautifulSoup(Response_obj.text,'html.parser')

trs = web_content.findAll("tr")


a2 = []

for tr in trs:
    tds = tr.find_all('td')
    a1 = []
    for td in tds:
        a1.append(td.text)
    a2.append(a1)
    
high = []
low =[]

for i in a2[2:]:
    high.append(float(i[2]))
    low.append(float(i[3]))

for i in range(0,12):
    plt.annotate(high[i], (i+1,high[i]))
    plt.annotate(low[i], (i+1,low[i]))
    
month = range(1,13)  
plt.plot(month,high,label="Highest",color="red")
plt.plot(month,low,label="Lowest",color="green")
plt.xlabel("month")
plt.ylabel("price")
plt.legend(loc='best')
plt.show()