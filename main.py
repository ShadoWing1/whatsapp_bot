import pyautogui
from time import sleep as bekle
from random import choice

#cumleler = []
#with open("cumleler", "+r") as dosya:

# dosya dan listeye atma
#    for satir in dosya:
#        if satir[len(satir) - 1] == '\n':
#            cumleler.append(satir[:-1])
#        else:
#            cumleler.append(satir)

a = 0

for i in range(5):
    print(i+1)
    bekle(1)

def mesaj():
    pyautogui.write(f"{a}")
    pyautogui.press('enter')

while True:
    mesaj()
    bekle(0)
    a = a + 1

# dosyadan rast gele okuma
#for _ in range(150):
#    pyautogui.write(choice(cumleler))
#    pyautogui.press('enter')
#    bekle(0.05)