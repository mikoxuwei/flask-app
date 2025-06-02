# import pandas module
import pandas as pd
# data index
# data = pd.Series([20, 20, 15, 5, -12], index=["a", "b", "c", "d", "e"])
# # print(data)

# print(data[2], data[0])
# print(data['e'], data['d'])

# print('maximum:', data.max())
# print('sumation:', data.sum())
# print('standard deviation:', data.std())
# print('median:', data.median())
# print('largest numbers in front:', data.nlargest(3))


data = pd.Series(['Sawadeekrap', 'Python', 'Pandas'])
print(data.str.lower())  # Convert all strings to lowercase
print(data.str.len())    # Get the length of each string
print(data.str.separate('-')  # Separate each string by '-'
print(data.str.contains('a'))  # Check if 'a' is in each string
print(data.str.replace('a', 'A'))  # Replace 'a' with 'A' in each string    

