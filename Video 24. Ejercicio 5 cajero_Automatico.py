'''
Hacer un programa que simule un cajero automático con un saldo inicial de $1000 y tendrá
el siguiente menú de opciones:

1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir
'''

Saldo = 1000

print("\t \n .:Menu:.")
print("\n1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")

Opcion = int(input(f"\nFavor ingrese la opción que necesite:  "))

if Opcion ==1:
    Extra = float(input(f"\nFavor ingrese que el valor a agregar a la cuenta:  " ))
    Saldo = Saldo + Extra
    print(f"Saldo en cuenta  {Saldo:.2f}")

elif Opcion ==2:
    Retiro = float(input(f"\nIngrese el valor que desea retirar de la cuenta:  " ))
    if Retiro>Saldo:
        print("\n .:No cuenta con esa cantidad en la cuenta:.")
    Saldo = Saldo - Retiro
    print(f"El Dinero restante que queda en la cuenta es de: {Saldo}")

elif Opcion ==3:
    print(f"\n \tEl saldo actual en la cuenta es de: {Saldo} ")

elif Opcion ==4:
     print("\n \t Su transacción a terminado")

else:
    print("\n \t El valor ingresado es incorrecto")
