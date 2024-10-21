"""
Ejercicio 4

Hacer un programa para sumar números pares dentro de un rango

Ejemplo:

suma de numeros pares de 2 al 30
Suma 240
"""

a = int(input(f"\nDigite de donde va a comenzar a sumar: "))
b = int(input(f"\nDigite de donde quiere llegar a sumar: "))
suma = 0

for i in range(a,b+1):
    if i%2==0: # Si el numero es par (es como el MOD en pseint)
        suma += i
print(f"\nla suma dentro del rango es: {suma}")