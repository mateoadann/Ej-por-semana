# • 6. Institución Educativa
# Una institución educativa necesita un programa que facilite la gestión de cupos de los
# cursos de primer grado. Ingresar tres grados. De cada grado se ingresa el código de identificación (Ejemplo 1A, 1B,
# ...) y la cantidad de niños y de niñas y cupo máximo (que es el mismo para los tres cursos). Los requerimientos
# funcionales son:
# a)  Código de identificación del curso que tenga menos alumnos inscriptos.
# b)  Porcentaje de niñas de cada curso.
# c)  Porcentaje de niños de cada curso.
# d)  Promedio general de alumnos.
# e) Si algunos de los tres grados supera el cupo máximo informar
# un mensaje la necesidad de apertura de una nueva división.

cupo_M = int(input('Cual es el cupo máximo de alumnos para los cusos?: '))
codigo_a = input('Ingrese el código del primer curso (2 dígitos. Por ejemplo: 3A): ')
codigo_b = input('Ingrese el código del segundo curso curso (2 dígitos. Por ejemplo: 3A): ')
codigo_c = input('Ingrese el código del tercer curso (2 dígitos. Por ejemplo: 3A): ')

print('Curso A')
nene_a = int(input('Cuantos chicos estan inscriptos en el primer curso?: '))
nena_a = int(input('Cuantas chicas estan inscriptos en el primer curso?: '))
total_a = nene_a + nena_a
porcentaje_nene_a = round(((nene_a * 100) / total_a), 2)
porcentaje_nena_a = round(((nena_a * 100) / total_a), 2)
print()

print('Curso B')
nene_b = int(input('Cuantos chicos estan inscriptos en el segundo curso?: '))
nena_b = int(input('Cuantas chicas estan inscriptos en el segundo curso?: '))
total_b = nene_b + nena_b
porcentaje_nene_b = round(((nene_b * 100) / total_b), 2)
porcentaje_nena_b = round(((nena_b * 100) / total_b),2)
print()

print('Curso C')
nene_c = int(input('Cuantos chicos estan inscriptos en el tercer curso?: '))
nena_c = int(input('Cuantas chicas estan inscriptos en el tercer curso?: '))
total_c = nene_c + nena_c
porcentaje_nene_c = round(((nene_c * 100) / total_c), 2)
porcentaje_nena_c = round(((nena_c * 100) / total_c), 2)


promedio =(total_a + total_b + total_c) // 3
menos = min(total_a, total_b, total_c)

print(' CURSO A ')
print('El total de inscriptos es de', total_a, 'alumnos')
print('El porcentaje de chicos es de', porcentaje_nene_a, '%')
print('El porcentaje de las chicas es de', porcentaje_nena_a, '%')
print()
print( 'CURSO B ')
print('El total de inscriptos es de', total_b, 'alumnos')
print('El porcentaje de chicos es de', porcentaje_nene_b, '%')
print('El porcentaje de las chicas es de', porcentaje_nena_b, '%')
print()
print( 'CURSO C')
print('El total de inscriptos es de', total_c, 'alumnos')
print('El porcentaje de chicos es de', porcentaje_nene_c, '%')
print('El porcentaje de las chicas es de', porcentaje_nena_c, '%')
print()


print('El promedio general es de', promedio, 'alumnos po curso.')

if menos == total_a:
    print('El curso con menos inscriptos es el "A", código:', codigo_a)
elif menos == total_b:
    print('El curso con menos inscriptos es el "B", código:', codigo_b)
elif menos == total_c:
    print('El curso con menos inscriptos es el "C", código:', codigo_c)
else:
    print('Todos tienen la misma cantidad de inscriptos.')

if total_a > cupo_M:
    print('El curso "A" posee mas inscriptos que el cupo máximo, se debe abrir una nueva división.')
elif total_b > cupo_M:
    print('El curso "B" posee mas inscriptos que el cupo máximo, se debe abrir una nueva división.')
elif total_c > cupo_M:
    print('El curso "C" posee mas inscriptos que el cupo máximo, se debe abrir una nueva división.')
