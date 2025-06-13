import requests
url = 'https://invoice.etax.nat.gov.tw/index.html'
web = requests.get(url) # 取得網頁內容
web.encoding = 'utf-8'  # 設定編碼為 utf-8，加上.encoding = 'utf-8' 可以避免中文亂碼問題
print(web.text)