#condizionali
#con valori
anni=16
#dichiarazione if
if anni<18: 
    print('Sei minorenne: puoi ordinare solo analcolici')  
elif anni>80:
    print('puoi ordinare alcolici ma facci piano')
else:
    print('sei maggiorenne: puoi ordinare ciò che vuoi')

#condizioni
#if anni>=21:
#if anni>30:
#if anni==50:

#con stringhe
nome='pier'
if nome == 'gianni':
    print('Bentornato gianni')

#con booleani
pub_aperto=False
if pub_aperto:
    print('siamo pronti a servirti')
else:
    print('gli orari sono ...')

#operatori booleani
#or una o l'altra vera
#and entrambe vere
#not condizione non vera
consegna=True
pub=False
if pub or consegna:
    print('vieni o chiamaci')
  