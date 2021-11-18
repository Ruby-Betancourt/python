#le Liste
#nome=[elem_1,...,elem_n]
alcolici=['mojito','white spriz','cosmopolitan']
analcolici=['limonata','gazosa']

print(alcolici) #tutta gli el
print(alcolici[1]) #uno solo

#len(nome_lista)
quantita_drink= len(alcolici) #misura lunghezza della lista

#nome_lista.append(elem)
alcolici.append('hugo') #aggiunge un elemento alla FINE della lista

#nome_lista.insert (posizione, elemento)
alcolici.insert(2, 'martini') #aggiunge un elemento in una posizione specifica della lista

#nome_lista.remove(elemento)
alcolici.remove('white spriz') #elimina un elemento nella lista

#nome_lista.pop(posizione)
alcolici.pop(2) #elimina un elemento in base alla posizione nella lista

#nome_lista[posizione]=elemento
alcolici[0]='spriz'

#nome_lista.sort()
alcolici.sort() #ordina gli elementi in ordine alfabetico 

drink=analcolici+alcolici #unisce gli elementi di diverse liste in una sola

if 'spriz' in alcolici:
    print('bevando disponibile')
    