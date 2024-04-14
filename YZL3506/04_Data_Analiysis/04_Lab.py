import pandas as pd

df = pd.read_csv('./Data/nba.csv')

# En yüksek maaş alan oyuncu kim?
# print(df[df['Salary'] == df['Salary'].max()][['Name', 'Salary']])

# Takımlara göre oyuncuların maaş ortalaması nedir?
# print(df.groupby('Team')['Salary'].mean())

# Veri setinde kaç farklı takım vardır. (groupby ile yapılır ama bir başka fonksiton daha var bu iş için)
# bir sütunda biricik değerleri nasıl sayarım
# group by ile yaparsam satır sayarken null olan satırları sayabilirim . Bu yüzden bu örneği group by ile yapmak risklidir.
# print(df['Team'].nunique())

# Yaşı 20 ile 35 arasında olan oyuncuların adı, takımı, yaş bilgilerini ve yaş bilgisine göre çoktan aza sıralayacak şekilde ekrana basın.
# print(
#     df[
#         (df['Age'] >= 25) & (df['Age'] <= 35)
#         ]
#     [['Name', 'Age', 'Team']]
#     .sort_values(by='Age', ascending=False)
# )


# İsmi içerisinde 'and' ifadesi geçen oyuncuları listeleyen bir custom function yazın.
# Bu fonksiyonu dataframe uygulayın.
def str_find(name: str):
    if 'and' in name.lower():
        return True
    else:
        return False


print(df[df['Name'].apply(str_find)])