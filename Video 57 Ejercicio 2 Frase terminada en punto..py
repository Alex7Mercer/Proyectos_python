"""
Ejercicio 2

Hacer un programa para detectar si una frase introducida por el usuario finaliza en punto
"." o no. Deberas imprimir por la consola una de las siguientes opciones: "Termina con un
punto" o por el contrario "No termina con un punto"
"""
while True:
    Frase = input("Ingrese la palabra a analizar: ")

    if Frase.endswith('.'):
        print("la frase termina en punto")
    else:
        print("la frase no termina  en punto")
        break



