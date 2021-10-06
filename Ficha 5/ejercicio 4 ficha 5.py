# 4. Observatorio meteorológico
# Un observatorio meteorológico ha tomado el registro de temperaturas en distintos momentos del día.
# Se solicita el desarrollo de un programa que facilite información estadísticas de ellas.
# El usuario debe ingresar cuatro valores de temperatura (considerar que son valores enteros).
# Los requerimientos funcionales son
# a) Promedio de temperatura diaria.
# b) Temperatura máxima.
# c) Temperatura mínima.
# d) Informar con un mensaje si algunas de las temperaturas supera a la temperatura promedio

temp_1 = int(input('Ingrese la primera temperatura obtenida: '))
temp_2 = int(input('Ingrese la segunda temperatura obtenida: '))
temp_3 = int(input('Ingrese la tercer temperatura obtenida: '))
temp_4 = int(input('Ingrese la cuarta temperatura obtenida: '))

promedio = (temp_1 + temp_2 + temp_3 + temp_4) // 4
maxima = max(temp_1, temp_2, temp_3, temp_4)
minima = min(temp_1, temp_2, temp_3, temp_4)

print('La temperatura promedio es de °' + str(promedio))
print()
print('La temperatura máxima es de °' + str(maxima))
print()
print('La temperaura minima es de °' + str(minima))

if temp_1 > promedio:
    print('La primer temperatura es aun mayor que el promedio de las cuatro. ')
elif temp_2 > promedio:
    print('La segunda temperatura es aun mayor que el promedio de las cuatro. ')
elif temp_3 > promedio:
    print('La tercer temperatura es aun mayor que el promedio de las cuatro. ')
elif temp_4 > promedio:
    print('La cuarta temperatura es aun mayor que el promedio de las cuatro. ')
else:
    print('Ninguna temperatura es mayor al promedio.')
