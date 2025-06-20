from flask import Flask
from flask import render_template  # 引入render_template函式，用於渲染HTML模板
from flask import jsonify  # 引入jsonify函式，用於返回JSON格式的響應
from flask import request  # 確保引入 request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__) #__name__代表目前執行的模組

@app.route('/') # 函式的裝飾 (decorator):以函式為基礎，提供附加功能
def home():
    return render_template("index.html")
    # return 'Hello, Flask!'

@app.route('/test') # 路由設定，當訪問/test時，會執行test函式
def test():
    return 'This is a test page.'

@app.route("/get_tsmc_data", methods=["GET"])
def get_tsmc_data():
    # 抓取台積電股票資訊
    url = 'https://tw.stock.yahoo.com/quote/2330'  # 台積電的股票
    web = requests.get(url, timeout=10)  # 設定超時時間為 10 秒
    soup = BeautifulSoup(web.text, 'html.parser')  # 轉換為 BeautifulSoup 物件

    title = soup.find('h1')  # 取得網頁標題
    a = soup.select('.Fz\\(32px\\)')[0]  # 取得股價
    b = soup.select('.Fz\\(20px\\)')[0]  # 取得漲跌幅

    s = ''  # 漲或跌的情況

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
        s = '-'  # 如果沒有漲跌情況，則預設為 '-'

    stock_info = f"{title.get_text()} : {a.get_text()}( {s}{b.text} )"
    return jsonify({"stock_info": stock_info})

@app.route("/invoice-check", methods=["POST"])
def invoice_check():
    data = request.get_json()
    num = data.get("invoice_number", "")
    
    url = 'https://invoice.etax.nat.gov.tw/index.html'
    result = ""
    
    try:
        web = requests.get(url, timeout=10)
        web.raise_for_status()
        web.encoding = 'utf-8'
        
        soup = BeautifulSoup(web.text, 'html.parser')
        td = soup.select('.container-fluid')[0].select('.etw-tbiggest')
        ns = td[0].getText()     # 特別獎號碼
        n1 = td[1].getText()     # 特獎號碼
        n2 = [td[2].getText()[-8:], td[3].getText()[-8:], td[4].getText()[-8:]]  # 頭獎號碼
        
        if not num.isdigit() or len(num) != 8:
            result = "發票號碼必須是8位數字。"
        elif num == ns:
            result = "恭喜！您的發票號碼中得特別獎 1000 萬元！"
        elif num == n1:
            result = "恭喜！您的發票號碼中得特獎 200 萬元！"
        else:
            match = False
            for i in n2:
                if num == i:
                    result = "恭喜！您的發票號碼中得頭獎 20 萬元！"
                    match = True
                    break
                elif num[-7:] == i[-7:]:
                    result = "恭喜！您的發票號碼中得二獎 4 萬元！"
                    match = True
                    break
                elif num[-6:] == i[-6:]:
                    result = "恭喜！您的發票號碼中得三獎 1 萬元！"
                    match = True
                    break
                elif num[-5:] == i[-5:]:
                    result = "恭喜！您的發票號碼中得四獎 4 千元！"
                    match = True
                    break
                elif num[-4:] == i[-4:]:
                    result = "恭喜！您的發票號碼中得五獎 1 千元！"
                    match = True
                    break
                elif num[-3:] == i[-3:]:
                    result = "恭喜！您的發票號碼中得六獎 2 百元！"
                    match = True
                    break
            if not match:
                result = "很遺憾，您的發票號碼沒有中獎。"
                
    except requests.exceptions.RequestException as e:
        result = f"發生錯誤: {e}"
        return jsonify({"result": result, "error": str(e)})
    
    return jsonify({"result": result})

@app.route("/get_currency_rate", methods=["GET"])
def get_currency_rate():
    url = 'https://rate.bot.com.tw/xrt/flcsv/0/day'  # 牌告匯率 CSV 網址
    
    try:
        rate = requests.get(url, timeout=10) 
        rate.encoding = 'utf-8'  # 設定編碼為 utf-8
        rt = rate.text  # 以文字模式讀取內容
        rts = rt.split('\n')  # 以換行符號分割成列表
        
        currency_rates = []
        
        # 跳過標題行
        for i in rts[1:10]:  # 只處理前9個貨幣
            try:
                a = i.split(',')  # 以逗號分割成列表
                if len(a) >= 13:  # 確認資料完整性
                    currency_name = a[0]  # 貨幣名稱
                    buying_rate = a[2]    # 現金買入
                    selling_rate = a[12]  # 現金賣出
                    currency_rates.append(f"{currency_name}: 買入 {buying_rate}, 賣出 {selling_rate}")
            except Exception as e:
                continue  # 跳過有問題的行
                
        result = "\n".join(currency_rates)
        if not result:
            result = "無法獲取匯率資料或資料格式有誤"
            
        return jsonify({"result": result})
        
    except requests.exceptions.RequestException as e:
        return jsonify({"result": f"連線失敗: {e}"})     

if __name__ == '__main__':
    app.run(debug=True) # debug=True 代表開啟除錯模式，會自動重啟伺服器