# ZEN-NOH COUNTDOWN JAPANのヒットチャートからデータを抽出する

import requests
from bs4 import BeautifulSoup
import re
import csv
import datetime

urlName = "https://www.tfm.co.jp/cdj/"             # URLを指定
url = requests.get(urlName)                         # requestでWebページを取得
soup = BeautifulSoup(url.content, "html.parser")    # BeautifulSoupでHTMLを取得

# div要素を取得して elems に格納
# class名を"even cleafix", "odd cleafix"に指定
elems = soup.find_all("div", {"class":["even cleafix", "odd cleafix"]})
# print(elems)

# elemの中からclass名（rank, song）のli要素を取得
# songのliは"曲名 ／ アーティスト名"であるため分割して格納
result = []
for elem in elems:  
    li = elem.find_all("li", {"class":{"rank","song"}})
    # print(li)
    row = []
    for l in li:
        c = l.get("class").pop(0)
        if c == "rank":
            row.append(l.get_text())
        elif c == "song":
            t = l.get_text().split(" ／ ")
            row = row + t
    # print(row)
    result.append(row)

# 最終結果をcsvとして出力
file = open('./web_scraping/zen-noh_{}.csv'.format(datetime.date.today()), 'w')
w = csv.writer(file)
w.writerows(result)
file.close()
# print(result)

