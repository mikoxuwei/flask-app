from flask import Flask
from flask import render_template  # 引入render_template函式，用於渲染HTML模板
app = Flask(__name__) #__name__代表目前執行的模組

@app.route('/') # 函式的裝飾 (decorator):以函式為基礎，提供附加功能
def home():
    return render_template("index.html")
    # return 'Hello, Flask!'

@app.route('/test') # 路由設定，當訪問/test時，會執行test函式
def test():
    return 'This is a test page.'

if __name__ == '__main__':
    app.run(debug=True) # debug=True 代表開啟除錯模式，會自動重啟伺服器
    # app.run(host='