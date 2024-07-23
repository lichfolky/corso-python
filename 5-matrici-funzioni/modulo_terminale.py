import os

colori = {"violet":"\\033[38;5;20m"}

def clear_screen():
    os.system("cls||clear")
    
def blue(testo):
    return "\033[36m" + testo + "\033[0m"

def violet(testo):
    return "\033[38;5;20m" + testo + "\033[0m"
