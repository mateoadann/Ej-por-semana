# Turno 02 – Enunciado 01 [T2E1]:

# Desarrolle un programa completo en Python, controlado por menú de opciones, que incluya las siguientes opciones:

# 1.) Ingrese los nombres de tres empresas dedicadas a la producción agrícola,
# e ingrese también las cantidades de trigo cosechadas por cada una en el último ciclo.
# Determine y muestre el nombre de la empresa que obtuvo la menor cosecha (y muestre también el valor de esa cosecha menor).
# Calcule y muestre además el porcentaje que la cosecha menor representa en el total cosechado entre las tres empresas.

# 2.)Ingrese por teclado una cadena de caracteres. Procese esa cadena a razón de un caracter por vuelta de ciclo,
# y determine cuántos de los caracteres eran letras 'w' (mayúscula o minúscula). Solamente si la cadena NO tiene la letra 'y' (minúscula)
# muestre ese conteo (cantidad de 'w'). Caso contario, muestre el mensaje: "La cadena tiene al menos una 'y' en minúscula".

# 3.)Terminar el programa.


opcion = 0

while opcion != 3:
    print()
    print('>' * 50)
    print('ESTE ES EL MENÚ DE OPCIONES...')
    print('=' * 50)
    print('OPCIÓN 1: Comparación entre tres empresas y sus cosechas. ')
    print('OPCIÓN 2: Análisis de caracteres. ')
    print('OPCIÓN 3: Salir. ')
    print()
    opcion = int(input('Seleccione una opción: '))

    if opcion == 1:
        print()
        print('EMPRESA N° 1: ')
        empresa_1 = input('Ingrese el nombre de la primera empresa -> ')
        cosecha_1 = float(input('Ingrese la cantidad de trigo cosechado :'))

        print()
        print('EMPRESA N° 2: ')
        empresa_2 = input('Ingrese el nombre de la segunda empresa -> ')
        cosecha_2 = float(input('Ingrese la cantidad de trigo cosechado: '))

        print()
        print('EMPRESA N° 3: ')
        empresa_3 = input('Ingrese el nombre de la tercera empresa -> ')
        cosecha_3 = float(input('Ingrese la cantidad de trigo cosechado: '))

        cosecha_total = cosecha_1 + cosecha_2 + cosecha_3

        if cosecha_1 < cosecha_2 and cosecha_1 < cosecha_3:
            cosecha_menor = cosecha_1
            print()
            print('La empresa que menos cosechó es', empresa_1, ',su cosecha fue de', cosecha_1, 'kg')

        elif cosecha_2 < cosecha_1 and cosecha_2 < cosecha_3:
            cosecha_menor = cosecha_2
            print()
            print('La empresa que menos cosechó es', empresa_2, ',su cosecha fue de', cosecha_2, 'kg')
        else:
            cosecha_menor = cosecha_3
            print()
            print('La empresa que menos cosechó es', empresa_3, ',su cosecha fue de', cosecha_3, 'kg')

        porcentaje = round(((cosecha_menor * 100) / cosecha_total), 2)
        print('El porcentaje de la menor cosecha es del', porcentaje, '%')

    elif opcion == 2:
        cadena = input('Ingrese una cadena de caracteres -> ')
        c_w = 0
        c_y = 0

        for caracter in cadena:
            if caracter == 'w' or caracter == 'W':
                c_w += 1

        for caracter in cadena:
            if caracter == 'y':
                c_y += 1

        if c_y > 0:
            print('La cadena tiene al menos una "Y" ')
        else:
            print('La cadena tiene', c_w, '"w"')

print(' -> FIN DEL PROGRAMA <- ')
