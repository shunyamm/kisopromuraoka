#!/usr/bin/env python
# -*- coding: utf-8 -*-
#*****************************************************************************************
# ぐるなびWebサービスの応援口コミAPIを実行しハンバーグの口コミを取得しパースするプログラム
# 注意：アクセスキーはユーザ登録後に発行されるキーを指定してください。
#*****************************************************************************************
import sys
import urllib.request
import urllib.parse
import json

####
# 変数の型が文字列かどうかチェック
####
def is_str( data = None ) :
  if isinstance( data, str ) or isinstance( data, unicode ) :
    return True
  else :
    return False

####
# 初期値設定
####
# APIアクセスキー
keyid     = "bee69271fd2e6a694365a72a7da1f109"
# エンドポイントURL
url       = "https://api.gnavi.co.jp/PhotoSearchAPI/20150630/"
#店舗名
shop_name = u"Anima Libera"
# メニュー
shop_name = u"AnimaLibera"
#文字コード
encoding = 'utf-8'

####
# APIアクセス
####
# URLに続けて入れるパラメータを組立
query = [
  ( "format",    "json"    ),
  ( "keyid",     keyid     ),
  ( "shop_name", shop_name.encode(encoding) )
]
# URL生成
url += "?{0}".format( urllib.parse.urlencode( query ) )
# API実行
try :
  result = urllib.request.urlopen( url ).read()
except ValueError :
  print ("APIアクセスに失敗しました。")
  sys.exit()

####
# 取得した結果を解析
####
data = json.loads( result )

# エラーの場合
if "error" in data :
  if "message" in data :
    print ("{0}".format( data["message"] ))
  else :
    print ("データ取得に失敗しました。")
  sys.exit()

# ヒット件数取得
total_hit_count = None
if "total_hit_count" in data["response"] :
  total_hit_count = data["response"]["total_hit_count"]

#ページごとの件数を取得
hit_per_page = None
if "hit_per_page" in data["response"] :
  hit_per_page = data["response"]["hit_per_page"]

# ヒット件数が0以下、または、ヒット件数がなかったら終了
if total_hit_count is None or total_hit_count <= 0 or hit_per_page is None or hit_per_page <= 0 :
  print ("指定した内容ではヒットしませんでした。")
  sys.exit()

# ヒット件数表示
print ("{0}件ヒットしました。".format( total_hit_count ))
print ("----")

# 出力件数
disp_count = 0

# 応援口コミデータ取得
for i in range( hit_per_page ) :
  photo = data["response"]["{0}".format(i)]["photo"]
  line                 = []
  id                   = ""
  name                 = ""
  mname                = ""
  comment              = ""

  # 店舗番号
  if "shop_id" in photo and is_str( photo["shop_id"] ) :
    id = photo["shop_id"]
  line.append( id )

  # 店舗名
  if "shop_name" in photo and is_str( photo["shop_name"] ) :
    name = photo["shop_name"]
  line.append( name )

  # メニュー名
  if "menu_name" in photo and is_str( photo["menu_name"] ) :
    mname = photo["menu_name"]
  line.append( mname )

  # コメント
  if "comment" in photo and is_str( photo["comment"] ) :
    comment = photo["comment"]
  line.append( comment )

  # タブ区切りで出力
  print ("\t".join( line ))
  disp_count += 1

# 出力件数を表示して終了
print ("----")
print ("{0}件出力しました。".format( disp_count ))
sys.exit()
