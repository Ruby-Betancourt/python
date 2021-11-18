#ciclo for

#con le liste
#for element(nomesceltodanoiacaso) in nome_lista:  (\n)fai qualcosa

alcolici=['a','b','c']
for alcolico in alcolici:
    print(alcolico)

for x in alcolici:
    if x=='b':
        break #comando per forzare l'uscita immediata dal for 
    print(x)

for element in alcolici:
    if element=='b':
        continue #comando per interrompere il ciclo attuale e passare al successivo del for  
    print(element)   

#con le stringhe
for az in 'stringa':
    print(az) #stampa lettera per lettera 

#con gli insiemi(?)/numeri
for numero in range (1,19):#NOTA (1,19) è l'insieme da 1 a 18
    print(numero)