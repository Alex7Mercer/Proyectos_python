"""
Hacer un programa que pida una cadena por teclado, luego meta los caracteres
en una lista sin repetir caracteres
"""


Cadena = input("Ingrese caracteres a almacenar: ")
Lista = []


for i in Cadena:
    if i not in Lista:
        Lista.append(i)

print(f"\na continuación te mostramos la lista da caracteres sin repetir: \n{Lista} ")


