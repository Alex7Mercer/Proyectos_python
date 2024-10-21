'''Escriba un programa donde tenga una lista y que, a continuación,
elimine los elementos repetidos, por último mostrar la lista.'''


Lista = ["Cama", "Apartamento_propio", "Moto", "Computador", "Carro", "Nevera", "Lavadora", "Mesa", "Armario", "Moto", "Lavadora"]

# para no tener elementos repetidos hacemos uso mejor de Conjuntos (intersante para listados grandes)

conjunto = set(Lista) # con esto ya borramos los datos duplicados.

Lista = list(conjunto)

# Lista = list(set(Lista)) >> Hace lo mismo pero en lugar de dos renglones lo hace en uno.


print(Lista)



