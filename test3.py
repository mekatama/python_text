import requests
import json
import csv
from bs4 import BeautifulSoup

#=================================================================
#価格.comから投信系を取得
#カナダ高配当株ツインα（毎月分配型）
load_url = "https://kakaku.com/fund/detail.asp?si_isin=JP90C00092Z0"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
kakaku = soup.find("span",class_="price")
temp = kakaku.text
tousin01 = int(temp.replace(",",""))
print(tousin01)

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

