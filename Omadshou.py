import time
a=input('Boriga baraka o`yiniga xush kelibsiz\nOyini boshlashga tayyormisiz\nha yiki yoq: ')
if a=='ha':
     b=input('Iltimos ismingizni kriting: ')
if a=='yoq':
  print('Tayor bo`lishingiz uchun 5 sekund vaqt beramiz')
print('Please Wait...')
time.sleep(5)

print(1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12, 13, 14, 15,16)
c = int(input('chois number: '))
d = {'Lada avtomabili', '2 xonali uy', 'Chet elga sayoxat', 'Televizor',  'kirsovun',
     'Malibu avtomabili', 'Makbook','Smartfon','Skuter', }
e = d.pop()
if c < 17:

    if c > 0:
        print('siz',e,'yutub oldingiz\n          Dasturimizdan foydalanganingiz uchun RAXMAT\n          Sovg`angizni asosiy ofisimixga kelib olib ketishingiz mumkin')
else:
    print('kechirasiz bunday raqam avjud emas')

