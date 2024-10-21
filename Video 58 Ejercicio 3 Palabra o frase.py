#Ejercicio 3 Palabra o frase palindroma.

cadena = input("Ingrese la frase a analizar: ")

#Quitamos los espacios en blanco de la cadena.
cadena = cadena.replace(' ','')

# Segundo invertimos la cadena.
cadena2 = cadena[::-1] # con este algoritmo revertimos las palabras.

print(f"La cadena invertida es: {cadena2} ")

if cadena == cadena2:
    print(f"La palabra {cadena} es una palabra palindroma ")
else:
    print(f"La palabra {cadena} no una palabra palindroma ")