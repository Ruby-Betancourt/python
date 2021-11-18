#dichiarazioni variabili
nome_barman = 'Aj bot'
drink_speciale = "DigitalVodka"
prezzo_drink = 5.5
alcolici=['mojito', 'white russian', 'caipirinha']
analcolici=['limonata','gazosa']

#Inizio del programma
print("Benvenuto al Pub Drink&Codici")
print('Mi chiamo '+nome_barman+' ...e sono pronto a servirti =)')
print('Il drink più cool del nostro pub è: '+str(drink_speciale))
print('Provalo subito, al modico prezzo di: '+str(prezzo_drink))
print('\nI drink alcolici sono '+str(len(alcolici)))
print('\nI drink analcolici sono '+str(len(analcolici)))

#inizio delle domande
print('\nInserisci il tuo anno di nascita')
anno_nascita = int (input())
anni_cliente = 2021 - anno_nascita
print('Hai '+str(anni_cliente)+' anni')

drink_disponibili=[]
if anni_cliente<18:
    print('\nSei minorenne puoi ordinare sono analcolici')
    drink_disponibili+=analcolici
else:
    print('\nSei maggiorenne puoi ordinare ciò che vuoi')  
    drink_disponibili=analcolici+alcolici

while True:
    print('ecco i drink consigliati per te:')
    for drink in drink_disponibili:
        print(drink)
    drink_scelto=input()
    if drink_scelto in drink_disponibili:
        print('hai scelto '+drink_scelto+'. Buon aperitivo!')
        break
    else:
        print('Mi dispiace, '+drink_scelto+' non è disponibile =(')    