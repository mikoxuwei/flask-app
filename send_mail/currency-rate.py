import requests

# url = 'http://rate.bot.com.tw/xrt/flcsv/0/day'  # 牌告匯率 CSV 網址
url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'  # 牌告匯率 HTML 網址
rate = requests.get(url) 
rate.encoding = 'utf-8'  # 設定編碼為 utf-8
rt = rate.text # 以文字模式讀取內容
rts = rt.split('\n')  # 以換行符號分割成列表
for i in rts:
    try:
        a = i.split(',')  # 以逗號分割成列表
        print(a[0] + ':' + a[12]) #取出第一個(0)和第十三個項目(12)
        rate = requests.get(url, timeout=10)  # 設定超時時間
        rate.raise_for_status()  # 檢查 HTTP 回應狀態碼
        print(rate.text)
    except requests.exceptions.RequestException as e:
        print(f"連線失敗: {e}")
    except: break  # 如果出現錯誤，則跳出迴圈


import requests

url = 'https://rate.bot.com.tw/xrt/flcsv/0/day'  # 牌告匯去 CSV 網址
rate = requests.get(url)  # 爬取網址內容
rate.encoding = 'utf-8'  # 調整回應訊息編碼為 utf-8，避免編碼不同造成亂碼
rt = rate.text  # 以文字模式讀取內容
rts = rt.split('\n')  # 使用「換行」將內容拆分成串列
for i in rts:  # 讀取串列的每個項目
    try:  # 使用 try 避開最後一行的空白行
        a = i.split(',')  # 每個項目用逗號拆分成子串列
        print(a[0] + ': ' + a[12])  # 取出第一個 ( 0 )和第十三個項目 ( 12 )
    except:
        break