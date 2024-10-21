"""
Capitulo 6 >> Funciones >> Ejercicio 3 >> Menu para clientes.

Crear un programa que tenga una lista de clientes, cada cliente tiene su
Nombre, apellido y DNI. El programa tendrá el siguiente menú de opciones.

1. Agregar nuevo cliente.
2. Mostrar todos los clientes.
3. Mostrar cliente por DNI.
4. Eliminar cliente.
5. Salir.

PD: Cada opción de menú se realizará con una función.
"""
# def para opción 1
def agregar_cliente(clientes,nombre,apellido,cedula):
    cliente = {}
    cliente['nombre'] = nombre
    cliente['apellido'] = apellido
    cliente['cedula'] = cedula
    clientes.append(cliente)

# def para opción 2
def mostrar_clientes(clientes):
    for i in clientes:
        print(f"Nombre: {i['nombre']}, Apellido: {i['apellido']}, Cedula: {i['cedula']} ")

# def para opción 3
def mostrar_cliente(cliente, cedula):
    for i in cliente:
        if i['cedula'] == cedula:
            print(f"Nombre: {i['nombre']}, Apellido {i['apellido']}, Cedula {i['cedula']} ")
            return True
    return False

# def para opción 4
def eliminar_cliente(clientes, cedula):
    for i in clientes:
        if i['cedula'] == cedula:
            clientes.remove(i)
            return True
        return False

clientes = [] # creamos la lista

while True:
    Opcion = print("""
.:Menú:.
1. Agregar nuevo cliente.
2. Mostrar todos los clientes.
3. Mostrar cliente por cedula.
4. Eliminar cliente.
5. Salir.
""")

    Opcion = int(input("Digite una opción de menu: "))

    print()

    if Opcion == 1:
        nombre = input(f"Favor ingrese nombre: ")
        apellido = input(f"Favor ingrese su apellido: ")
        cedula = input(f"Favor ingrese su Cedula: ")
        agregar_cliente(clientes, nombre, apellido, cedula)


    elif Opcion == 2:
        mostrar_clientes(clientes)

    elif Opcion == 3:
        cedula = input("Favor ingrese la cedula del cliente: ")
        if mostrar_cliente(clientes, cedula):
            print("Cliente encontrado en base ")

        else:
            print("cliente no encontrado en base ")

    elif Opcion == 4:
        cedula = input("Favor ingrece la cedula del cliente: ")
        if eliminar_cliente(clientes, cedula):
            print("cliente eliminado")
        else:
            print("Eliminación incorrecta")

    elif Opcion==5:
        print("!!Usted ha salido de la plataforma.!!")
        break
    else:
        print("Opción incorrecta")







