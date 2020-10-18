# FM FUKUOKAのヒットチャートからデータを抽出する
# 参考サイト：https://qiita.com/hujuu/items/b0339404b8b0460087f9

import requests
from bs4 import BeautifulSoup
import re
import csv
import datetime

urlName = "https://fmfukuoka.co.jp/hitchart/"       # URLを指定
url = requests.get(urlName)                         # requestでWebページを取得
soup = BeautifulSoup(url.content, "html.parser")    # BeautifulSoupでHTMLを取得

# tableを取得（class名を指定）
table = soup.findAll("table", {"class":"table table-bordered hitchart_table"})[0]
# 全ての行を取得
rows = table.findAll("tr")

result = [] # 最終結果格納用のリスト
# 各行に対してデータを抽出→リストへの格納
for row in rows:
    dataRow = row.findAll(['td', 'th'])
    resultRow = []
    for cell in dataRow:
        resultRow.append(cell.get_text())
    # print(resultRow)
    result.append(resultRow)

# 最終結果をcsvとして出力
file = open('./web_scraping/fmfukuoka_{}.csv'.format(datetime.date.today()), 'w')
w = csv.writer(file)
w.writerows(result)
file.close()
# print(result)