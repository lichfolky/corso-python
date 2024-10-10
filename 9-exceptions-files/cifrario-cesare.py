import re

messaggioSegreto = ""
k = 1
try:
    with open("9-exceptions-files\\messaggio.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.lower()
            # line = re.sub(r"[^\w]", " ", line)
            for lettera in line:
                if lettera.isalpha():
                    num = ord(lettera)
                    coded_num = num + k
                    if coded_num > 122:
                        coded_num = 96 + (coded_num - 122)
                        # print(lettera, num, coded_num)
                    messaggioSegreto += chr(coded_num)
                else:
                    messaggioSegreto += lettera
        with open("9-exceptions-files\\coded-msg.txt", "a", encoding="utf-8") as coded_file:
            coded_file.write(messaggioSegreto)
except FileNotFoundError as error:
    print("file non trovato")
