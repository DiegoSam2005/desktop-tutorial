#Listas
milistanombres=[]
while True:
    nombre=input('Dame un nombre: ')
    if nombre == "Salir":
        break
    milistanombres.append(nombre)
#Buscar un nombre de la lista
nombrebuscar=input("Dame un nombre a buscar: ")
if nombrebuscar in milistanombres:
    print("El nombre esta en la lista")
else:
    print("El nombre no esta en la lista")
#Modificar un nombre
nombreamodificar=input("Dame un nombre a modificar: ")
if nombreamodificar in milistanombres:
    indice=milistanombres.index(nombreamodificar)
    nuevonombre=input("Dame el nuevo nombre: ")
    milistanombres[indice]=nuevonombre
#Borrar un nombre de la lista
nombreaborrar=input("dame un nombre a borrar: ")
if nombreaborrar in milistanombres:
    milistanombres.remove(nombreaborrar)
print(milistanombres)