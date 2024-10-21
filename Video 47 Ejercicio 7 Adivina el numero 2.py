"""
Ejercicio 7

realizar un juego para adivinar un número, para ello generar un numero aleatorio entre
0 - 100 y luego ir pidiendo numeros indicando es "mayor" o es "menor" segun sea mayor
o menor con respecto a N el proceso termina cuando el usuario acierta y mostrar el
número de intentos.
"""

import random

aleatorio = random.randint(1,10) # Generamos un número en aleatorio

print(f"\n\t.:Juego adivina el número:.")
contador = 0
while True:
    numero = int(input("\nFavor ingresa un número: "))
    contador +=1
    print(f"\n\tIntento {contador} fallido")
    if numero>aleatorio:
        print("\tNo No No No No No....")
    elif numero<aleatorio:
        print("\tNo No No No No No....")
    else:
        print(f"\n\t¡¡¡HAS ADIVINADO!!! {aleatorio}")
        break # con esto rompemos el bucle while

print(f"\n\tlograste adivinar el número despuès de {contador} intentos ")