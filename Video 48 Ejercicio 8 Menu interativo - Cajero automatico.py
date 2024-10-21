"""
Ejercicio 8

Hacer un programa que cimule un cajero automatico con un saldo inicial de $1000
y tendra el siguiente menu de opciones.

Opción 1. Ingrese du dinero a la cuenta
opción 2. retirar el dinero de la cuenta.
Opción 3. Mostrar el dinero disponible
opción 4. salir.
"""
Saldo = 1000

while True:
    print("\t \n .:Menu:.")
    print("\n1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")

    Opcion = int(input(f"\ningrese una opción de menu:  "))

    if Opcion ==1:
        Extra = float(input(f"\nFavor ingrese que desea agregar a la cuenta:  " ))
        Saldo = Saldo + Extra
        print(f"Saldo en cuenta  ${Saldo:.2f}")

    elif Opcion ==2:
        Retiro = float(input(f"\nIngrese el valor que desea retirar de la cuenta:  " ))
        if Retiro>Saldo:
            print("\n .:No cuenta con esa cantidad en la cuenta:.")
        Saldo = Saldo - Retiro
        print(f"El Dinero restante que queda en la cuenta es de: ${Saldo}")
    elif Opcion ==3:
        print(f"\n \tEl saldo actual en la cuenta es de: ${Saldo} ")
    elif Opcion ==4:
        print(f"Gracias por utilizar nuestros servicios")
        break
    else:
        print("\n \t El valor ingresado es incorrecto")

    print()
