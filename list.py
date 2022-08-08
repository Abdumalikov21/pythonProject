# list -tartibli va o`zgaruvchan
# fruits1='banan', 'apple', 'mango', 'kivi'
# fruits2=str(('banan', 'apple', 'mango', 'kivi'))
# fruits3=('banan', 'apple', 'mango', 'kivi')
#
# txt1='apple'
# txt2=str('apple')
#
# data=(45,'python',False,45>20,7*9)
# fruits2=tuple(('banan','apple', 'mango', 'kivi'))
# print(len(fruits2))
#
# list-tartibli va o`zgaruvchan
# lib1=['pygame','playsound','tkinter','tirtle']
# lib2=list(('pygame','playsound','tkinter','tirtle'))
#
# sort() - listni tartiblab beradi
# numbers=[12,405,78,89,5.6,2.3]
# numbers.sort()
# print(numbers)
#
#
# alfabit=['k','f','a','d','c']
# alfabit.sort()
# print(alfabit)
#
# words=['olma','anor','banan','nok','apelsin','kivi']
# words.sort()
# print(words)
#
# ls=[True,False, int(),float(),complex(),tuple()]
# print(ls)
# append()-listni oxiriga yangi malumot qoshadi
# ls=['java','kotlin','dart','c#']
# ls.append('Swift')
# print(ls)
#
# insert()-biz bergan index boyicha malumot qoshadi
# ls=['java','kotlin','dart','c#']
# ls.insert('2','python')
# print(ls)

#remove()ocgirib tashlash


fruits=['olma','banan','apelsin','mandarin']
price=[5000,15000,20000,30000]

klient=input(f'{fruits}\nQanday meva olasiz?\n>>>: ').lower()
# if klient=='admin':
if klient in fruits:
      fruit_price=price[fruits.index(klient)]
      print(f'1kg-{fruit_price}')
      weight = float(input('miqdori(kg): '))
      print(f'{weight * fruit_price}som')
else:

 print('Bunday meva hozircha bizda mavjud emas')













'''________________________________________________________________________________________________________________'''

ln=['python','java','swift','dart','hackel','teserakt']
