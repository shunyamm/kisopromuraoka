from flask import Flask,request
from flask import render_template
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import sqlite3

app = Flask(__name__)

# mainメソッド
if __name__ == "__main__":

    @app.route('/')
    def index():    
        return render_template('index.html', message="こんにちは")

    """
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
    """

@app.route("/result")
def result():
    keyword = request.args.get("search")
    
    #「karin's」データベースにアクセス
    #karins_data (shopName text, shopURL text, review longtext, reviewURL text);
    conn2 = sqlite3.connect("shops.db")
    cursor2 = conn2.cursor()
 
    cursor2.execute( "select * from karins_data" )   
    cursor2.execute('SELECT * FROM karins_data WHERE shopURL=?', (keyword,))
    #cursor.execute('SELECT * FROM karins_data WHERE shopURL LIKE "%s"' % ("%" + keyword + "%"))
    text2 = cursor2.fetchone()
    tuple_text2 =tuple(text2)
    
    shop_list = [""]
    for i in tuple_text2:
        shop_list.append(i)
        
    #「kato's」データベースにアクセス
    #main_shops (id int primary key, name varchar(30),tell int, address varchar(100), opening_time varchar(100),
    #tabelog_reviews longtext,gurunavi_reviews longtext, tabelog_star float, gurunavi_star float);
    conn3 = sqlite3.connect("shops_katou.db")
    cursor3 = conn3.cursor()
 
    cursor3.execute( "select * from main_shops" )   
    cursor3.execute('SELECT * FROM main_shops WHERE name=?', (keyword,))
    text3 = cursor3.fetchone(),
    tuple_text3 =tuple(text3)
    
    shop_list3 = [""]
    for i in tuple_text3:
        shop_list3.append(i)
    
    #「muraoka's」データベースにアクセス
    #muraokas_data (shopName text, shopURL text,review text,reviewURL text,tel text,star float);
    conn = sqlite3.connect("shops_muraoka.db")
    cursor = conn.cursor()
 
    cursor.execute("select * from muraokas_data")   
    cursor.execute('SELECT * FROM muraokas_data WHERE shopName=?', (keyword,))
    #cursor.execute('SELECT * FROM muraokas_data WHERE　shopName　glob "%s"' % ('*' + keyword + '*',))
    #cursor.execute('SELECT * FROM muraokas_data WHERE　shopName LIKE "%s"' % ("%" + keyword + "%"))
    text1 = cursor.fetchone(),
    tuple_text1 = tuple(text1)
    
    shop_list1 = [""]
    for i in tuple_text1:
        shop_list1.append(i)
    
    


    return render_template('result.html', keyword=keyword, all1=text1, all2=text2, all3=text3, shop_list=shop_list, shop_list1=shop_list1  )

#keyword=keyword, shopName1=shopName1,shopLink1=shopLink1, review1=review1, reviewLink1=reviewLink1, phoneNumber1=phoneNumber1, star1=star1
 
@app.route("/shop")
def shop():
    return render_template('shop.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

