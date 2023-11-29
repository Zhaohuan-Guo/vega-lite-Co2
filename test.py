import pandas as pd


data = pd.read_csv('D:\\github\\test\\food_consumption.csv')

co2_sum_per_country = data.groupby('country')['co2_emmission'].sum().reset_index()

co2_sum_per_country.to_csv('co2_sum_per_country.csv', index=False)
