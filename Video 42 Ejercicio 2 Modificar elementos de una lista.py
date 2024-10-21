'''
Llenar una lista con los numeros del 1 al 10, luego de modificar los
elementos de una lista multiplicandolos por un valor que el usuario digite
'''

lista = []

lista = list(range(0,11))
print(f"lista: ")
for i in lista:
    print(i,end="-")

valor = int(input(f"\ningrese un digito a multiplicar: "))

#ahora procedemos a multiplicar todos los elementos de la lista

indice = 0
for i in lista:
    lista[indice] *=valor
    indice +=1

#Una forma más facil de hacer lo mismo es de la siguiente manera.

#for indice,i in enumerate(lista):   #esto gracias a la función enumerate.
#   lista[indice] *=valor



#Aqui ya mostramos el resultado.
print(f"\nEl resultado con los elementos multiplicados es {valor} ")
for i in lista:
    print(i,end="-")
