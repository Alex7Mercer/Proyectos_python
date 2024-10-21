#Ejercicio 1

"""
Hacer un programa donde se debera imprimir por la consola la palabra con más caracteres
de dos palabras dadas, en el caso de que ambas palabras tangan la misma cantidad de palabras
decir son iguales.
"""
while True:
    Cadena1 = input("favor ingrese la primer cadena de caracteres: ")
    Cadena2 = input("favor ingrese la segunda cadena de caracteres: ")

    if len(Cadena1) < len(Cadena2):
        print(f"\nla cadena mas larga es: {Cadena2}")
        print()
    elif len(Cadena1) > len(Cadena2):
        print(f"\nla cadena mas larga es: {Cadena1}")
        print()
    else:
        print("\nSon iguales")
        print()
        break



