"""
Ejercicio 6

Hacer un programa que pida un número por teclado y guarde en una lista su tabla
de multiplicar hasta el 10, por ejemplo, si digita el 5  la lista tendra 5,10,15,20,25,30,35,40,45,50.
"""
lista = []

numero = int(input("Ingrese el numero que desea multiplicar: "))

# ahora procedemos a multiplicar el numero obtenido con los numeros de la lista

for i in range(1,11):
    lista.append(i*numero)
print(lista)