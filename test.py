import pandas as pd

# 读取数据
data = pd.read_csv('final_data.csv')

# 计算每个国家的 co2_emission_animal 和 co2_emission_non_animals 的值
animal_category = 'Animal Products'
non_animal_category = 'Non-Animal Products'

# 计算 co2_emission_animal 和 co2_emission_non_animals 的值
co2_emission_animal = data[data['category'] == animal_category]['co2_emission_category'].iloc[0]
co2_emission_non_animals = data[data['category'] == non_animal_category]['co2_emission_category'].iloc[0]

# 为每个国家填充 co2_emission_animal 和 co2_emission_non_animals 的值
data['co2_emission_animal'] = co2_emission_animal
data['co2_emission_non_animals'] = co2_emission_non_animals

# 保存修改后的数据到新的 CSV 文件
data.to_csv('updated_data.csv', index=False)
