"""
Ejercicio 4

Hacer un programa donde se remplacen todos los espacios de una cadena por astericos
y ademas cada palabra comience por una mayuscuala.
"""

Cadena = input("Favor ingrese una frase: ")
Cadena = Cadena.replace(' ', '*') # remplazamos los espacios por astericos.
print(Cadena)
print()
Cadena = Cadena.title() # pasamos la primera letra de cada palabra a mayuscula.

print(Cadena)
