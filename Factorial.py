#Escriba un programa que calcule el factorial de un número
#El usuario debe ingrgesar el número
#El progrma debe mostrar el resultado

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

numero = int(input("Ingresa un número entero para calcular su factorial: "))

if numero < 0:
    print("El factorial no está definido para números negativos.")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:
    print("El factorial de", numero, "es", factorial(numero))
