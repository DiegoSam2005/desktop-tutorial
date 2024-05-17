'''
r=float(input("Ingrese el radio: "))
areacirc=3.1416*r**2
print("El area del circulo es: ", areacirc)
base=float(input("Ingrese la base: "))
altura=float(input("Ingrese la altura: "))
arearec=base*altura
print("El area del rectangulo es:", arearec)

def area_circunferencia(radio):
    area=3.1416*(radio**2)
    return area

r=float(input("Ingrese el radio: "))
area_recibida=area_circunferencia(r)
print("El area de la circunferencia es: ", area_recibida)

def area_circunferencia():
    radio=float(input("ingrese el radio de la circunferencia"))
    return 3.1416*(radio**2)

def area_rectangulo(base, altura):
    return base*altura    

b=float(input("Ingrese la base del rectangulo: "))
h=float(input("Ingrese la altura del rectangulo: "))
area_recibida=area_rectangulo(b, h)
print("El area del rectangulo es: ", area_recibida)
'''

def area_circunferencia():
    radio=float(input("Ingrese el radio de la circunferencia: "))
    return 3.1416*radio**2
    

def area_rectangulo():
    base=float(input("Ingrese la base del rectángulo: "))
    altura=float(input("Ingrese la altura del rectángulo: "))
    return base*altura
     
# ---------- còdigo principal ----------
opcion=input("area circunferencia ingrese 1, area rectangulo ingrese 2: ")
if opcion=="1":
    area_recibida=area_circunferencia()
elif opcion=="2":
    area_recibida=area_rectangulo()
else:
    print("Opción incorrecta")
    area_recibida=0
print("El área es: ", area_recibida)