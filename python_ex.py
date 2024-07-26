# Creaimo il giochino carta forbice sasso

print("Benvenuto!")
nome = input("Inserisci il tuo nome:")
print("Ciao", nome)

POSSIBILI_SCELTE = ["sasso", "carta", "forbice"]
partite=10
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
    if i==partite:
        break
print("Fine del gioco")
print("Il tuo punteggio è", punteggio_utente)
print("Il punteggio del pc è", punteggio_pc)
if punteggio_utente>punteggio_pc:
    print("Hai vinto!")
elif punteggio_utente<punteggio_pc:
    print("Hai perso!")
else:
    print("Pareggio!")