import pandas as pd

df = pd.read_csv('./Data/youtube-ing.csv')


# En çok görüntülenmye sahip ilk 10 farklı videonun title ve views sütüblarını ekrana basın
# print(
#     df.groupby(by=['title', 'views'])
#     .sum(numeric_only=True)
#     .sort_values(by='views', ascending=False)
#     .head(10)
# )

# categorilerine göre likes ortalamalarını bulun
# print(
#     df.groupby(by='category_id')[['likes']].mean(numeric_only=True).sort_values(by='likes', ascending=False)
#     .head(10)
# )

# hangi kanal ne kadar yorum almış
# print(
#     df.groupby(by='channel_title')[['comment_count']].mean(numeric_only=True).sort_values(by='comment_count', ascending=False)
#     .head(10)
# )

# Herbir video için kullanılan tag sayısını tag_count isimli yeni bir sütun yarataun
# title ve tag_count ekrana basalım
# custom function
# Path-I
# def calculate_tag_amount(tag: str):
#     return len(tag.split('|'))


# df['tags_count'] = df['tags'].apply(calculate_tag_amount)
# print(df[['title', 'tags_count']].sort_values(by='tags_count', ascending=False))
# Path-II(lambda expression)
# df['tags_count'] = df['tags'].apply(lambda x: len(x.split('|')))
# print(df[['title', 'tags_count']])


# Her bir videonun like ve dislike oranlarını bulalım
# like_avg isimli yeni bir sütuna yazalım.
# yazacağımız function argüman olarak veri seti alacak.
def like_dislike_avg(data_set: pd.DataFrame) -> list:
    like_list = list(data_set['likes'])
    dislike_list = list(data_set['dislikes'])

    comb_list = list(zip(like_list, dislike_list))
    avg_list = []
    for like, dislike in comb_list:
        if like + dislike == 0:
            avg_list.append(0)
        else:
            avg_list.append(like / (like + dislike))

    return avg_list

df['like_avg'] = like_dislike_avg(df)

# yukarıda elde ettiğimiz like_avg sorgu yazalım

print(df.sort_values(by='like_avg', ascending=False)[['title','likes','dislikes','like_avg']].to_string())
