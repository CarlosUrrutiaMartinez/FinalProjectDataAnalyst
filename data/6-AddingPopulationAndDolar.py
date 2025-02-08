import pandas as pd
from datetime import datetime

date_range = pd.date_range(start='2017-01-01', end='2024-12-31', freq='D')

poblacion_anual = {
    '2017': 7.53,
    '2018': 7.63,
    '2019': 7.71,
    '2020': 7.79,
    '2021': 7.87,
    '2022': 7.95,
    '2023': 8.03,
    '2024': 8.10 
}

poblacion_df = pd.DataFrame({
    'Fecha': pd.to_datetime(list(poblacion_anual.keys()), format='%Y'),
    'Poblacion_Mundial': list(poblacion_anual.values())
})

poblacion_df.set_index('Fecha', inplace=True)
poblacion_diaria = poblacion_df.reindex(pd.date_range(start='2017-01-01', end='2024-12-31', freq='D'))
poblacion_diaria['Poblacion_Mundial'] = poblacion_diaria['Poblacion_Mundial'].interpolate(method='linear')

m2_anual = {
    '2017': 13.8,
    '2018': 14.3,
    '2019': 15.3,
    '2020': 18.2,
    '2021': 19.4,
    '2022': 21.7,
    '2023': 21.5,
    '2024': 21.0
}

m2_df = pd.DataFrame({
    'Fecha': pd.to_datetime(list(m2_anual.keys()), format='%Y'),
    'USD_en_Circulacion': list(m2_anual.values())
})

m2_df.set_index('Fecha', inplace=True)
m2_diaria = m2_df.reindex(pd.date_range(start='2017-01-01', end='2024-12-31', freq='D'))
m2_diaria['USD_en_Circulacion'] = m2_diaria['USD_en_Circulacion'].interpolate(method='linear')

df = pd.DataFrame(date_range, columns=['Fecha'])
df.set_index('Fecha', inplace=True)
df['Poblacion_Mundial'] = poblacion_diaria['Poblacion_Mundial'].values
df['USD_en_Circulacion'] = m2_diaria['USD_en_Circulacion'].values

df.to_csv('dataset_poblacion_m2.csv')


