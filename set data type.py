import time
import pyttsx3
print("\tTosh Qaychi Qog'oz o'yiniga xush kelibsiz")
a=input('Oʻyini boshlashga tayyormisiz: ')
b = {'tosh', 'qaychi', "qog'oz"}
c = ["tosh", 'qaychi', "qog'oz"]
if a=='ha':
    print('please wait...')
    while True:
        time.sleep(2)
        e = b.pop()
        d = input("Javobingizni kiriting:")
        print("Kompyuter tanlagan javob: ", e)
        if d == 'qaychi' and e == "qaychi":
            pyttsx3.speak("draw")
        if d == "tosh" and e == "tosh":
            pyttsx3.speak("draw")
        if d == "qog'oz" and e == "qog'oz":
            pyttsx3.speak("draw")
        if d == "qaychi" and e == "qog'oz":
            pyttsx3.speak("!!!")
        if d == "qaychi" and e == "tosh":
            pyttsx3.speak("you win")
        if d == "tosh" and e == "qog'oz":
            pyttsx3.speak("you win")
        if d == "tosh" and e == "qaychi":
            pyttsx3.speak("you win")
        if d == "qog'oz" and e == "tosh":
            pyttsx3.speak("you win")
        if d == "qog'oz" and e == "qaychi":
            pyttsx3.speak("you lose")

if a=='yoq':
    time.sleep(2)
    print('O`yin to`xtatildi')


















