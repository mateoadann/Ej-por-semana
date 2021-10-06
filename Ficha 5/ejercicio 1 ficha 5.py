# 1. Operaciones de orden con 3 nros.
# Realizar un programa que tome tres números, los ordene de mayor a menor,
# y diga si el tercero es el resto de la división de los dos primeros.

num_1 = int(input('Ingrese el primer número: '))
num_2 = int(input('Ingrese el segundo número: '))
num_3 = int(input('Ingrese el tercer número: '))

mayor = max(num_1, num_2, num_3)
menor = min(num_1, num_2, num_3)
print('El número mayor es es', mayor, ' y el número menor es el', menor)

division = num_1 % num_2

if num_3 == division:
    print('El tercer número es el resto de la división entre', num_1, 'y', num_2)
else:
    print('El resto de la división es ', division)
    print('El tercer número NO es el resto de la división.')

print('Fin del programa.')