import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"

request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windowns NT 10.0; Win64; x64) ApplieWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("div", class_="title")
for title in titles:
    if title.a != None:
        print(title.a.string)