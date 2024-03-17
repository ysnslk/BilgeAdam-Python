# Tuple (Demetler)
# List'ler gibi benzer mantığa sahiptirler. Lakin listelere uyguladığımız built-in fonksiyonlara sahip değildir.
# Lakin indexleme mantığı Tuple'da mevcuttur.
# Hme listelerde hemde demetelerde ki ortak noktalardan bir diğeride slicing (dilimleme)
# Tuple sabitlerimi tutacağım bir yapı gibi düşünebilirsiniz. Yani değiştirilemezler. 2 tuple birleştirme gibi fonksiyonlar vardır.

# tuple_1 = ('Galatasaray', 'Fenerbahçe', 'Beşiktaş', 'Trabzonspor')
# tuple_2 = ('12', '35.5', 'b', 'Eagles', 'Patrios', 'Red Skins')
# tuple_3 = tuple_1 + tuple_2
# print(tuple_3)
#
# # Dilimleme (Slicing)
# print(tuple_3[0:3])  # output => ('Galatasaray','Fenerbahçe','Beşiktaş')
# print(tuple_3[2:4])  # output => ('Beşiktaş','Trabzonspor')
#
# print(tuple_3[::2])  # output => ('Galatasaray','Beşiktaş','12','b','Patrios2)
# print(tuple_3[-1])   # output => Red Skins
# print(tuple_3[::-1])
# print(tuple_3[::-2])
# print(tuple_3[3::-2])

tuple_4 = ('Sarıyer', ('Suadiye', 'Erenköy'), ('Yeniköy', 'Bebek', ('Etiler', 'Ulus')))
print(tuple_4[2])
print(tuple_4[1][1])
print(tuple_4[2][2][0])
