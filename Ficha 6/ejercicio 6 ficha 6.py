#     • 6. Números pares e impares
# Se pide desarrollar un programa que permita leer una serie de números.
# La finalización de carga de datos se presenta cuando el usuario ingrese un número negativo.
#
# Los requerimientos funcionales del programa son:
# a) La sumatoria de solo los números que estén comprendidos entre 50 y 100.
# b) Cantidad de valores pares ingresados.
# c) Cantidad de valores impares ingresados.
# d) Informar si en la carga de números se ingreso al menos un número 0.
# e) Informar si la serie contiene solo números pares e impares alternados

print('-'* 40)
print('Programa de datos: ')
print()

num_par = 0
num_impar = 0
sumatoria = 0
alternados = True
num_0 = False
anterior = -1
n = int(input('Ingrese un número (con un número negativo corta el programa): '))

while n >= 0:
    if 50 < n < 100:
        sumatoria += n
    paridad = n % 2
    if paridad == 0:
        num_par += 1
    else:
        num_impar += 1
    if n == 0:
        num_0 = True


    if anterior == paridad:
        alternados = False

    anterior = paridad
    n = int(input('Ingrese un número (con un número negativo corta el programa):'))

print('-'* 40)
print('RESULTADOS')
print('-'* 40)

print('La cantidad de números pares es : ', num_par)
print('La cantidad de números impares es : ', num_impar)
if num_0 == True:
    print('Al menos hay un cero')
else:
    print('No se encontró ningún 0')

print('La sumatoria de los número es: ', sumatoria)
if alternados == True:
    print('Los número SI fueron alternados par-impar')
else:
    print('Los números NO fueron alternados ')
