import pandas as pd
# 建立 DataFrame 物件
data = pd.DataFrame({
    'name': ['John', 'Anna', 'Peter'],
    'salary': [50000, 60000, 70000],
},index=['a', 'b', 'c'])
print("DataFrame:\n", data)

print("===========================")
# observe data
print('data size:', data.size)  # 總元素數量
print('data shape:', data.shape)  # 行數和列數
print('data index:', data.index)  # 行索引

print('grab 2nd row data:', data.iloc[1], sep='\n')
print('===========================')
print('grab c row data:', data.loc['c'], sep='\n')  # 使用行索引選擇第二行
# grab 
names = data['name']  # grab name column
print('transfer all names to capital:', names.str.upper(), sep='\n')  # 將所有名字轉為大寫
# calculate average salary
average_salary = data['salary'].mean()
print('average salary:', average_salary)
# set new column
data['bonus'] = data[50000, 60000, 70000]
data['rank'] = pd.Series([3,6,1],index = ['a','b','c'])
data['cp'] = data['salary']
print(data)