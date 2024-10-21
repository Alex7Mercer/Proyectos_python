## Hacer un programa que pida 3 números y determine cuál es el mayor.

Num1 = int(input("Ingrese el numero uno: "))
Num2 = int(input("Ingrese el numero dos: "))
Num3 = int(input("Ingrese el numero tres: "))

if Num1>=Num2 and Num1>=Num3:
    print(f"El numero mayor es: {Num1}")
elif Num2>=Num1 and Num2>=Num3:
    print(f"El numero mayor es: {Num2}")
elif Num3>=Num1 and Num3>=Num2:
    print(f"El numero mayor es: {Num3}")




