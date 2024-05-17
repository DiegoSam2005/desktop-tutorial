#Diccionarios
'''
Los diccionarios son una estructura de datos que permite almacenar pares de valores clave-valor.

diccionario_estudiantes = {'Carnet':123, 'Nombre':'Juan', 'correo':'juanperez@miumg.edu.gt'}
print(diccionario_estudiantes['Carnet'])
print(diccionario_estudiantes['Nombre'])
print(diccionario_estudiantes['correo'])
#Modificar un elemento dentro del diccionario
diccionario_estudiantes['Nombre']='Jose'
print(diccionario_estudiantes)
'''
listado=[{'carnet':1, 'nombre':'Juan', 'correo':'Jlango@.com'}
         {'carnet':2, 'nombre':'Marta', 'correo':'Mmartinez@.com'}
         {'carnet':3, 'nombre':'Cesar', 'correo':'Clopez@.com'}
        ]
#datos={'carnet':'', 'nombre':'', 'correo':''}
'''while True:
    datos['carnet']=input('Ingrese carnet: ')
    datos['nombre']=input('Ingrese nombre: ')
    datos['correo']=input('Ingrese correo: ')
    listado.append(datos.copy())
    salir=input('Desea salir? (s/n): ')
    if salir.lower()=='s':
        break
print(listado)'''
correobuscado='Jlango@.com'
for i in listado:
    if i['nombre']==correobuscado:
        print('Correo encontrado')
        print('Los datos son: ',i)
