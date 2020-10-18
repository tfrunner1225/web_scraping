# FM FUKUOKAのヒットチャートからデータを抽出する

import requests
from bs4 import BeautifulSoup
import re

urlName = "https://fmfukuoka.co.jp/hitchart/"       # URLを指定
url = requests.get(urlName)                         # requestでWebページを取得
soup = BeautifulSoup(url.content, "html.parser")    # BeautifulSoupでHTMLを取得

# tableを取得（class名を指定）
table = soup.findAll("table", {"class":"table table-bordered hitchart_table"})[0]
# 全ての行を取得
rows = table.findAll("tr")

result = []
for row in rows:
    dataRow = row.findAll(['td', 'th'])
    resultRow = []
    for cell in dataRow:
        resultRow.append(cell.get_text())
    # print(resultRow)
    result.append(resultRow)

print(result)