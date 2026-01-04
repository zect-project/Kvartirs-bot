import pandas as pd

df = pd.read_csv("Kvartirs/data/main_train.csv")

city_num = {
    'Moscow': 1,
    'Novosibirsk': 2,
    'Kazan': 3,
    'Petersburg': 4,
    'Yekaterinburg': 5
}

df['city'] = df['city'].map(city_num)

print(df['city'])
