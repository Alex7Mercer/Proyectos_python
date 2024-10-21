"""
Hacer un programa donde el usuario ingrese una frase, la cual se debolver la misma frase
pero sin espacios en blanco y ademas un indicar cuantos caracteres tiene la frase
(Sin contar los espacios en blanco).

"""

Frase = input("Ingrese una frase, nuestro codigo se la devolvera sin espacios: ")
Frase2 = " "

for i in Frase:
    if i!=" ":
        Frase2 += i

Frase = Frase2

print(f"Resultado: {Frase} ")
print(f"Numero de caracteres: {len(Frase)} ")



