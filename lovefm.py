# Love FM Top 40のヒットチャートからデータを抽出する

import requests
from bs4 import BeautifulSoup
import re
import csv
import datetime

urlName = "https://lovefm.co.jp/top_forties"        # URLを指定
url = requests.get(urlName)                         # requestでWebページを取得
soup = BeautifulSoup(url.content, "html.parser")    # BeautifulSoupでHTMLを取得

# tableを取得
table = soup.findAll("table", {"class":"top40"})[0]
rows = table.findAll("tr")

for i in range(2):
    row = rows[i]
    td = row.findAll("td", {"class":"music"})
    if len(td) != 0:
        # print(len(td))
        # print(td[0])
        [s, n] = td[0].findAll("li")
        song = s.get_text()
        name = n.get_text()
        print(song)
        print(name)
