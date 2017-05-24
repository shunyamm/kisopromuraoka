from flask import Flask,render_template,request
app = Flask(__name__)

import urllib, urllib.request, re, json
from urllib import parse
#from selenium import webdriver
from bs4 import BeautifulSoup
#from selenium.webdriver.support.ui import WebDriverWait
#driver = webdriver.PhantomJS()


@app.route('/', methods=['GET'])
def index():
    # インデックスページを表示する
    return render_template('index.html')

@app.route("/page1")
def page1():

    #hotpepperグルメの検索フォームから目的のリンク先urlを取得する
    #検索フォームに値を代入
    keyword = request.args.get("name", "検索したい店名を入力してください")
    url = "https://www.hotpepper.jp/CSP/psh010/doBasic?FWT=" + parse.quote(keyword) + "&SA=SA11&RDT=&CBF=&CBT="
    
    #検索結果のhtmlから目的のお店のurlを取得
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html.read(),"lxml")
    link = soup.find("script",type="application/ld+json").text

    #リンク部分をjson形式に変換、url部分のみを抽出してリストにする
    link_list = json.loads(link)
    
    """
    for x in link_list:
        book_page = link_list['itemListElement'][x]
        print('{0}:{1}'.format('itemListElement', x))
    """
    #とりあえず一番上のリンクだけ取り出す
    link_target = link_list['itemListElement'][0]
    p = re.compile("url+")
    m = p.match(link_target)
    target = m.start()
    
    return render_template('page1.html', url=target)
    
if __name__ == "__main__":
    app.run()

#gunicorn -e SCRIPT_NAME='/a' -b 0.0.0.0:5000 app:app --reload
#http://0.0.0.0:5000/a/