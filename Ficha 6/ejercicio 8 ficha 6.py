#     • 8. Mayor número en orden par
# Ingresar de a uno una serie de números.
# Encontrar e imprimir el mayor de todos los números pares cuyo número de orden sea par,
# el proceso terminará cuando el número leído sea igual a cero.

n = int(input('Ingrese un número: (con 0 corta el programa): '))
orden = 1
par_mayor = 0

while n != 0:
    if n % 2 == 0 and orden % 2 == 0 and n > par_mayor:
        par_mayor = n

    orden += 1
    n = int(input('Ingrese un número: (con 0 corta el programa): '))

print('El número par mayor es:', par_mayor)
