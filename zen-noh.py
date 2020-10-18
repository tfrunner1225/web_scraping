# ZEN-NOH COUNTDOWN JAPANのヒットチャートからデータを抽出する

import requests
from bs4 import BeautifulSoup
import re

urlName = "https://www.tfm.co.jp/cdj/"             # URLを指定
url = requests.get(urlName)                         # requestでWebページを取得
soup = BeautifulSoup(url.content, "html.parser")    # BeautifulSoupでHTMLを取得