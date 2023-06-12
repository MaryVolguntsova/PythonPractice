import pandas as pd

df = pd.read_csv('california_housing_train.csv')
# print(df.head())
# print(df[df['housing_median_age'] < 20][['total_bedrooms','total_rooms']])
# print(df.shape)
# print(df.dtypes)
# print(df[df['median_income'] < 2]['median_house_value'])
# print(df.describe())

# Табличные данные с выполнением двух условий
# print(df[(df.housing_median_age < 20) & (df.median_house_value > 70000)])

# Мин и макс значения в данных
# print(df.loc('median_house_value').max()) - не работает
# print(df.median_house_value.max(), df.median_house_value.min())

#  При выполнении условия
# print(df.loc[(df.median_income == 3.125), ['median_house_value']].max())

#  Найти максимальное количество жителей в зоне минимальной стоимости жилья
# print(df.loc[(df.median_house_value.()), ['population']].max())

# Взяли нижние 25% от медиан... (не одно значение, а несколько!)
df1 = df.loc[df.median_house_value < df.median_house_value.quantile(.15)]
print(df1.population.max())
print(df1) 
print(df.median_house_value.quantile(.25)) 