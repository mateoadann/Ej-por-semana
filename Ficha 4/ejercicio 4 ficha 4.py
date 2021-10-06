#4. Temperatura diaria
#Se solicita realizar un programa que permita ingresar tres temperaturas
# correspondientes a diferentes momentos de un día y determinar:
#Cual es el promedio de las temperaturas.
#Si existe alguna temperatura que sea mayor al promedio.

temp_1 = float(input('Ingrese la temperatura durante la mañana: '))
temp_2 = float(input('Ingrese la temperatura durante la tarde: '))
temp_3 = float(input('Ingrese la temperatura durante la noche: '))

promedio = round(((temp_1 + temp_2 + temp_3) / 3), 2)

if temp_1 > promedio:
    print('La temperatura de la mañana fue las mas alta.')
    print('El promedio de la temperatura durante el día fue de: °' + str(promedio))
elif temp_2 > promedio:
    print('La temperatura de la tarde fue la mas alta.')
    print('El promedio de la temperatura durante el día fue de: °' + str(promedio))
elif temp_3 > promedio:
    print('La temperatura de la noche fue la mas alta.')
    print('El promedio de la temperatura durante el día fue de: °' + str(promedio))
else:
    print('El promedio de la temperatura durante el día fue de:', promedio)

print()
print('Fin del programa')
