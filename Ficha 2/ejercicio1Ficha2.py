# 1. Cuadrados y cubos
# Leer dos números y calcular: La suma de sus cuadrados. El promedio de sus cubos.

# Dates
a = float(input(' Ingrese el primer número: '))
b = float(input(' Ingrese el segundo número: '))

# Process
cuadradoA = a**2
cuadradoB = b**2
suma_cuadrados = cuadradoA + cuadradoB
cuboA = a**3
cuboB = b**3
prom_cubo = (cuboA + cuboB) / 2

# Results
print('El cuadrado de ', a, ' es ', cuadradoA)
print('El cuadrado de ', b, ' es ', cuadradoB)
print('La suma de los cuadrados de los número es: ', suma_cuadrados)
print('El cubo de ', a, ' es ', cuboA)
print('El cubo de ', b, ' es ', cuboB)
print('El promedio de los cuadrados de los número es: ', prom_cubo)
