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



