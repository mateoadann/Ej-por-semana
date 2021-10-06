# 2. Suma - División - Potencia
# Se necesita desarrollar un programa que permita calcular la suma de tres números.
# Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales),
# en caso contrario elevar el resultado al cubo.

num_1 = float(input('Ingrese el primer número: '))
num_2 = float(input('Ingrese el segundo número: '))
num_3 = float(input('Ingrese el tercer número: '))

suma = num_1 + num_2 + num_3

if suma > 10:
    division = round((suma / 2), 0)
    print('El resultado es:', division)
else:
    elevar = suma ** 3
    print('El resultado es:', elevar)

print('Fin del programa')
