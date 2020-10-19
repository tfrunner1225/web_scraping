# TOKIO HOT 100のヒットチャートからデータを抽出する

import requests
from bs4 import BeautifulSoup
import re
import csv
import datetime

urlName = "https://www.j-wave.co.jp/original/tokiohot100/chart/main.htm"    # URLを指定
url = requests.get(urlName)                         # requestでWebページを取得
soup = BeautifulSoup(url.content, "html.parser")    # BeautifulSoupでHTMLを取得

rows = soup.findAll("tr",{"bgcolor":("#F2F2F2","#ffffff")})

result = []
for row in rows:
    font = row.find("font",{"color":"#cc0000"})
    # print(font)
    if font != None:
        this = font.get_text()

        font = row.find("font",{"class":"text2"})
        last = font.get_text()
        if last == "":
            last = "-"
        # print(this)
        # print(last)
        r = row.findAll("td",{"class":"text2"})
        # print(r)
        song = r[0].get_text()
        name = r[1].get_text()
        # print(song)
        # print(name)
        result.append([this,last,song,name])


# 最終結果をcsvとして出力
file = open('./web_scraping/tokio-hot_{}.csv'.format(datetime.date.today()), 'w')
w = csv.writer(file)
w.writerows(result)
file.close()
# print(result)

