"""
pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar,
por ultimo, muestra los números ordenados de menor a mayor.
"""

lista = []

salir = False

while not salir:
    numero = int(input("Digite un numero: "))
    if numero==0:
        salir = True
        print(lista)
    else:
        lista.append(numero)

lista.sort()
print(f"\nahora te comparto la lista ordenada:\n{lista}")