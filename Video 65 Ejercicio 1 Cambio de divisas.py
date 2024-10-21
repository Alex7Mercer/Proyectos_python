"""
Capitulo 6 >> Funciones >> Ejercicio 1

Desarrollar un programa que pueda calcular el tipo de cambio de moneda (de tu moneda
hacia dolar  y viceversa).
"""
def Cambio_Pesos_Dolares(Pesos):
    return Pesos/3.716

def Cambio_Dolares_Pesos(Pesos):
    return Dolares*3.716

while True:
    print(""".:Menu:.
1. Convertir de pesos colombianos a Dolares.
2. Convertir de Dolares a pesos colombianos.
3. Salir.
""")
    Opcion = int(input("Digite una opción: "))
    print()

    if Opcion == 1:
        Pesos = float(input("Digite la cantidad de Pesos que desea convertir: "))
        print(f"Dólares >> ${Cambio_Pesos_Dolares(Pesos):.3f}")

    elif Opcion == 2:
        Dolares = float(input("Digite la cantidad de dólares que desea convertir: "))
        print(f"Pesos >> {Cambio_Dolares_Pesos(Dolares):.3f}")

    elif Opcion == 3:
        print("!!Gracias por utilizar nuestros servicios!!")
        break
    else:
        print("A ingresado una opción incorrecta")

print()