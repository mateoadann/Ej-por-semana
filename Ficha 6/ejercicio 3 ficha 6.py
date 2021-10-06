# 3. Promedio de números aleatorios
# Realice un programa que permita calcular el promedio de 1000 números aleatorios generados en el rango de [0, 100000]
import random

acumulador = 0
i = 0
while i < 1000:
    n = random.randint(0, 10000)
    acumulador = n
    i += 1
    print(acumulador)

promedio = acumulador / i
print('El promedio es, ', promedio)





