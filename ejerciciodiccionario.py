def crear_registro(lista,diccionario):
    lista.append(diccionario)
    return lista

def buscar(lista,indice,valor):
    for i in lista:
        if i[indice]==valor:
            return True,i
    return False,{}

def modificar(lista,indice,valor,nombre,carnet):
    for i in lista:
        if i[indice]==valor:
            if nombre!='':
                i['nombre']=nombre
            if carne!='':
                i['carne']=carnet
            return True
    return False

def eliminar(lista,indice,valor):
    for i in lista:
        if i[indice]==valor:
            lista.remove(i)
            return True
    return False

def realizar_pago(lista,carnet,mespagado,cantidad):
    registro={'carnet':carnet,'mes':mespagado, 'monto':cantidad}
    lista.append(registro)

def consultar_pagos(lista,carnet):
    listadepagos=[]
    for i in lista:
        if i['carnet']==carnet:
            listadepagos.append(i)
    return listadepagos