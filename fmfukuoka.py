import requests
from bs4 import BeautifulSoup
import re

urlName = "https://fmfukuoka.co.jp/hitchart/"
url = requests.get(urlName)
soup = BeautifulSoup(url.content, "html.parser")