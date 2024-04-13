import pandas as pd
import numpy as np

number = [20, 30, 40, 50]
letters = ['a', 'b', 'c', 'd']
scaler = 5
dictionary = {
    'a': 10,
    'b': 20,
    'c': 30
}
ny_array = np.array([20, 30, 40, 40])

# pandas kütüphanesinde 2 ana veri tipi bulunmaktadır. Bunlarda 1. Series bir diğeri ise Dataframe'dir.
pd_series = pd.Series(number)
print(pd_series)
print(type(pd_series))

# pandas serisini ML algoritmalarında ki matematiksel işlemlerş yada istatistiksel methodları kullanırken ihtiyaç duyacağız.
pd_series = pd.Series(letters)
print(pd_series)

# python'daki sözlük objesinin anahtarlarını index valueları ise series value'su olarak ayarlar
pd_series = pd.Series(dictionary)
print(pd_series)

# python temellerinde önceden öğrendiğimiz dilimleme işlemini pandas serilerinde de kullanabiliriz.
# print(pd_series[:2])

# pandas serilerinin sahip olduğu bazı built-in fonksiyonlar ve attirbute'ler.
# not aynı fonksiyon ve attirbute'ler Dataframe içinde kullanılabilir.
print(pd_series.shape)  # serinin kaç satır ve sütundan oluştuğu döner

print(pd_series.dtype)  # serinin veri tipin döner

print(pd_series.ndim)  # serinin kaç katmanlı olduğunu döner

print(pd_series.describe())  # serinin hızlıca count, mean, std vb özet bilgilerini verir.

print(pd_series.head(
    1))  # serinin ilk index'ten başlayarak başlayarak argüman olarak verilen değere kadar olan indexleri döner. head() default değeri 5'tir. Yani bir argüman değeri belirtmezsek ilk 5 satır döerç

print(pd_series.tail(2))  # head() fonksiyonunun tam tersi yani son index'ten başlayarak head mantığında çalışır.

# şartın tutup tutmaması durumuna göre true false dönen
print(pd_series >= 20)

print(pd_series % 2 == 0)

# Aggregate function olarak isimlendirilen sum(), min(), max(), count(), mean() gibi fonksiyomları kullanabiliriz.
print(f'Bütün değerlerin toplamı: {pd_series.sum()}')

opel_2000 = pd.Series([20, 30, 40], ['astra', 'corsa', 'vectra'])
opel_2001 = pd.Series([50, 60, 70], ['astra', 'corsa', 'vectra'])

total = opel_2000 + opel_2001

print(total)

# DataFrame
# pandas yoğun olarak kullanılan bir başka yapıdır. Excel gibi düşünebilirsiniz yani satır ve sütunlardam oluşan bir yapı söz konusudur.
df = pd.DataFrame(
    data=np.random.rand(3, 5),
    index=['A', 'B', 'C'],
    columns=['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
)

print(df)

# DataFrame üzerinden veri seçme (select)
print(df['Column2'])
print(type(df['Column2']))

print(df[['Column1']])
print(type(df[['Column1']]))

# Tek kareli parantez ile select attığımda tek sütun çağırabilen double kareli parantez kullandığımda birden fazla sütun çağırabilirim. Bu yüzden kullandığım kareli parantez dönen verinin tipine etki etmetedir. tek kareli parantez series dönerken, double kareli parantez dataframe döner.


# loc[] index değerlini vererek istediğimiz index değerinede tutulan kayda erişebiliriz.
print(df.loc['B'])
print(type(df.loc['B']))

# ilk argüman index, ikinci argüman sütun olarak verilir.
print(df.loc['C', 'Column3'])
print(type(df.loc['C', 'Column3']))

print(df.loc[:, ['Column1', 'Column4']])

print(df.loc[['A', 'C'], ['Column2', 'Column4']])
