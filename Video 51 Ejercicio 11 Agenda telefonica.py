"""
Hacer un programa que simule una agenda de contactos. Crear un diccionario donde
la clave sea el numero de usuario y el valor sea el numero de telefono.

El programa tendra el siguiente menu de opciones.

1. Nuevo contacto.
2. Borrar contacto.
3. Ver contactos existentes.
4. Salir.
"""

agenda = {}

while True:
    print(f"""\t.:Menu:.
1. Nuevo contacto
2. Borrar contacto
3. Ver contactos existentes
4. Salir
    """)
    Opcion = int(input("Digite una opción de menu: "))

    print()

    if Opcion ==1:
        nombre = input("Nombre de contacto: ")
        telefono = input("Numero de telefono: ")

        if nombre not in agenda:
            agenda[nombre] = telefono #agregamos el dato a nuestra agenda.
            print("\n!!Contacto agregado exitosamente!!")
        else:
            print("\nEse nombre de contacto ya exite")

    elif Opcion==2:
        nombre = input("favor ingrese el nombre del contacto a eliminar")

        if nombre in agenda:
            del(agenda[nombre])
            print("\nContacto eliminado")
        else:
            print("Ese dato no existe")

    elif Opcion == 3:
        print("Agenda de contactos")
        print(agenda)

    elif Opcion == 4:
        print(f"\nA salido de la opción contactos")
        break

    else:
        print("\nOpción ingresada incorrecta")

    print()


