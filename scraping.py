import sqlite3


# DBファイルを保存するためのファイルパス

# Google Colab
#path = '/content/'

# ローカル（自分のMac）
path = '/Users/fukasakai/ds-profinal/'

# DBファイル名
db_name = 'scraping.sqlite'

# DBに接続する（指定したDBファイル存在しない場合は，新規に作成される）
con = sqlite3.connect(path + db_name)

# DBへの接続を閉じる
con.close()

# 1．DBに接続する
con = sqlite3.connect(path + db_name)
# print(type(con))

# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 3．実行したいSQLを用意する
# テーブルを作成するSQL
# CREATE TABLE テーブル名（カラム名 型，...）;
sql_create_table_windows = 'CREATE TABLE IF NOT EXISTS windows(id int, windows int);'
#sql_create_table_git2 = 'CREATE TABLE git2(id int, mac int);'
# 4．SQLを実行する
cur.execute(sql_create_table_windows)

# 5．必要があればコミットする（データ変更等があった場合）
con.commit()

# 6．DBへの接続を閉じる
con.close()


# 1．DBに接続する
con = sqlite3.connect(path + db_name)
# print(type(con))

# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 3．実行したいSQLを用意する
# テーブルを作成するSQL
# CREATE TABLE テーブル名（カラム名 型，...）;
#sql_create_table_git = 'CREATE TABLE git(id int, windows int);'
sql_create_table_mac = 'CREATE TABLE IF NOT EXISTS mac(id int, mac int);'
# 4．SQLを実行する
cur.execute(sql_create_table_mac)

# 5．必要があればコミットする（データ変更等があった場合）
con.commit()

# 6．DBへの接続を閉じる
con.close()



from bs4 import BeautifulSoup
import requests
import time

mac_list = []

# 各ページのURLをループで取得
for i in range(1, 17):
    url = f'https://www.itreview.jp/products/macos/reviews?page={i}'
    r = requests.get(url)

    # 文字化け対策
    r.encoding = r.apparent_encoding

    # HTMLを解析する
    html_soup = BeautifulSoup(r.text, "html.parser")
    #取り出す時に数字だけ取り出せなかったからクラス名をリストにする
    # 星評価のクラス名
    class_names = [ "one", "two", "three", "four", "five"]

    # 各クラス名に対してスクレイピング
    #ここはいつも通り
    for class_name in class_names:
        star_rating_elements = html_soup.find_all("div", class_=class_name)

        for star_rating_element in star_rating_elements:
            review1 = f"{class_name} {star_rating_element.text.strip()}"
            print(review1)
            #作ったリストにぶち込む
            mac_list.append(review1)

#ここからはWindows
from bs4 import BeautifulSoup
import requests
import time

windows_list = []

# 各ページのURLをループで取得
for i in range(1, 71):
    url = f'https://www.itreview.jp/products/windows-10/reviews?page={i}'
    r = requests.get(url)

    # 文字化け対策
    r.encoding = r.apparent_encoding

    # HTMLを解析する
    html_soup = BeautifulSoup(r.text, "html.parser")
    #取り出す時に数字だけ取り出せなかったからクラス名をリストにする
    # 星評価のクラス名
    class_names = [ "one", "two", "three", "four", "five"]

    # 各クラス名に対してスクレイピング
    #ここはいつも通り
    for class_name in class_names:
        star_rating_elements = html_soup.find_all("div", class_=class_name)

        for star_rating_element in star_rating_elements:
            review2 = f"{class_name} {star_rating_element.text.strip()}"
            print(review2)
            #作ったリストにぶち込む
            windows_list.append(review2)

print(mac_list)
print(windows_list)

# 1．DBに接続する
con = sqlite3.connect(path + db_name)
# print(type(con))

# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 3．SQLを用意
# データを挿入するSQL
# INSERT INTO テーブル名 VALUES (列に対応したデータをカンマ区切りで);
sql_insert_many = "INSERT INTO windows VALUES (?, ?);"

# データをリストで用意する(一つずつの入力は無理だしリスト作った方が簡単にできそう)
windows1_list = []
#一番数が少ない言語に合わせた範囲で指定
#三つのデータの数が違ったなんで？
#rangeのところ2409にしたらダメだったからlenした
#numでやって、numが１の時それぞれのリストの1番目が格納されるようになってる
for num in range(0,len(windows_list)):
  windows1_list.append((num+1,windows_list[num]))
#一応git_listプリントしとく
print(windows1_list)

# 4．SQLを実行
cur.executemany(sql_insert_many, windows1_list)

# 5．コミット処理（データ操作を反映させる）
con.commit()

# 6．DBへの接続を閉じる
con.close()


# 1．DBに接続する
con = sqlite3.connect(path + db_name)
# print(type(con))

# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 3．SQLを用意
# データを挿入するSQL
# INSERT INTO テーブル名 VALUES (列に対応したデータをカンマ区切りで);
sql_insert_many = "INSERT INTO mac VALUES (?, ?);"

# データをリストで用意する(一つずつの入力は無理だしリスト作った方が簡単にできそう)
mac1_list = []
#一番数が少ない言語に合わせた範囲で指定
#三つのデータの数が違ったなんで？
#rangeのところ2409にしたらダメだったからlenした
#numでやって、numが１の時それぞれのリストの1番目が格納されるようになってる
for num in range(0,len(mac_list)):
  mac1_list.append((num+1,mac_list[num]))
#一応git_listプリントしとく
print(mac1_list)

# 4．SQLを実行
cur.executemany(sql_insert_many, mac1_list)

# 5．コミット処理（データ操作を反映させる）
con.commit()

# 6．DBへの接続を閉じる
con.close()

# 1．DBに接続する
con = sqlite3.connect(path + db_name)
# print(type(con))

# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 3．SQLを用意
# SELECT * FROM テーブル名;
# *の部分は取得したい列の名前をカンマ区切りで指定することもできる
sql_select = 'SELECT * FROM windows;'

# 4．SQLを実行
cur.execute(sql_select)

for r in cur:
  print(r)

#コミット処理
con.commit()
# 6．DBへの接続を閉じる
con.close()

# 1．DBに接続する
con = sqlite3.connect(path + db_name)
# print(type(con))

# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 3．SQLを用意
# SELECT * FROM テーブル名;
# *の部分は取得したい列の名前をカンマ区切りで指定することもできる
sql_select = 'SELECT * FROM mac;'

# 4．SQLを実行
cur.execute(sql_select)

for r in cur:
  print(r)

#コミット処理
con.commit()
# 6．DBへの接続を閉じる
con.close()