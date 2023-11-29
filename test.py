import pandas as pd

# 读取数据
data = pd.read_csv('final_data.csv')

# 创建一个函数来计算每个国家的 co2_emission_animal 和 co2_emission_non_animals 的值
def calculate_emissions(df):
    animal_category = 'Animal Products'
    non_animal_category = 'Non-Animal Products'

    co2_emission_animal = df[df['category'] == animal_category]['co2_emission_category'].iloc[0]
    co2_emission_non_animals = df[df['category'] == non_animal_category]['co2_emission_category'].iloc[0]

    df['co2_emission_animal'] = co2_emission_animal
    df['co2_emission_non_animals'] = co2_emission_non_animals

    return df

# 按国家分组应用函数
data = data.groupby('country').apply(calculate_emissions).reset_index(drop=True)

# 保存修改后的数据到新的 CSV 文件
data.to_csv('updated_data_new.csv', index=False)
