from flask import Flask
from flask import render_template  # 引入render_template函式，用於渲染HTML模板
from flask import jsonify  # 引入jsonify函式，用於返回JSON格式的響應
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

@app.route("/invoice-check")
def invoice_check():
    return render_template("invoice_check.html")

if __name__ == '__main__':
    app.run(debug=True) # debug=True 代表開啟除錯模式，會自動重啟伺服器
    # app.run(host='