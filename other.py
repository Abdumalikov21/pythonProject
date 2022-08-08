text = input('Darsturda yoqdimi?: ').lower()
# text = text.lower()
if text=='ha':
    print('Foydalanganingiz uchun rahmat!!!')
elif text=='yoq':
    print('Oldin ozingiz shunday dastur tuzib oling...')
else:
    print('ha/yoq tanlamadingiz?')

    """
    456 -> integer(int)
    0.02 -> float
    5j -> complex
    True -> boolean(bool)
    'word' -> string(str)

    string bu nima?
    1. matn turi(text type)
                    Qoida!
    qoshtirnoq "" yoki birtirnoq '' ichida yozilgan
    har qangay malumot matn turi hisoblanadi!
    misol: 'word', "68468464",  "True", "5*6", "😊👌⭕😂😘❤"

    """
    # name = 'Tom Kenry'  # str
    # print(name)
    # print(type(name))  # <class 'str'>

    # name = str('Tom Kenry')
    # print(name)

    # number = 456789  # int
    # number = str(number)  #
    # print(number+16) # error chunki matnga sonni qoshib bolmaydi
    # print(type(number))

    # name = ''
    # name += 'Axmad Axmedov'
    # name += 'Ikromjon o`gli'
    # print(name)

    # n = int()
    # num = 0
    #
    # txt = str()
    # t = ''

    # text = 'Assalomu Aleykum "Ozbekiston"'
    meva1 = 'olma'
    meva2 = 'banan'
    mevalar = meva1 + meva2
    print(mevalar)

    # upper() - textni katta harfga aylantirish
    # text = 'assalomu aleykum'
    # text = text.upper()
    # print(text)

    # lower() - textni kichik harfga aylantiradi
    # text = 'AsSALOmU aLEyKUM'
    # print(text.lower())

    # capitalize() - berilgan textni faqt bosh harfini
    #                       katta qilib beradi
    # text = 'assalomu aleykum'
    # print(text.capitalize())

    # title() - berilgan textdagi har bir sozni
    #               bosh harfini katta qilib beradi
    text = 'assalomu aley kum hammaga'
    print(text.title())