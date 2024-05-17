#Crear un codigo que pida correo, nombre y carnet; lo tiene que devolver al flujo otra vez y se tiene que guawrdar en tres variables distintas
#Debe de llamar las variables: Carnet, Nombre y Correo.
#Debe de devolver la informacion recibida
def informacion_del_alumno():
    carnet=int(float(input("Ingrese su carnet de estudiante: ")))
    nombre=input("Ingrese su nombre : ")
    correo=input("Ingrese su correo de estudiante: ")
    return carnet, nombre, correo

#Desde el programa inicial se manda a llamar a esta funcion y se imrpimen los valores recibidos
respuesta='s'
while True:
    respuesta=input('Desea ingresar un valor? (s/n): ')
    if respuesta=='s':
        ca,n,co=informacion_del_alumno()
        print('El carnet del alumno es: ',ca)
        print('El nombre del alumno es:',n)
        print('El correo del alumno es: ',co)
    else:
        break
print(ca)
print(n)
print(co)
