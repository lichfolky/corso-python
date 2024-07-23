import morse_dizionario
import os

testo  = ""
testo_morse = ""
'''
def sempre_print(a):
    print(a + "!!!!!")

keyboard.add_hotkey('a', sempre_print, args=(['forza napoli']))
'''
os.system("cls||clear")

while True:
    testo_input = input()
    testo_morse += morse_dizionario.encode_text(testo_input)
    testo += testo_input
    os.system("cls||clear")
    print(testo,": ",testo_morse)