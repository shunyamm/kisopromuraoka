

from flask import Flask
from flask import render_template
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime

print ("exercise1 works!")

app = Flask(__name__)
html = urllib.request.urlopen("https://r.gnavi.co.jp/gant402/review/")

#変数htmlには上記のHTMLがstrで代入されているとします。
soup = BeautifulSoup(html,"lxml")

#変数titleにタイトルが代入されます。
main_body = soup.find("div", {"class": "toggle-unit.js-accordion-unit"})
print(html)
#################################################

#open_url = input('URLを入力してください: ')
#search_word = input('探したい言葉を入力してください: ')

#f = urllib.request.urlopen(open_url)
#html = f.read()
#f.close()



#soup = BeautifulSoup(html,"lxml")
#links = soup.find_all("a")
#link_set = []
#answer_link_set = []

# aタグすべて
#for link in links:
# リンクを抽出
#    if ":" in link.get("href"):
#        link_set = link.get("href")

#for link in link_set:
#    page = urllib.request.urlopen(link)
#    if search_word in page:
#        answer_link_set += link
