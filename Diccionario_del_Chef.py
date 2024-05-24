list_platos=[]
plato={}
def agregar_plato():
    list_platos.append(plato)

def consultar_plato(nombre_plato):
    for i in list_platos:
        if i["nombre"]==nombre_plato:
            return True,i[listado_ingredientes]
    return None

def mostrar_Menu():
    print(list_platos)

def mostrar_menu():
    print("1. Agregar un plato")
    print("2. Consultar un plato")
    print("3. Eliminar un plato")
    print("4. Modificar un plato")
    print("5. Mostrar el menu")
    print("6. Salir")
    opcion=int(input("Dame una opcion: "))
    return opcion

# Programa principal
while True:
    op=mostrar_menu()
    print(op)
    if op==1:
        nombre_plato=input("Dame un plato: ")
        precio_plato=float(input("Dame un precio: "))
        categoria_plato=input("Tipo de plato: ")
        listado_ingredientes = []
        for ing in range(5):
            ingrediente = input("Ingrese el ingrediente, para salir escriba 0:")
        if ingrediente == '0':
            break
        listado_ingredientes.append(ingrediente)
        agregar_plato(nombre_plato, precio_plato, categoria_plato, listado_ingredientes)
    elif op==2:
        plato_consultado=input("Dame un nombre a buscar: ")
        if consultar_plato(plato_consultado):
            print("Plato: ",nombre_plato)
            print('***ingredientes***')
        else:
            print("El plato no se encuentra en el menu")
    elif op==3:
        nombreaborrar=input("Dame un nombre a borrar: ")
        if eliminarnombre(nombreaborrar):
            print("El nombre fue eliminado")
        else:
            print("El nombre no estaba en la lista")
    elif op==4:
        nombreamodificar=input("Dame un nombre a modificar: ")
        nuevonombre=input("Dame el nuevo nombre: ")
        if modificarnombre(nombreamodificar, nuevonombre):
            print("El nombre fue modificado")
        else:
            print("El nombre no estaba en la lista")
    elif op==5:
        mostrar_Menu()
    elif op==6:
        break
    else:
        print("Opcion no valida")
