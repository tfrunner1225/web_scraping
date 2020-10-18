# CDTVサタデー！のヒットチャートからデータを抽出する

import requests
from bs4 import BeautifulSoup
import re
import csv
import datetime

urlName = "https://www.tbs.co.jp/cdtv/"             # URLを指定
url = requests.get(urlName)                         # requestでWebページを取得
soup = BeautifulSoup(url.content, "html.parser")    # BeautifulSoupでHTMLを取得

# tableを取得
table = soup.findAll("table")[0]
# 全ての行を取得
rows = table.findAll("tr")

# 各行に対してデータを抽出→リストへの格納
result = [] # 最終結果格納用のリスト
for row in rows:
    dataRow = row.findAll('td')
    resultRow = []
    for cell in dataRow:
        resultRow.append(cell.get_text())
    # print(resultRow)
    result.append(resultRow)

# 最終結果をcsvとして出力
file = open('./web_scraping/cdtv_{}.csv'.format(datetime.date.today()), 'w')
w = csv.writer(file)
w.writerows(result)
file.close()