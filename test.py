import pandas as pd

# 读取两个数据集
data1 = pd.read_csv('new_data_1.csv')
data2 = pd.read_csv('co2_sum_per_country.csv')

# 根据 'country' 和 'food_category' 列合并两个数据集
merged_data = pd.merge(data1, data2, on=['country'])

merged_data.to_csv('new_data_1.csv', index=False)
