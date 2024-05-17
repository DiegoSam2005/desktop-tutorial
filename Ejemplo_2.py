"""
base=0
altura=0
base=input("Ingrese la base del triangulo: ")
base=float(Base)
altur=input("Ingresse la altura del triangulo: ")
altura=float(altura)
area=base*altura
perimetro=(2^base)*(2^altura)
print("El area del triangulo es: ")
print(area)
print("El perimetro del triangulo es: ")
print(perimetro)
"""
"""
radio=0
pi=3.1416
radio=input("Ingrese el valor del radio")
radio=float(radio)
area=pi*radio**2
perimetro=pi*radio*2
print("El area del circulo es: ")
print(area)
print("El perimetro del circulo es: ")
print(perimetro)
"""
"""
#crear las variables para los catetos
cateto1=0
cateto2=0
#pedir los valores de los catetos
cateto1=float(input("ingrese el valor del cateto 1: "))
cateto2=float(input("Ingrese el valor del cateto 2: "))
#calcular la hipotenusa
hipotenusa=(cateto1**2+cateto2**2)**(1/2)
#mostrar el resultado
print("La hipotenusa es: ", hipotenusa)
#operadores aritmeticos: suma= + division= / multiplicacion= * potencia= ** raiz= **(1/2)
"""
"""
#Calcular el año de nacimiento de una persona, pidiendo su nombre y edad
nombre=0
edad=0
año_actual=2024
edad=float(input("ingrese su edad: "))
nombre=input("ingrese el nombre de su persona: ")
año_de_nacimiento=año_actual- edad
print("La siguiente persona nacio en este año: ", nombre, año_de_nacimiento)
"""
"""
#Verificar si una persona es mayor de edad o no por su año de nacimiento
anlonac=int(input("Ingrese el año de nacimiento: "))
edad=2024-anlonac
if edad>=18:
    print("Es mayor de edad")
else:
    print("Es menor de edad, ya que tiene ", edad, "años")
"""