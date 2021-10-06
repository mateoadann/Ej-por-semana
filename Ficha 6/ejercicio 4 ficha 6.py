# 4. Búsqueda de mayor
# Realizar un programa que permita buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000].

import random

mayor = 0
i = 0

while i < 1000:
    n = random.randint(1, 100000)
    if n > mayor:
        mayor = n
    i += 1


print(' El número mayo es: ', mayor)