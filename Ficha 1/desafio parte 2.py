import random
print('-'*40)
j1 = input('Ingrese su nombre:')
print('-'*40)
paridad = int(input('Ingrese 1 para impar o 2 para par: '))
print('-'*40)
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)
print('-'*40)
print("Dado 1 de", j1, ":", d1)
print("Dado 2 de", j1, ":", d2)
print("Dado 3 de", j1, ":", d3)
suma = d1 + d2 + d3
total = 0
mayor = (max(d1, d2, d3))
menor = (min(d1, d2, d3))

if paridad == 1 and suma % 2 != 0:
    print('-'*40)
    print('apostó al impar y la suma de sus dado dio impar, GANO ')
    total += mayor
elif paridad == 1 and suma % 2 == 0:
    print('-'*40)
    print('Apostó al impar pero la suma de los dados dio par, PERDIO')
    total -= menor
elif paridad == 2 and suma % 2 == 0:
    print('-'*40)
    print('Apostó al par y la suma de sus dados dio par, GANO')
    total += mayor
elif paridad == 2 and suma % 2 != 0:
    print('-'*40)
    print('Apostó al par pero la suma de los dados dio impar, PERDIO')
    total -= menor

print('-'*40)
print('La suma de los dados dio: ', suma)
print('-'*40)
print('El resto de la suma dio: ', suma % 2)
print('-'*40)
print('EL número mayor es:', mayor)
print('-'*40)
print('El número menor es:', menor)

if paridad == 2 and d1 % 2 == 0 and d2 % 2 == 0 and d3 % 2 == 0:
    total = total * 2
    print('El resultado final es: ', total)
elif paridad == 1 and d1 % 2 != 0 and d2 % 2 != 0 and d3 % 2 != 0:
    total = total * 2
    print('El resultado final es: ', total)

print('-'*40)
print('El total es: ', total)
print('FINAL DEL JUEGO.....')
