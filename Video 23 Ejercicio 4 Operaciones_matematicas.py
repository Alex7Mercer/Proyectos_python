'''
Condicionales - Ejercicio 4:
Construir un programa que simule el funcionamiento de una calculadora
que puede realizar las cuatro operaciones aritméticas básicas
(suma, resta, multiplicación y división). El usuario debe especificar la
operación con el primer carácter  del nombre de la operación.
S, s – Suma
R, r – Resta
P, p, M, m – Multiplicación
D, d - División
'''

print("\ndatos a tener en cuenta")

print("\nS, s – Suma")
print("R, r – Resta")
print("P, p, M, m – Multiplicación")
print("D, d - División")

Tipo_operac = input("\nFavor indique la operación a realizar: ")
Num1 = float(input("\nFavor indique el primer numero: "))
Num2 = float(input("Favor indique el segundo numero: "))

if Tipo_operac=='S' or Tipo_operac=='s':
    Res_Operacion = (Num1+Num2)
    print(f"El resultado es: {Res_Operacion} ")

elif Tipo_operac=='R' or Tipo_operac=='r':
    Res_Operacion = (Num1 - Num2)
    print(f"\nEl resultado es: {Res_Operacion} ")

elif Tipo_operac=='P' or Tipo_operac=='p' or Tipo_operac=='M' or Tipo_operac=='m':
    Res_Operacion = (Num1 * Num2)
    print(f"\nEl resultado es: {Res_Operacion} ")

elif Tipo_operac=='D' or Tipo_operac=='d':
    Res_Operacion = (Num1 / Num2)
    print(f"\nEl resultado es: {Res_Operacion} ")

else:
    print("\nEl caracter ingresado es incorrecto")



