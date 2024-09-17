file = open(".\\9-exceptions-files\\nuovofile.txt","w")
file.write("Prima c'era un file con scritto ciao\n")
file.close()
file = open(".\\9-exceptions-files\\nuovofile.txt","a")
file.write("Aggiungo una riga")

'''
r read
w write
a append
r+ read write
c create, se è già presente il file da errore
'''