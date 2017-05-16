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
main_body = soup.find("div", {"id": "main"})


@app.route('/')
def index2():
    return render_template('index.html', message="こんにちは",review=main_body)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/signin")
def signin():
    return render_template('signin.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/sidebar-left")
def sidebarleft():
    return render_template('sidebar-left.html')

@app.route("/sidebar-right")
def sidebarright():
    return render_template('sidebar-right.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
