
import qrcode
text=input('Matn kriting: ')
img=qrcode.make(text)
img.save("rasm1.png")