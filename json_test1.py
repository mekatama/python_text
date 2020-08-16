import json #モジュール入れる

#辞書型データ作る
dict_data = {
    'user':{
        'name':'name1',
        'age':30,
    },
    'country':{
        'name':'japan',
        'city':['tokyo','osaka','nagoya']
    }
}

#jsonデータに変換
json_data = json.dumps(dict_data)   #dumps関数
print(json_data)

#ファイルに書き込む
file = open('test.json','w')    #ファイルを書き込みモードにする
json.dump(json_data,file)       #dump関数
file.close()                    #書き込み終了
