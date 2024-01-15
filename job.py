from bs4 import BeautifulSoup
import requeｓts
import time
#リスト作る
mac_job_list = []
for i in range(1,17):
    time.sleep(1)
    url = f'https://www.itreview.jp/products/macos/reviews?page={i}'
    r=requests.get(url)

#文字化け少なく（意味なし？）
    r.encoding = r.apparent_encoding
#HTMLを解析する
    html_soup = BeautifulSoup(r.text, "html.parser")
#レビュースター名
    mj_span_list = html_soup.find_all(class_="product-review-info")
    for mj_tag in mj_span_list:
        mj_name = mj_tag.text.strip()
        mac_job_list.append(mj_name)
        print(mj_name)