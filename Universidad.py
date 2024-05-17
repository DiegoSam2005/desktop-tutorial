#Debe de pedir carnet, nombre, DPI, gmail para saber si es estudiante o no
def estudiante():
    carnet=int(float(input("Ingrese su carnet de estudiante: ")))
    nombre=input("Ingrese su nombre : ")
    correo=input("Ingrese su correo de estudiante: ")
    return carnet, nombre, correo

def persona_no_estudiante():
    dpi=int(float(input("Ingrese su dpi: ")))
    nombre=input("Ingrese su nombre: ")
    return dpi, nombre

opcion=input("Informacion del estudiante ingrese 1, informacion de personas fuera de la universidad ingrese 2: ")
if opcion=="1":
    c, n, co=estudiante()
    print("Carnet: ", c)
    print("Nombre: ", n)
    print("Correo: ", co)
elif opcion=="2":
    d, n=persona_no_estudiante()
    print("DPI: ", d)
    print("Nombre: ", n)
else:
    print("Opcion no validad")
