# Analisis de palabra
# Se pide un programa que le solicite al usuario que ingrese una palabra. Con esa palabra calcular los siguientes puntos:
# Determinar la cantidad de letras que tiene  la palabra.
# Mostrar un mensaje que informe si la palabra termina en vocal.

palabra = input('ingrese una palabra: ')


if palabra[-1] == 'a' or palabra[-1] == 'e' or palabra[-1] == 'i' or palabra[-1] == 'o' or palabra[-1] == 'u':
    print('La palabra que ingresó tiene', len(palabra), 'letras')
    print('La palabra termina con una vocal')
else:
    print('La palabra que ingresó tiene', len(palabra), 'letras')

for caracter in palabra:
    print(caracter)


print('Fin del programa...')

