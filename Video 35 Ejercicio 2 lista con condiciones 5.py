'''
Escriba un programa que tenga dos listas y que, a continuación, cree las siguientes listas (en las que no debe haber repeticiones):

- Lista de elementos que aparecen en las dos listas.
- Lista de elementos que aparecen en la primera lista, pero no en la segunda.
- Lista de elementos que aparecen en la segunda lista, pero no en la primera.
- Lista de elementos que aparecen en ambas listas.
'''

Lista1 = [1,2,3,4,2,1,9]
Lista2 = [8,4,2,5]

# Elimino los duplicados en cada lista
a = set(Lista1)
b = set(Lista2)

Union = (a | b)
SoloA = (b - a)
SoloB = (a - b)
Interceccion = (a & b)

print(f"Lista de elementos que aparecen en las dos listas {Union} ")
print(f"Lista de elementos que aparecen en la primera lista, pero no en la segunda. {SoloA}")
print(f"Lista de elementos que aparecen en la segunda lista, pero no en la primera. {SoloB}")
print(f"Lista de elementos que aparecen en ambas listas {Interceccion}")
