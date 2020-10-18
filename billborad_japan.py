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