#ciclos en python
"""
El ciclo for esta diseñado para realizar una tarea un numero determinado de veces (predefinido).
El ciclo while se utiliza cuando no se sabe cuantas veces se va a repetir una tarea.

#Ciclo for
for variable in range(11,1):
    print(variable)
"""
    
#Ciclo while
respuesta='s'
while True:
    respuesta=input('Desea ingresar un valor? (s/n): ')
    if respuesta=='s':
        nombre=input('Nombre: ')
        correo=input('Correo: ')
        tel=input('Telefono: ')
    else:
        break
print(nombre)
print(correo)
print(tel)
