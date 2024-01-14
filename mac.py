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
            review = f"{class_name} {star_rating_element.text.strip()}"
            print(review)
            #作ったリストにぶち込む
            mac_list.append(review)


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
            review = f"{class_name} {star_rating_element.text.strip()}"
            print(review)
            #作ったリストにぶち込む
            windows_list.append(review)

