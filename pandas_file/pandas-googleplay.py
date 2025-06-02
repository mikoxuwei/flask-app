import pandas as pd

data = pd.read_csv("googleplaystore.csv")
# print(data)
print('資料筆數:', data.shape)
print('資料欄位:', data.columns)
print("==========================================)")
print(data["Rating"])

# # 分析資料
# print("==========================================)")
# print('平均數:', data["Rating"].mean())
# print('中位數:', data["Rating"].median())
# print('取得前一百得平均:', data["Rating"].nlargest(100).mean())
# print("==========================================)")
# condition = data["Rating"] >= 5.0
# data = data[condition]
# print(data)
# print("==========================================)")
# print(data['Installs']) # 以字串形式儲存

# print('==========================================)')
# # 分析資料：安裝數量的各種統計數據
# # 處理 Installs 欄位：移除逗號和加號，轉換為數值
# data['Installs'] = data['Installs'].str.replace('[+,]', '', regex=True)
# data['Installs'] = pd.to_numeric(data['Installs'], errors='coerce') # 無法轉換的設為 NaN
# #分析資料：安裝數量的各種統計數據
# print('平均數:', data['Installs'].mean())
# condition = data["Installs"] > 10000
# print('安裝次數大於 10,000 次的應用程式有幾個:', data[condition].shape[0])

# # 基於資料的運用：以關鍵字搜尋應用程式名稱
# print('==========================================)')
# keyword = input('請輸入關鍵字：')  # user input
# condition = data['App'].str.contains(keyword)
# print('包含關鍵字的應用程式數量:', data[condition]['App'])

print('==========================================)')
keyword = input('請輸入關鍵字：')  # user input
condition = data['App'].str.contains(keyword, case=False)  # 不區分大小寫
print('包含關鍵字的應用程式數量:', data[condition].shape[0])