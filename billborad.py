# billboard japanのヒットチャートからデータを抽出する

import requests
from bs4 import BeautifulSoup
import re
import csv
import datetime


def get_chart(urlName):

    url = requests.get(urlName)                         # requestでWebページを取得
    soup = BeautifulSoup(url.content, "html.parser")    # BeautifulSoupでHTMLを取得

    # tableを取得
    table = soup.findAll("table")[0]

    # 順位ごとの情報を取得してリストに格納
    result = []
    for i in range(1,21):
        c = "rank" + str(i)
        print(c)
        # class名を指定（rankX:X=順位）して取得
        row = table.findAll("tr", {"class":c})[0]
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

        result.append([i,last,song,name])

    return result

# 最終結果をcsvとして出力
def save_csv(type, result):
    if type == "japan":
        file = open('./web_scraping/billboard_japan_{}.csv'.format(datetime.date.today()), 'w')
    elif type == "world":
        file = open('./web_scraping/billboard_world_{}.csv'.format(datetime.date.today()), 'w')
    w = csv.writer(file)
    w.writerows(result)
    file.close()
    # print(result)

urlName = "http://www.billboard-japan.com/charts/detail?a=hot100"   # URLを指定
result = get_chart(urlName)
save_csv("japan",result)

urlName = "http://www.billboard-japan.com/charts/detail?a=uhot100"   # URLを指定
result = get_chart(urlName)
save_csv("world",result)
