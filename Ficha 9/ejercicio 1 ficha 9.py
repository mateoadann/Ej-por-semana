#     • 1. Ejercicio Tipo Parcial (Resuelto 1K14)
# Desarrollar un programa completo en Python, que a través de un menu de opciones, ejecute los siguientes puntos:
# 1) Ingresar el nombre de tres atletas, ademas ingrese también los tiempos que esos lograron en su actividad deportiva
# (expresados en segundos), informe cual fue el nombre del atleta que gano la competición,
# ademas indicar con un mensaje que si el tiempo del ganador es menor a 850 segundos batió el record de la actividad
# 2) Ingresar un texto, el mismo termina con punto, recorrer el texto caracter a caracter
# y determinar cuantas letras 'p' hay en el texto, cuantas letras 'j' hay en el texto.
# Ademas indique cual es el porcentaje que cada conteo representa sobre el total de caracteres del texto.
# 3) Terminar el Programa

opcion = 0
while opcion != 3:
    print('Opcion 1: Problema con \t atletas\n')
    print('Opcion 2 : Análisis de cadena de caracteres.\n')
    print('Opción 3: Salir. \n')
    opcion = int(input('Ingrese su opción:'))

    if opcion == 1:
        def ganador(atleta1, atleta2, atleta3, tiempo1, tiempo2, tiempo3):
            record = False
            if tiempo1 < tiempo2 and tiempo1 < tiempo3:
                winner = atleta1
                if tiempo1 < 850:
                    record = True
            elif tiempo2 < tiempo1 and tiempo2 < tiempo3:
                winner = atleta2
                if tiempo2 < 850:
                    record = True
            elif tiempo3 < tiempo1 and tiempo3 < tiempo2:
                winner = atleta3
                if tiempo3 < 850:
                    record = True
            else:
                return 'Hay empate...'

            if record:
                return 'El ganado es', winner, ' y también batió el record de la actividad.'
            else:
                return 'El ganador es: ', winner


        atleta1 = input('Ingrese el nombre del primer atleta: ')
        atleta2 = input('Ingrese el nombre del segundo atleta: ')
        atleta3 = input('Ingrese el nombre del tercero atleta: ')
        tiempo1 = int(input('Ingrese el tiempo que tardó el primer atleta (en segundos): '))
        tiempo2 = int(input('Ingrese el tiempo que tardó el segundo atleta (en segundos): '))
        tiempo3 = int(input('Ingrese el tiempo que tardó el tercer atleta (en segundos): '))
        
        print(ganador(atleta1, atleta2, atleta3, tiempo1, tiempo2, tiempo3))

    elif opcion == 2:
        def cadena(palabras):
            contador = 0
            contador_espacios = 0
            for pal in palabras:
                if pal == 'p' or pal == 'P':
                    contador += 1
                elif pal == 'j' or pal == 'J':
                    contador += 1
                elif pal == ' ':
                    contador_espacios += 1
                    

            total = len(palabras) - contador_espacios
            porcentaje = round(((contador * 100) / total), 2)
            return 'La cantidad de "P" y de "J", es de ', contador, f'y el porcentaje de esas letras en su cadena es de {porcentaje}% '


        palabra = input('Ingrese una cadena: ')

        print(cadena(palabra))


else:
    print('Fin del programa.')










