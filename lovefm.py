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

result = []
for row in rows:
    # class名を指定してtd要素を取得
    td = row.findAll("td", {"class":"music"})
    # ヘッダーにはtdが含まれないので除外
    if len(td) != 0:
        # print(len(td))
        # print(td[0])

        # 今週と先週の順位を取得
        # 画像のファイル名を利用
        imgs = row.findAll("img")
        for img in imgs:
            if img["src"].startswith("/img/top40/chart_lst"):
                #print(img["src"])
                s = img["src"].replace("/img/top40/chart_lst","")
                last = s.replace(".gif","")
            elif img["src"].startswith("/img/top/icon_new.gif"):
                #print(img["src"])
                last = "-"
            elif img["src"].startswith("/img/top40/chart_"):
                #print(img["src"])
                s = img["src"].replace("/img/top40/chart_","")
                this = s.replace(".gif","")
            
        print("This week rank is {}".format(this))
        print("Last week rank is {}".format(last))

        [s, n] = td[0].findAll("li")
        song = s.get_text()
        name = n.get_text()
        print(song)
        print(name)

        result.append([this,last,song,name])

# 最終結果をcsvとして出力
file = open('./web_scraping/lovefm_{}.csv'.format(datetime.date.today()), 'w')
w = csv.writer(file)
w.writerows(result)
file.close()
# print(result)