import pandas as pd

# 读取数据
data = pd.read_csv('updated_data_new.csv')

# 创建新的列来表示不同的档次
bins = [0, 500, 1000, 1500, float('inf')]
labels = ['0-500', '500-1000', '1000-1500', '1500+']
data['co2_emission_range'] = pd.cut(data['co2_emission_all'], bins=bins, labels=labels)

data.to_csv('updated_data.csv', index=False)