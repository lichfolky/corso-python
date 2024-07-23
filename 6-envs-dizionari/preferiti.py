preferiti = {"Impara ad usare il browser":"www.impara.com"}

def aggiungi_preferito(nome_preferito, url):
    preferiti.update({nome_preferito:url})
    
aggiungi_preferito("YouTube","www.youtube.com")
print(preferiti["YouTube"])

colori = {"crimson":"#ed143d"}