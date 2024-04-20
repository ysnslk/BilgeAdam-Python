import pandas as pd
import numpy as np

df = pd.read_csv('./Data/auto.csv')

# Veri setimizde sütun isimleri yok. Veri Setimize sütun isimleri basalım.
df.columns = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
              "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight",
              "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio",
              "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

# Hatalı ve eksik değerleri saptama
# Veri setimizde bazı hüclerelerde '?' sembolü bulunmaktadır. Şayet veri setimizde bu tarz anormalliklerin bulunması duurmda veri setimizi herhangi  bir ML algoritması sokup çalıştırmalıyız. Çünkü ML algoritmaları matematiksel işlemlere dayanmaktadır. Örneğin regresyon, Entropi vb. Bu sebepten ötürü veri setimizde ki eksik ya da hatalı alanları saptayıp onlşarı ele almamız ML algoritması için hazırlamamız gerekmetedir.

# Step-I
# Eksik ve hatalı verileri ML algoritmasında kullanmalıyız.Buun için numpy kütüphanesinde bulunan NaN yani diğer programlama dillerinde Null diye geçen boş anlamına gelen veriyi eksik ve hatalı verilerle değiştireceğiz böylelikle ML algortimasında bir hata ile karşılaşmayacağız.

df.replace('?', np.nan, inplace=True)
# print(df.head().to_string())

# Step-II
# Ne kadar eksik değerim var saptayalım
missing_values = df.isnull().sum()
total_missing = missing_values.sum()

print("Toplam eksik değer sayısı:", total_missing)
print("Her sütundaki eksik değer sayıları:")
print(missing_values)

# Step-III Handling Missing Values
# Yukarıda hangi sütunda ne kadar missing value'muz var detect ettik şimdi onları handle edelim.
# Peki neden uğraşıyoruz. Silip kurtulamaz mıyız? ML algoritmalarında ne kadar farklı veri ile algoritmamızı train edersek o kadar başarılı sonuçlar elde ederiz bu nedenle ver bir satır veri bizim kıymetlidir.

# Eksik verileri ele alırken iki yöntem kullanabiliriz.
# Bunlar:
# 1. İlgili sütunda bulunan değerlerin ortalamssını alarak bu ortalama değeri eksik değerlerin bulunduğu hücre yazabiliriz.
# 2. Yine ilgili sütunda bulunan değerşerin frekans aralığını bulup eksik değerlerin bulunduğu hücleree yazabiliriz. Burada frekans aralığından kastımız ilgili sütunda bulunan değerlerin ne sıklıkla ilgili sütunda bulunduğudurç

# Ortalama Değeri Bularak Eksik Veriler İle Değiştirme
df['normalized-losses'] = df['normalized-losses'].replace(to_replace=np.nan,
                                                          value=df['normalized-losses'].astype(float).mean())

df['horsepower'] = df['horsepower'].replace(to_replace=np.nan,
                                            value=df['horsepower'].astype(float).mean())
# print(df.head().to_string())


# Frekans Aralığı İle Eksik Verileri Değiştirme
# value_counts() ==> bir sütunda geçen farklı değerlerin kaç tane olduğunu bize söyler
# idmax() ==> ilgili sütunda en çok geçen değeri bize söyler
df['num-of-doors'] = df['num-of-doors'].replace(to_replace=np.nan,
                                                value=df['num-of-doors'].value_counts().idxmax())

# Veri Standartizasyonu
# ML algoritmalarında kullanılacak veri setinde ki değerlerin beilirli bir standartda olması gerekmektedir. Örneğin 2 ver kaynağımız olsun birisi amerikadan diğeri avrupadan. Avrupadan gelen verilerde ki yakıt türü kilometre başına litredir. Lakin amerikan da mile per galon olarak hesaplanmaktadır. Yada avrupada kilogram kullanırken amerika da pound yada libre birimleri kullanılmaktadır. Veri setinde ki bu farklı birimlere sahip değerler ML algoritmamızın train edilip sürettiği sonuçları olumsuz yönde etkileyecektir. Bu yüzden verimizin bir standarta sahip olması gerekmektedir.

df['city_l/km'] = 235/df['city-mpg']
df['highway_l/km'] = 235/df['highway-mpg']

# Veri Normalizasyonu
# Belirli bir sütunda ki değerlerin benzer bir aralığa kavuşması işlemine veri normalizasyonu denir. Veri setimizde bulunan lenght, width gibi değerlerinb 0.1 - 1.9 vb bir aralığa yani daha küçük scalar büyüklüklere dönüştürlmesi için yapılan  bir işlemdir.

df['length'] = df['length'] / df['length'].max()
df['width'] = df['width'] / df['width'].max()
df['height'] = df['height'] / df['height'].max()

print(df[['length', 'width', 'height']])

# Dummy Variable
# Veri setimizde

dummy_variable = pd.get_dummies(df['fuel-type'], dtype='float')
print(dummy_variable.head())

# bakımını yaptığımız veri setimizi yeni bir excel yazalım
df.to_csv('clean_auto.csv')


