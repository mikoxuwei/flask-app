# 載入 pandas 套件
import pandas as pd
## 篩選練習 - series
# data = pd.Series([30, 15, 20])
# # condition = [True, False, True]
# condition = data < 18
# filtered_data = data[condition]
# print(filtered_data)

# data = pd.Series(["您好", "Python", "Pandas"])
# condition = data.str.contains("Pandas")
# print(condition)
# filtered_data = data[condition]
# print(filtered_data)

data = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "salary": [25000, 50000, 40000]
})
print(data)
# condition = data["salary"] >= 40000
condition = data["name"] >= "Alice"
filtered_data = data[condition]
print(filtered_data)