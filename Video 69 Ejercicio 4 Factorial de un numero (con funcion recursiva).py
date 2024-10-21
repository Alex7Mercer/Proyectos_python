# Video 69 -Factorial de un numero (con funcion recursiva)

#Desarrollar un programa para calcular el factorial de un numero
#con ayuda de una funcion recursiva.

#Un factorial es la multiplizacion de un numero hasta la unidad ejemplo el
# factorial de 5! = 5*4*3*2*1 => 120

def calcular_factorial(num):
    if num>0:
        resultado = num * calcular_factorial(num-1)
    else:
        resultado = 1

    return resultado
valor = calcular_factorial(5) # para saber el valor almacenado en una funcion debemos guardarla en una variable.
print(valor)