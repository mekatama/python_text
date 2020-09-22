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
temp = kakaku.text
tousin01 = int(temp.replace(",",""))

#短期豪ドル債オープン（毎月分配型）
load_url = "https://kakaku.com/fund/detail.asp?si_isin=JP90C0002M09"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
kakaku = soup.find("span",class_="price")
temp = kakaku.text
tousin02 = int(temp.replace(",",""))
print(tousin02)

#ダイワ・グローバルＲＥＩＴ・オープン（毎月分配型）
load_url = "https://kakaku.com/fund/detail.asp?si_isin=JP90C0003PX5"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
kakaku = soup.find("span",class_="price")
temp = kakaku.text
tousin03 = int(temp.replace(",",""))
print(tousin03)

#ダイワ・グローバル債券ファンド（毎月分配型）
load_url = "https://kakaku.com/fund/detail.asp?si_isin=JP90C0003LQ8"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
kakaku = soup.find("span",class_="price")
temp = kakaku.text
tousin04 = int(temp.replace(",",""))
print(tousin04)

#エマージング・ボンド・ファンド・円コース（毎月分配型）
load_url = "https://kakaku.com/fund/detail.asp?si_isin=JP90C0006AW2"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
kakaku = soup.find("span",class_="price")
temp = kakaku.text
tousin05 = int(temp.replace(",",""))
print(tousin05)

#ダイワ先進国リートα　為替ヘッジなし（毎月分配型）
load_url = "https://kakaku.com/fund/detail.asp?si_isin=JP90C0008G43"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
kakaku = soup.find("span",class_="price")
temp = kakaku.text
tousin06 = int(temp.replace(",",""))
print(tousin06)

#ツインアクセル（ブラジル国債＆オーストラリア小型株式）
load_url = "https://kakaku.com/fund/detail.asp?si_isin=JP90C000AQQ6"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
kakaku = soup.find("span",class_="price")
temp = kakaku.text
tousin07 = int(temp.replace(",",""))
print(tousin07)

#ダイワ・ブラジル・レアル債α（毎月分配型）－スーパー・ハイインカム－　α１００コース
load_url = "https://kakaku.com/fund/detail.asp?si_isin=JP90C000BBX2"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
kakaku = soup.find("span",class_="price")
temp = kakaku.text
tousin08 = int(temp.replace(",",""))
print(tousin08)

#=================================================================
#MSNから株価を取得
# 吉野家ＨＬＤＧ株価
load_url_msn = "https://www.msn.com/ja-jp/money/stockdetails/tks-9861/fi-a9j1fr"
html = requests.get(load_url_msn)
soup = BeautifulSoup(html.content, "html.parser")
topstories = soup.find("span", class_="currentval")
temp = topstories.text
kabuka_yosinoya = int(temp.replace(",",""))
#print(kabuka_yosinoya)

# ビックカメラ株価
load_url_msn = "https://www.msn.com/ja-jp/money/stockdetails/tks-3048/fi-a9c2lh"
html = requests.get(load_url_msn)
soup = BeautifulSoup(html.content, "html.parser")
topstories = soup.find("span", class_="currentval")
temp = topstories.text
kabuka_biccamera = int(temp.replace(",",""))
#print(kabuka_biccamera)

# フジ日本精糖株価
load_url_msn = "https://www.msn.com/ja-jp/money/stockdetails/tks-2114/fi-a9b7mw"
html = requests.get(load_url_msn)
soup = BeautifulSoup(html.content, "html.parser")
topstories = soup.find("span", class_="currentval")
temp = topstories.text
kabuka_fnihonseitou = int(temp.replace(",",""))
#print(kabuka_fnihonseitou)

# イオン株価
load_url_msn = "https://www.msn.com/ja-jp/money/stockdetails/tks-8267/fi-a9ho6h"
html = requests.get(load_url_msn)
soup = BeautifulSoup(html.content, "html.parser")
topstories = soup.find("span", class_="currentval")
temp = topstories.text
kabuka_aeon = int(temp.replace(",",""))
#print(kabuka_aeon)

# 飯田グループHLDG株価
load_url_msn = "https://www.msn.com/ja-jp/money/stockdetails/tks-3291/fi-a9cf6h"
html = requests.get(load_url_msn)
soup = BeautifulSoup(html.content, "html.parser")
topstories = soup.find("span", class_="currentval")
temp = topstories.text
kabuka_iida = int(temp.replace(",",""))
#print(kabuka_iida)

# タカラレーベン株価
load_url_msn = "https://www.msn.com/ja-jp/money/stockdetails/tks-8897/fi-a9i53m"
html = requests.get(load_url_msn)
soup = BeautifulSoup(html.content, "html.parser")
topstories = soup.find("span", class_="currentval")
temp = topstories.text
kabuka_takaraleben = int(temp.replace(",",""))
#print(kabuka_takaraleben)

# グローセル株価
load_url_msn = "https://www.msn.com/ja-jp/money/stockdetails/tks-9995/fi-a9j72w"
html = requests.get(load_url_msn)
soup = BeautifulSoup(html.content, "html.parser")
topstories = soup.find("span", class_="currentval")
temp = topstories.text
kabuka_glosel = int(temp.replace(",",""))
#print(kabuka_glosel)

# スカイラークHLDG株価
load_url_msn = "https://www.msn.com/ja-jp/money/stockdetails/tks-3197/fi-a9car7"
html = requests.get(load_url_msn)
soup = BeautifulSoup(html.content, "html.parser")
topstories = soup.find("span", class_="currentval")
temp = topstories.text
kabuka_skylark = int(temp.replace(",",""))
#print(kabuka_skylark)

#=================================================================
#csvに保存
f = open('keizai_csv','w')
writer = csv.writer(f)
writer.writerow([
    usd,
    aud,
    eur,
    nikkei,
    dau,
    tousin01,
    tousin02,
    tousin03,
    tousin04,
    tousin05,
    tousin06,
    tousin07,
    tousin08,
    kabuka_yosinoya,
    kabuka_biccamera,
    kabuka_fnihonseitou,
    kabuka_aeon,
    kabuka_iida,
    kabuka_takaraleben,
    kabuka_glosel,
    kabuka_skylark])   #配列です
f.close()
