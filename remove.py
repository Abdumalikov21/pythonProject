# clear()-LISTNI MALUMOTLARINU BERIKGAN MALUMOTLARNI O`CHIRADI
# ln=['python','java','swift','dart','hackel','teserakt']
# ln.clear()
# print(ln)


# del - berilgan o`zgaruvchilarni tozalaydi lekin list o`zi qoladi
# ln=['python','java','swift','dart','hackel','teserakt']
# del ln
# print(ln) #name error-sababi bizni list yuqorida o`chirip tashlandi

# extend()
# ls1=['a','b','c']
# ls2=['d','t','k']
# ls1.extend(ls1)
# print(ls1)

#pop() - berilgan indeksdagi malumotni o`chiradi
# ln=['python','java','swift','dart','hackel','teserakt']
# ln.pop
# print(ln)


# numbers=[1,23,[78,54,],97,[15,12]]
# print(numbers[2][0])#78
# print(numbers[4][0])#15
#
#
# k = ['m', 'a', 'k', 't', 'a', 'b']
# newWord = ['_', '_', '_', '_', '_', '_']
# count = 0
# while True:
#     if count==len(k):
#         break
#     s1 = input('Symbol: ')[0].strip()
#     if s1 in k:
#         indx_s1 = k.index(s1)
#         newWord[indx_s1]=s1
#         print(newWord)
#     else:
#         print('Wrong!!!')
#         count += 1
# print('You lose!!!')
#
#
#
#
import time

fruits = ['olma', 'banan', 'apelsin', 'mandarin', 'anor', 'kivi']
price = [5000, 15000, 20000, 30000, 35000, 70000]
while True:
    klient = input(f'{fruits}\nQanday meva olasiz?\n>>>').lower()
    if klient!='admin':
        print('Please Wait...')
        time.sleep(3)
        if klient in fruits:
            fruit_price = price[fruits.index(klient)]
            print(f"1 kg - {fruit_price}")
            weight = float(input('miqdori(kg): '))
            print(f"{weight*fruit_price} so`m")
        else:
            print('Bunday mahsulot bizda qolmadi!!!')
    else:
        command = input('Delete, Add, Update\nchoice command: ').lower()
        if command=='delete':
            getFruit = input('Delete fruit name: ')
            if getFruit in fruits:
                fruit_price = price[fruits.index(getFruit)]
                fruits.remove(getFruit)
                price.remove(fruit_price)
                print(fruits)
                print('removed!!!')
        elif command=='add':
            newFruit = input('Enter Fruit: ')
            newPrice = float(input('price the fruit: '))
            fruits.append(newFruit)
            price.append(newPrice)
            print('Please Wait...')
            time.sleep(2)
            print('Thank you!!!')
        elif command=='update':
            nameF = input('Fruit: ')
            newP = float(input(f'Price of {nameF}: '))
            fruit_price =  fruits.index(nameF)
            price[fruit_price]=newP
            print('Please Wait...')
            time.sleep(2)
            print('Thank you!!!')




# data = [['banan', 'olma'], ['java', 'python']]
# print(data[0])  # ['banan', 'olma']
# print(len(data))  # 2

# numbers = [1, 23, [78, 54], 97, [15, 12]]  # <----78-15
# print(len(numbers))  # 5
# print(numbers[3])  # 97



# numbers = [1, 23, [78, 54], 97, [15, 12]]
# n1 = numbers[2]
# print(n1[0])  # 78
#
# n2 = numbers[4]
# print(n2[0])  # 15

# numbers = [1, 23, [78, 54], 97, [15, 12]]
# print(numbers[2][0])  # 78
# print(numbers[4][0])  # 15

# numbers = [1, 23, [[[78, 54], 97], 45, 14], [15, 12]]
# print()





# # list - taribli va o`zgaruvchan
# fruits1 = 'apple', 'banana', 'mango', 'kivi'
# fruits2 = str(('apple', 'banana', 'mango', 'kivi'))
# fruits3 = ('apple', 'banana', 'mango', 'kivi')
# #
# txt1 = 'apple'
# txt2 = str('apple')
#
# data = (45, 'python', False, 45 > 10, 7*9)
# fruits2 = tuple(('apple', 'banana', 'mango', 'kivi'))
# print(len(fruits2))
#
# # list - taribli va o`zgaruvchan
# lib1 = ['pygame', 'playsound', 'tkinter', 'turtle']
# lib2 = list(('pygame', 'playsound', 'tkinter', 'turtle'))
#
# numbers = [12, 45, 78, 89, 5.6, 2.3]
# print(type(numbers))
# print(numbers[0])  # 12
# print(numbers[1] / 5)  # 9
# print(numbers[:4])  #  12, 45, 78, 89
# print(numbers[::-1])
#
# # sort() - listni tartiblab beradi
# numbers = [12, 45, 78, 89, 5.6, 2.3]
# numbers.sort()
# print(numbers)
#
# alfabit = ['k', 'f', 'a', 'd', 'c']
# alfabit.sort()
# print(alfabit)
#
#
# words = ['olma', 'anor', 'banan', 'nok', 'apelsin', 'behi']
# words.sort()
# print(words)
#
# ls = [True, False, int(), float(), complex(), tuple(), list()]
# print(ls)
#
# # append() - listni ohiriga yangi malumot qoshadi
# ls = ['java', 'kotlin', 'dart', 'C#']
# ls.append('Swift')
# print(ls)
#

# ls = ['java', 'kotlin', 'dart', 'C#']
# # insert() - biz bergan index boyicha malumot qoshadi
# ls = ['java', 'kotlin', 'dart', 'C#']
# ls.insert(2, 'python')
# print(ls)


# remove() - list ichidan malumot olib tashlaydi
# ls = ['java', 'kotlin', 'dart', 'C#']
# ls.remove('dart')
# print(ls)


# ln = ['python', 'java', 'swift', 'dart', 'hackel', 'teserakt']
# ln[1]='c++'
# print(ln)


# remove() - list ichidan berilgan malumotni ochiradi
# ln = ['python', 'java', 'swift', 'dart', 'hackel', 'teserakt']
# ln.remove('teserakt')
# print(ln)

# clear() - listni malumotlarini tozalaydi lekin list ozi qoladi
# ln = ['python', 'java', 'swift', 'dart', 'hackel', 'teserakt']
# ln.clear()
# print(ln)

# del - berilgan ozgaruvchidagi malumot va var ni ochirin tashlaydi
# ln = ['python', 'java', 'swift', 'dart', 'hackel', 'teserakt']
# del ln
# print(ln)  # nameError - sababi bizni list yuqorida ochirib tashlangan edi


# ln = ['python', 'java', 'swift', 'dart', 'hackel', 'teserakt']
# ln.reverse()  # listni teskari tartibga keltiradi
# print(ln)

# extend() - ikkita listni birlashtirib beradi
# ls1 = ['a', 'b', 'c']
# ls2 = ['d', 't', 'k']
# ls1.extend(ls2)
# print(ls1)

# pop() - berilgan indexdagi malumotni ochiradi
ln = ['python', 'java', 'swift', 'dart', 'hackel', 'teserakt']
ln.pop(2)
print(ln)