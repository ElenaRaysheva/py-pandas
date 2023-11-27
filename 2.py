import pandas as pd

def baltic(country):
    if country in ['Lithuania', 'Latvia', 'Estonia']:
        return 'Прибалтика'

    return 'Other'

power = pd.read_csv("./power.csv")
power['baltic'] = power.country.apply(baltic)
result = power[power.year.isin(range(2005, 2011))][power.quantity.gt(0)][power.category.isin([4,12,21])][power.baltic.eq('Прибалтика')]


print(result.quantity.sum()) # 240580.0
