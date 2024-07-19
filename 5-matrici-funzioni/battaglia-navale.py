import modulo_matrici
import modulo_terminale

mare = [[1,0,0],
        [1,0,2],
        [1,0,2]]

conteggi = [3,2]

totale = sum(conteggi)

colpi = [[0,0,0],
        [0,0,0],
        [0,0,0]]

termina_gioco = False
while not termina_gioco:
    modulo_terminale.clear_screen()
    modulo_matrici.stampa_matrice(colpi)
    riga = int(input("inserisci riga\n")) - 1
    colonna = int(input("inserisci colonna\n")) - 1 
    if colpi[riga][colonna] == 0:
        colpi[riga][colonna] = 1 # segna i colpi effettuati dall'utente
        if mare[riga][colonna] != 0:
            barca = mare[riga][colonna] - 1
            conteggi[barca] -= 1 # decrementa il numero di pezzi sani della barca
            totale -= 1
            if conteggi[barca] == 0:
                print("COLPITA E AFFONDATA!")
                if totale == 0:
                    termina_gioco = True
                    print("HAI VINTO! Tutte le barche sono state affondate!")
            else:
                print("COLPITO!")
        else:
            print("ACQUA!")
    else:
        print("hai già colpito qui!")