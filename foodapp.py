from flask import Flask
from flask import render_template
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime

print ("test2 works!")

app = Flask(__name__)
html = urllib.request.urlopen('https://r.gnavi.co.jp/gant402/review/')

#coding: utf-8


#変数htmlには上記のHTMLがstrで代入されているとします。
soup = BeautifulSoup(html,"lxml")

#変数title, timestamp, author, author_link, bodyにそれぞれタイトル、投稿日時、著者、著者のリンク、記事本文が代入されます。
title = soup.find('p',class_='trip-advisor-review-day--post')


@app.route('/')
def index():
    return render_template('page0.html', message="こんにちは",title=title)

@app.route("/page1")
def page1():
    return render_template('page1.html', user="ゲスト")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
