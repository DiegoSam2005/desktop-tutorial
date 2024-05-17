'''
import modulodiccionarios as md
listado=[{'carnet':1, 'nombre':'Juan', 'correo':'Jlango@.com'},
         {'carnet':2, 'nombre':'Marta', 'correo':'Mmartinez@.com'},
         {'carnet':3, 'nombre':'Cesar', 'correo':'Clopez@.com'},
         {'carnet':4, 'nombre':'Antonio', 'correo':'Amunguia@.com'},
         {'carnet':5, 'nombre':'Mirian', 'correo':'MIestrada@.com'},
        ]

existe,registro=md.buscar(listado,'carnet','3')
if existe:
    print('El registro existe: ', registro)

borro=md.eliminar(listado,'carnet','5')
if borro:
    print(listado)

nuevo={'carnet':6, 'nombre':'Pepe', 'correo':'Pmartinez@.com'}
md.crear_registro(listado,nuevo)
print('\n \n',listado)

modifico=md.modificar(listado,'carnet','6','Mary','')
print('\n \n',listado)
'''
import modulodiccionarios as md
listado=[{'carne': '1', 'nombre': 'Raul', 'correo': 'rrendonp@miumg.edu.gt'},
          {'carne': '2', 'nombre': 'Carlos', 'correo': 'carlosc@miumg.edu.gt'},
          {'carne': '3', 'nombre': 'Raquel', 'correo': 'rmolina32@miumg.edu.gt'},
          {'carne': '4', 'nombre': 'Pedro', 'correo': 'pmujia@miumg.edu.gt'},
          {'carne': '5', 'nombre': 'Marta', 'correo': 'mtortola@miumg.edu.gt'}
        ]
pagos=[]

'''
existe,registro=md.buscar(listado,'carne','3')

if existe:
    print('El registro existe:',registro)
borro=md.eliminar(listado,'carne','5')
if borro:
    print(listado)
nuevo={'carne': '6', 'nombre': 'Maria', 'correo': 'mmorales@miumg.edu.gt'}
md.crear_registro(listado,nuevo)
print('\n \n',listado)

modifico=md.modificar(listado,'carne','6','Mary','')
print('\n \n',listado)
'''
while True:
    print('1. Registrar pago')
    print('2. Consultar pagos de un estudiante')
    print('3. Agregar un estudiante')
    print('4. Modificar un estudiante')
    print('5. Eliminar un estudiante')
    print('6. Consultar datos de un estudiante')
    print('10. Salir')
    opcion=input('Seleccione una opcion:')
    if opcion=='1':
        carnet=input('Ingrese el carne del estudiante que realiza pago: ')
        existe,registro=md.buscar(listado,'carne',carnet)
        if existe:
            mes=input('Ingrese el mes que realiza el pago: ')
            monto=float(input('Ingrese el monto del pago: '))
            md.realizar_pago(pagos,carnet,mes,monto)
        else:
            print('El estudiante no existe')
    elif opcion=='2':
        carne=input('Ingrese el carne:')
        lista_pagados=md.consultar_pagos(pagos,carne)
        print('Pagos realizados por el estudiante:')
        for i in lista_pagados:
            print(i)
    elif opcion=='3':
        carne=input('Ingrese el carne del estudiante: ')
        nombre=input('Ingrese el nombre del estudiante: ')
        correo=input('Ingrese el correo del estudiante: ')
        nuevo={'carne':carne,'nombre':nombre,'correo':correo}
        md.crear_registro(listado,nuevo)
    elif opcion=='4':
        carne=input('Ingrese el carne del estudiante a modificar: ')
        existe,registro=md.buscar(listado,'carne',carne)
        if existe:
            nombre=input('Ingrese el nuevo nombre: ')
            correo=input('Ingrese el nuevo correo: ')
            md.modificar(listado,'carne',carne,nombre,correo)
        else:
            print('El estudiante no existe')
    elif opcion=='5':
        carne=input('Ingrese el carne del estudiante a eliminar: ')
        existe,registro=md.buscar(listado,'carne',carne)
        if existe:
            md.eliminar(listado,'carne',carne)
        else:
            print('El estudiante no existe')
    elif opcion=='6':
        carne=input('Ingrese el carne del estudiante a consultar: ')
        existe,registro=md.buscar(listado,'carne',carne)
        if existe:
            print('Datos del estudiante:')
            print(registro)
        else:
            print('El estudiante no existe')
    elif opcion=='10':
        break
    else:
        print('Opcion incorrecta')