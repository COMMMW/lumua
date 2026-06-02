import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

data_list = []

# 示范：爬大众点评某店铺前5页评论（你可以换url）
for page in range(1, 6):
    # 这里url你换成自己的店铺评论页
    url = f"https://www.dianping.com/shop/xxxxxx/review_feed?pn={page}"
    print("正在爬第", page, "页")
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        continue
    soup = BeautifulSoup(res.text, "html.parser")
    reviews = soup.find_all("div", class_="review-words")
    for r in reviews:
        content = r.get_text(strip=True)
        data_list.append({"user_content": content})
    time.sleep(2)

df = pd.DataFrame(data_list)
df.to_csv("xunpu_data.csv", index=False, encoding="utf-8-sig")
print("完成，共", len(df), "条")
df.head()
