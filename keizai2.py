import requests
import json
import csv
from bs4 import BeautifulSoup

#=================================================================
# Alpha Vantageの為替データ
# response01 = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo')
# print(response.text)    #.textで取得data表示はできる

# Alpha Vantageの為替データ jsonデータで取得
#USD
r01 = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=9C61LRH22KOSAPQO')
kawase_data01 = r01.json()
usd = kawase_data01['Realtime Currency Exchange Rate']['5. Exchange Rate']
print(usd)
#AUD
r03 = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=AUD&to_currency=JPY&apikey=9C61LRH22KOSAPQO')
kawase_data03 = r03.json()
aud = kawase_data03['Realtime Currency Exchange Rate']['5. Exchange Rate']
print(aud)
#EUR
r02 = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=JPY&apikey=9C61LRH22KOSAPQO')
kawase_data02 = r02.json()
eur = kawase_data02['Realtime Currency Exchange Rate']['5. Exchange Rate']
print(eur)

#=================================================================
#MSNから日経平均とダウを取得
load_url_msn = "https://www.msn.com/ja-jp/money/markets"
html = requests.get(load_url_msn)
soup = BeautifulSoup(html.content, "html.parser")
topstories = soup.find("div", class_="majorIndicesPane")
colboxindexes = topstories.find_all("div", class_="majorIndexTile")
#日経平均
aaa = colboxindexes[0].find("div",class_ = "currentPrice inline")
aaaa = aaa.text
nikkei = int(aaaa.replace(",",""))
#ダウ
bbb = colboxindexes[2].find("div",class_ = "currentPrice inline")
bbbb = bbb.text
dau = float(bbbb.replace(",",""))

#=================================================================
#価格.comから投信系を取得
#カナダ高配当株ツインα（毎月分配型）
load_url = "https://kakaku.com/fund/detail.asp?si_isin=JP90C00092Z0"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

kakaku = soup.find("span",class_="price")
temp01 = kakaku.text
tousin01 = int(temp01.replace(",",""))

# Alpha Vantageから株価を取得
# 吉野家ＨＬＤＧ株価
k01 = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=9861.T&apikey=9C61LRH22KOSAPQO')
k01a = k01.json()
kabuka_yosinoya = k01a['Global Quote']['05. price']


#=================================================================
#csvに保存
f = open('keizai_csv','w')
writer = csv.writer(f)
writer.writerow([usd,aud,eur,nikkei,dau,tousin01,kabuka_yosinoya])   #配列です
f.close()
