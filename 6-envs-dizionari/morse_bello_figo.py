import morse_dizionario
import keyboard
import os

testo = ""
'''
def sempre_print(a):
    print(a + "!!!!!")

keyboard.add_hotkey('a', sempre_print, args=(['forza napoli']))
keyboard.wait()

'''

while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == "esc":
            break
        if event.name == "space":
            testo += " "
        else: 
            if event.name in morse_dizionario.encode:
                testo += morse_dizionario.encode[event.name]
        os.system("cls||clear")
        print(testo)