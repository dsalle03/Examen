lista = [18, 50, 210, 80, 145, 333, 70, 30]

def recorrer(lista):
    print("Los números multiplos de 10 y menores de 200 son:")
    for i in lista:
        if i%10 == 0:
            if i < 200:
                print(i)
    print("Recorremos la lista hasta llegar a un número mayor que 300:")
    for i in lista:
        if i < 300:
            print(i)
        else:
            break
    

recorrer(lista)

