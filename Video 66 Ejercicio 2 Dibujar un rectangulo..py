"""
Capitulo 6 >> Funciones >> Ejercicio 2 >> Dibujar un rectangulo.

hacer un programa que pida la anchura y altura de un rectangulo con ayuda de una
función lo dibuje con *.
"""

def dibujar(ancho, alto):
    for i in range(alto):
        for j in range(ancho):
            print("* ",end= "")
        print()

ancho = int(input("Ingrese la anchura que desea tener: "))
alto = int(input("Ingrese la anchura que desea tener: "))

dibujar(ancho,alto)

