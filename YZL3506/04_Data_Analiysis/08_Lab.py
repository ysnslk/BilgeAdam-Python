import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl

# region Task 1
# xlsx formatındaki excel'in 'Canada by Citizenship' isimli sheet'i okuyoruz.
# ilk 20 satır ve son 2 satır okunmayacak.

df = pd.read_excel(
    './Data/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2
)
print(df.head(10).to_string())
# endregion

# region Task 2
# OdName => Country
# AreaName => Continent
# RegName => Region
# Eski sütun isimlerini yenileriyle değiştirin
df.rename(columns={
    'OdName': 'Country',
    'AreaName': 'Continent',
    'RegName': 'Region'
}, inplace=True)
print(df.head(10).to_string())
# endregion

# region Task 3
# AREA, REG, Type, Coverage, DevName sütunlarını silin
df.drop(
    columns=['AREA', 'REG', 'Type', 'Coverage', 'DevName'],
    axis=1,
    inplace=True
)
print(df.head(10).to_string())
# endregion

# region Task 4
# Soru 1: Sütun başlıklarının tiplerini ekrana basın
for column in df.columns:
    print(type(column))

# Soru 2: Sütun başlıklarının hepsini tipini string yap
df.columns = list(map(str, df.columns))
for column in df.columns:
    print(type(column))
# endregion