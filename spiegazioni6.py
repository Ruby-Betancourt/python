#ciclo while
a=1
while a<5:
    print('tigre')
    a+=1

while True: #condizione true fa andare avanti all'infinito finchè non ho la risposta giusta e avviene il break
    print('Che fa u uccellino dentro un computer?')
    risposta=input()
    if risposta=='chip':
        print('risposta esatta')
        break
    else:
        print('ritenta\n')
