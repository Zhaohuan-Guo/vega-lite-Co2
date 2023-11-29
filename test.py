import pandas as pd

# 读取CSV文件
df = pd.read_csv('updated_data_new.csv', encoding='utf-8')  # 请将文件名替换成你的CSV文件名，确保指定正确的编码

# 创建一个函数将排放量映射到对应的范围
def map_emission_range(emission):
    if 0 <= emission < 500:
        return '0-500'
    elif 500 <= emission < 1000:
        return '500-1000'
    elif 1000 <= emission < 1500:
        return '1000-1500'
    else:
        return '1500+'

# 使用apply函数将CO2排放量映射到范围列
df['co2_emission_range'] = df['co2_emission_all'].apply(map_emission_range)

# 创建一个字典来存储每个国家的第一个CO2排放范围
country_ranges = {}

for index, row in df.iterrows():
    country = row['country']
    emission_range = row['co2_emission_range']
    
    if country not in country_ranges and emission_range != '':
        country_ranges[country] = emission_range

# 将处理后的范围值更新到DataFrame中，确保每个国家只有一个非空的范围值
for index, row in df.iterrows():
    country = row['country']
    if country in country_ranges:
        df.at[index, 'co2_emission_range'] = country_ranges[country]

# 保存处理后的数据到新的CSV文件
df.to_csv('processed_data.csv', index=False, encoding='utf-8-sig')
