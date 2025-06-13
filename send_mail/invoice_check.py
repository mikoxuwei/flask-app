import requests
from bs4 import BeautifulSoup

url = 'https://invoice.etax.nat.gov.tw/index.html'

try:
    web = requests.get(url, timeout=10)  # 設定超時時間為 10 秒
    web.raise_for_status()  # 檢查請求是否成功
    web.encoding = 'utf-8'  # 設定編碼為 utf-8

    soup = BeautifulSoup(web.text, 'html.parser')
    td = soup.select('.container-fluid')[0].select('.etw-tbiggest') # 中獎號碼位置
    ns = td[0].getText()     # 特別獎號碼
    n1 = td[1].getText()     # 特獎號碼
    n2 = [td[2].getText()[-8:], td[3].getText()[-8:], td[4].getText()[-8:]] # 頭獎號碼

    while True:
        try:
            num = input("請輸入發票號碼 (或輸入q離開): ")
            if num.lower() == 'q':
                print("已退出")
                break
            if not num.isdigit() or len(num) != 8:
                raise ValueError("發票號碼必須是8位數字。")
            num = num.strip()  # 去除前後空格
            if not num:
                raise ValueError("發票號碼不能為空。")
            if num == ns:
                print("恭喜！您的發票號碼中得特別獎 1000 萬元！")
            elif num == n1:
                print("恭喜！您的發票號碼中得特獎 200 萬元！")
            else:
                match = False
                for i in n2:
                    if num == i:
                        print("恭喜！您的發票號碼中得頭獎 20 萬元！")
                        match = True
                        break
                    elif num[-7:] == i[-7:]:
                        print("恭喜！您的發票號碼中得二獎 4 萬元！")
                        match = True
                        break
                    elif num[-6:] == i[-6:]:
                        print("恭喜！您的發票號碼中得三獎 1 萬元！")
                        match = True
                        break
                    elif num[-5:] == i[-5:]:
                        print("恭喜！您的發票號碼中得四獎 4 千元！")
                        match = True
                        break
                    elif num[-4:] == i[-4:]:
                        print("恭喜！您的發票號碼中得五獎 1 千元！")
                        match = True
                        break
                    elif num[-3:] == i[-3:]:
                        print("恭喜！您的發票號碼中得六獎 2 百元！")
                        match = True
                        break
                if not match:
                    print("很遺憾，您的發票號碼沒有中獎。")
        except KeyboardInterrupt:
            print("已退出")
        except ValueError as ve:
            print(f"輸入錯誤: {ve}")
except requests.exceptions.RequestException as e:
    print(f"發生錯誤: {e}")