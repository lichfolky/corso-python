import os
import time
from pyfiglet import Figlet

for i in range(3, 0, -1):
    os.system("cls||clear")
    font = Figlet(font="moscow")
    print("\033[36m", font.renderText(str(i)), "\033[0m", sep="", end="")
    time.sleep(1)
os.system("cls||clear")
font = Figlet(font="poison")
print("\033[38;5;20m", font.renderText("Boom!"), "\033[0m", sep="", end="")
