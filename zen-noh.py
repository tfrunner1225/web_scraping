# ZEN-NOH COUNTDOWN JAPANのヒットチャートからデータを抽出する

import requests
from bs4 import BeautifulSoup
import re

urlName = "https://www.tfm.co.jp/cdj/"             # URLを指定
url = requests.get(urlName)                         # requestでWebページを取得
soup = BeautifulSoup(url.content, "html.parser")    # BeautifulSoupでHTMLを取得

# div要素を取得して elems に格納
# class名を"even cleafix", "odd cleafix"に指定
elems = soup.find_all("div", {"class":["even cleafix", "odd cleafix"]})
# print(elems)

for elem in elems:  
    # print(elem)
    li = elem.find_all("li", {"class":{"rank","song"}})
    print(li)