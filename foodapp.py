from flask import Flask
from flask import render_template
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime

print ("test2 works!")

app = Flask(__name__)
html = urllib.request.urlopen("https://r.gnavi.co.jp/gant402/review/").read()

#変数htmlには上記のHTMLがstrで代入されているとします。
soup = BeautifulSoup(html,"lxml")

#変数titleにタイトルが代入されます。
main_body = soup.find("div", {"class": "unit-inner"})
reviews = main_body.find("ul", class_= "trip-review")
titles = main_body.find("li",{"class": "trip-advisor-review__list.cx"})

@app.route('/')
def index():
    return render_template('page0.html', message="こんにちは",title=main_body)

@app.route("/page1")
def page1():
    return render_template('page1.html', user="ゲスト")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
