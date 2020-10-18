# billboard japanのヒットチャートからデータを抽出する

import requests
from bs4 import BeautifulSoup
import re
import csv
import datetime

urlName = "http://www.billboard-japan.com/charts/detail?a=hot100"   # URLを指定
url = requests.get(urlName)                         # requestでWebページを取得
soup = BeautifulSoup(url.content, "html.parser")    # BeautifulSoupでHTMLを取得

# tableを取得
table = soup.findAll("table")[0]

# for i in range(1:21):
#     c = "rank" + str(i)
#     print(c)

# class名を指定（rankX:X=順位）して取得
row = table.findAll("tr", {"class":"rank1"})[0]
#print(row)
# class名を指定してp要素から曲名とアーティスト名を取得
song = row.findAll("p", {"class":"musuc_title"})[0].get_text()
name = row.findAll("p", {"class":"artist_name"})[0].get_text()
print("曲名：{}".format(song))
print("アーティスト名：{}".format(name))
# 前回の順位を取得
l = row.findAll("span", {"class":"last"})[0].get_text()
last = l.replace("前回：","")
print("前回：{}".format(last))

