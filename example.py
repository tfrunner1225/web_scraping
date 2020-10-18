# upgrade pip
# pip3 install --upgrade pip

# Install libraries before import
# pip3 install requests
# pip3 install BeautifulSoup4

import requests
from bs4 import BeautifulSoup
import re

# example
# url:https://qiita.com/koichi_hiphopdream/items/f4b006159cdbf5e4ee30

urlName = "https://business.nikkei.com"
url = requests.get(urlName)
soup = BeautifulSoup(url.content, "html.parser")

# span要素を取得して elems に格納
elems = soup.find_all("span")

for elem in elems: 
  try:
    # span要素の中からclass名を取得
    string = elem.get("class").pop(0)
    # print("string = {}".format(string))

    # class名が "category" が判定
    if string in "category":
      print(elem.string)
      # 同じ深さにあるh3タグからタイトルを取得
      title = elem.find_next_sibling("h3")
      # タイトル内に含まれる改行を削除
      print(title.text.replace('\n',''))
      # urlを取得
      # 1階層上のaタグを取得
      r = elem.find_previous('a')
      # hrefを指定してurlを組み合わせて出力
      print(urlName + r.get('href'), '\n')
  except:
    pass