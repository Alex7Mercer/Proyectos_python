#Sumar digitos de un numero.

def SumarDigitos(num):
    if num==0: # Caso Base
        resultado = 0
    else: # Caso recursivo.
        resultado = SumarDigitos(int(num/10)) + (num%10) # recordemos que el int hace que nuestra division no tenga en cuenta los decimas.


    return resultado

Valor = SumarDigitos(646)
print(Valor)
