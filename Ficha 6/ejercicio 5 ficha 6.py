# 5. Menores y promedio Realizar un programa
# que genere 5000 números
# aleatorios en el rango de [0, 100000] y que permita:
# Determinar el menor de los números generados en forma aleatoria
#Calcular el valor promedio de los números menores a 10.000.

import random

menor = 0
menor_q = 0 
i = 0

while i < 5000:
    n = random.randint(1, 100000)
    if n < 10000:
        menor_q = n
        menor = n

    i += 1
    

print('El número menor es, ', menor)
print('Es menor que 10.000, ', menor_q)
