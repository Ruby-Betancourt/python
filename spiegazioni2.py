#calcoli matematici con operatori binari e unari

#con valori int e float
somma=2+3 #bi 
print(somma)
a=10
a+=5 #un 
print(a)
sott=5.5-3.5 #bi
print(sott)
a-=5
print(a)

#con variabili
b=2
molt=a*b #bi
molt*=b #un
div=a/b #bi
div/=b

#con stringhe
nome ="Ru" + "by"
print(nome)
print("Ru"+"by")
print("Il mio nome è " + nome)

#misto  valori e stringhe
x=3
y="2"
#z=x+y errore!!
z= str(x) + y #da una stinga '32'
print(z)
z= x + int(y) #fa la somma aritmetica
print(z)
