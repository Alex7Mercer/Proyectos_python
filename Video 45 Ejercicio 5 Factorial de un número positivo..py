"""
Ejercicio 5
Hacer un programa para calcular el factorial de un numero positivo.
"""

numero = int(input("Ingrese el numero el cual desea calcular su factorial: "))
while numero<0: # mientras el numero sea negativo.
    print("Erorr -> Favor ingrese un numero positivo")
    numero = int(input("Ingrese el numero el cual desea calcular su factorial: "))


# ahora vamos a calcular el factorial.
factorial = 1

for i in range(1,numero+1):
    factorial *=i
print(f"el Factorial del {numero} es {factorial}")

