# 載入 pandas 模組
import pandas as pd
# 建立 Series 物件
data = pd.Series([20, 20, 15])
# # 基本 Series 操作
# print("Max", data.max())
# print("Median", data.median())
# data = data * 2
# print(data)

data = data == 20 # 比較布林代數
print(data)

data = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "salary": [50000, 60000, 70000]
})

# 基本 DataFrame 操作
print("DataFrame:\n", data)

print("===========================")
print(data.iloc[0])  # 使用 iloc 按位置選擇第一行