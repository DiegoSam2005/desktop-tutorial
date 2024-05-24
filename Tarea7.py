from os import system
def menu1():
    print('1. Convertir entre Km y millas')
    print('2. Convertir entre m3 y Pie3')
    print('3. Convertir entre pies, mts y yardas')
    print('10. Salir')
    opcion=int(input('Ingrese su opción: '))
    return opcion

def conversion_Km_millas(conversion, distancia):
    if conversion=='a':
        return distancia*0.62
    elif conversion=='b':
        return distancia*1.64

def conversion_mts_cubicos_pies_cubicos(convertir, medicion):
    if convertir=='a':
        return medicion*35.3147
    elif convertir=='b':
        return medicion*0.028

def conversion_pie_mts_yardas(conver, medidas):
    if conver=='a':#pie a metro
        return medidas*0.3048
    elif conver=='b':#metro a pie
        return medidas*3.28084
    elif conver=='c':#Yarda a metro
        return medidas*0.9144
    elif conver=='d':#Metro a yarda
        return medidas*1.09361
    elif conver=='e':#Pie a yarda
        return medidas*0.333333
    elif conver=='f':#Yarda a pie
        return medidas*3

while True:
    system('cls')
    op=menu1()
    if op==1:
        conv=input('Escriba a para km a millas, y b para millas a kim: ')
        conv=conv.lower()
        if conv!='a' and conv!='b':
            print('Debe elegir una opcion valida')
        else:
            if conv=='a':
                cant=float(input('Ingrese la cantidad de km: '))
                de_a=conversion_Km_millas(conv, cant)
                print(f'{cant} km son {de_a} millas')
                system('pause')
            else:
                cant=float(input('Ingrese la cantidad de millas: '))
                de_a=conversion_Km_millas(conv, cant)
                print(f'{cant} millas son {de_a} km')
                system('pause')
    elif op==2:
        conv=input('Escriba a para mts cubicos a pies cubicos, y b para pies cubicos a mts cubicos: ')
        conv=conv.lower()
        if conv!='a' and conv!='b':
            print('Debe elegir una opcion valida')
        else:
            if conv=='a':
                cant=float(input('Ingrese la cantidad de mts cubicos: '))
                de_a=conversion_mts_cubicos_pies_cubicos(conv, cant)
                print(f'{cant} mts cubicos son {de_a} pies cubicos')
                system('pause')
            else:
                cant=float(input('Ingrese la cantidad de pies cubicos: '))
                de_a=conversion_mts_cubicos_pies_cubicos(conv, cant)
                print(f'{cant} pies cubicos son {de_a} mts cubicos')
                system('pause')
    elif op==3:
        conv=input('Escriba a para pies a mts, b para mts a pies, c para yardas a mts, d para mts a yardas, e para pie a yarda, y f para yarda a pie: ')
        conv=conv.lower()
        if conv!='a' and conv!='b' and conv!='c' and conv!='d' and conv!='e' and conv!='f':
            print('Debe elegir una opcion valida')
        else:
            if conv=='a':
                cant=float(input('Ingrese la cantidad de pies: '))
                de_a=conversion_pie_mts_yardas(conv, cant)
                print(f'{cant} pies son {de_a} metros')
                system('pause')
            elif conv=='b':
                cant=float(input('Ingrese la cantidad de metros: '))
                de_a=conversion_pie_mts_yardas(conv, cant)
                print(f'{cant} metros son {de_a} pies')
                system('pause')
            elif conv=='c':
                cant=float(input('Ingrese la cantidad de yardas: '))
                de_a=conversion_pie_mts_yardas(conv, cant)
                print(f'{cant} yardas son {de_a} metros')
                system('pause')
            elif conv=='d':
                cant=float(input('Ingrese la cantidad de metros: '))
                de_a=conversion_pie_mts_yardas(conv, cant)
                print(f'{cant} metros son {de_a} yardas')
                system('pause')
            elif conv=='e':
                cant=float(input('Ingrese la cantidad de pies: '))
                de_a=conversion_pie_mts_yardas(conv, cant)
                print(f'{cant} pies son {de_a} yardas')
                system('pause')
            else:
                cant=float(input('Ingrese la cantidad de yardas: '))
                de_a=conversion_pie_mts_yardas(conv, cant)
                print(f'{cant} yardas son {de_a} pies')
                system('pause')
    elif op==10:
        break