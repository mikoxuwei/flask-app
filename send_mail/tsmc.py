import requests
from bs4 import BeautifulSoup

url = 'https://tw.stock.yahoo.com/quote/2330' # 台積電的股票
web = requests.get(url, timeout=10)  # 設定超時時間為 10 秒
soup = BeautifulSoup(web.text, 'html.parser') # 轉換為 BeautifulSoup 物件

title = soup.find('h1')  # 取得網頁標題
a = soup.select('.Fz\\(32px\\)')[0]  # 取得股價
b = soup.select('.Fz\\(20px\\)')[0]  # 取得漲跌幅

s = '' # 漲或跌的情況

try:
    # 判斷是否為下跌(紅字)
    if soup.select('#main-0-QuoteHeader-Proxy .C\\(\\$c-fuji-down\\)'):
        s = '-'
except:
    pass
try:
    # 判斷是否為上漲(綠字)
    if soup.select('#main-0-QuoteHeader-Proxy .C\\(\\$c-fuji-up\\)'):
        s = '+'
except:
    pass

if s == '':
    s = '-' # 如果沒有漲跌情況，則預設為 '-'
print(f"{title.get_text()} : {a.get_text()}( {s}{b.text} )")

