import requests
import json

# 'noaa_gfs_global_sflux_0.12d”は気象データのID
url = 'http://api.planetos.com/v1/datasets/noaa_gfs_global_sflux_0.12d/point'

#↓後で調べる
querystring = {
    'lat':'35.70',                  #緯度
    'lon':'139.80',                 #経度
    'var':'Temperature_surface',    #温度
    'count':'1',                   #データ取得数
    'apikey':'09c42ac4bf04441baeca7dfbc69c5ffc' #アカウントで取得したAPIキー
}

#↓後で調べる
#response = requests.request('GET',url,params=querystring )
response = requests.get(url,params=querystring)

print(response.text)    #.textで表示はできる

#ファイルに書き込む
file = open('planet.json','w')    #ファイルを書き込みモードにする
json.dump(response,file)       #dump関数
file.close()                    #書き込み終了

