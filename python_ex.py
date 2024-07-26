# Creaimo il giochino carta forbice sasso

print("Benvenuto!")
nome = input("Inserisci il tuo nome:")
print("Ciao", nome)
numero_partite = input("Quante partite vuoi fare?")

while numero_partite.isdigit() == False:
    numero_partite = input("Inserisci un numero intero per il numero delle partite:")

POSSIBILI_SCELTE = ["sasso", "carta", "forbice"]
partite=int(numero_partite)
punteggio_utente=0
punteggio_pc=0

import random

for i in range(partite):
    print("Scegli tra sasso, carta e forbice")
    scelta = input().lower()
    if scelta in POSSIBILI_SCELTE:
        scelta_pc = random.choice(POSSIBILI_SCELTE)
        print("Il pc ha scelto", scelta_pc)
        if scelta == scelta_pc:
            print("Pareggio")
        elif scelta == "sasso" and scelta_pc == "forbice":
            print("Hai vinto")
            punteggio_utente+=1
        elif scelta == "carta" and scelta_pc == "sasso":
            print("Hai vinto")
            punteggio_utente+=1
        elif scelta == "forbice" and scelta_pc == "carta":
            print("Hai vinto")
            punteggio_utente+=1
        else:
            print("Hai perso")
            punteggio_pc+=1
    else:
        print("Scelta non valida, partita annullata")
        break
    if i==partite:
        break

print(f'Fine del gioco, {nome}')
print("Il tuo punteggio è", punteggio_utente)
print("Il punteggio del pc è", punteggio_pc)
if punteggio_utente>punteggio_pc:
    print("Hai vinto!")
elif punteggio_utente<punteggio_pc:
    print("Hai perso!")
else:
    print("Pareggio!")