## Hacer un programa que pida 2 números y se de cuenta cuál de ellos es par, o si ambos lo son.

Num1 = int(input(f"Ingrese el valor numero uno: "))
Num2 = int(input(f"Ingrese el valor numero dos: "))

if Num1%2==0 and Num2%2==0:
    print("Ambos numeros son pares")
elif Num1%2==0 and Num2%2!=0:
    print(f"{Num1} es par")
elif Num1%2!=0 and Num2%2==0:
    print(f"{Num2} es par")
else:
    print("ambos números son impares")
