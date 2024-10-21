'''
Escriba un programa donde cree una lista con los siguientes personajes del Señor
de los anillos.

Nombre: Aragorn
Clase: Guerrero
Raza: Dúnadan del Norte

Nombre: Gandalf
Clase: Mago
Raza: Istar

Nombre: Legolas
Clase: Arquero
Raza: Elfo Sindar
'''

Personajes = [] # creando lista vacia

# de esta manera metemos diccionarios en una lista.

P1 = {"Nombre" : "Aragorn" , "Clase" : "Guerrero" , "Raza" : "Dúnadan del Norte"}
Personajes.append(P1)  # Agregamos el personaje a la lista.

P2 = {"Nombre" : "Gandalf" , "Clase" : "Mago" , "Raza" : "Istar"}
Personajes.append(P2)  # Agregamos el personaje a la lista.

P3 = {"Nombre" : "Legolas" , "Clase" : "Arquero" , "Raza" : "Elfo Sindar"}
Personajes.append(P3)  # Agregamos el personaje a la lista.

print(Personajes)