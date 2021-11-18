prezzo=5.5
sconto=1
cliente_pref='giacomo'

print('Inserisci come ti chiami?')
nome=input()

print('Inserisci quanti anni hai?')
anni=int(input())

if nome==cliente_pref and anni>25:
    prezzo-=sconto

print('Prezzo drink: '+ str(prezzo))
