#     • 3. Mantenimiento Informático
# El Área de Mantenimiento de un laboratorio informático nos ha solicitado el desarrollo de un programa
# que facilite la gestión de las tareas realizadas en el día.
# El usuario debe ingresar de tres equipos informáticos (PC) los siguientes datos:
# número de identificación de la PC, tiempo de reparación (expresado en minutos) y la causa de mantenimiento
# (1- Problema de Hardware 2-Problema de Software)
# Los requerimientos funcionales son:
# a)  ¿Cuál es el tiempo total de las tareas de mantenimiento?
# b)  ¿Cuál es la PC (Número de identificación) que tuvo mayor tiempo en tareas de mantenimiento?
# c)  Tiempo promedio de tareas de mantenimiento.
# d)  Informar con un mensaje si todas las PC (Número de identificación)
# que se les ha realizado mantenimiento tuvieron problemas de Hardware.

print('PC N°1:')
numid_1 = int(input('Ingrese los tres dígitos de identificación de la PC: '))
tiempoR_1 = int(input('Ingrese el tiempo de reparación (expresados en minutos): '))
causaM_1 = input('Ingrese la causa del mantenimiento (1 pada hardware - 2 para software): ')
print()

print('PC N°2: ')
numid_2 = int(input('Ingrese los tres dígitos de identificación de la PC: '))
tiempoR_2 = int(input('Ingrese el tiempo de reparación (expresados en minutos): '))
causaM_2 = input('Ingrese la causa del mantenimiento (1 pada hardware - 2 para software): ')
print()

print('PC N°3: ')
numid_3 = int(input('Ingrese los tres dígitos de identificación de la PC: '))
tiempoR_3 = int(input('Ingrese el tiempo de reparación (expresados en minutos): '))
causaM_3 = input('Ingrese la causa del mantenimiento (1 pada hardware - 2 para software): ')
print()

tiempoTotal = tiempoR_1 + tiempoR_2 + tiempoR_3
print('El tiempo total para realizar el mantenimiento de todas las computadoras es de', tiempoTotal, 'minutos.')
print()

mayorTiempo = max(tiempoR_1, tiempoR_2, tiempoR_3)
if mayorTiempo == tiempoR_1:
    print('La computadora que mas tiempo requiere es la computadora es la primera computadora ID:', numid_1)
elif mayorTiempo == tiempoR_2:
    print('La computadora que mas tiempo requiere es la computadora es la segunda computadora ID:', numid_2)
elif mayorTiempo == tiempoR_3:
    print('La computadora que mas tiempo requiere es la computadora es la tercer computadora ID:', numid_3)
else:
    print('Todas requieren del mismo tiempo para ser raparadas.')

print()
promedio = (tiempoR_1 + tiempoR_2 + tiempoR_3) // 3
print('El tiempo promedio para arregalar cada computadora es de', promedio, 'minutos.')

if causaM_1 == '1' and causaM_2 == '1' and causaM_3 == '1':
    print('Las tres computadoras requieren de un mantenimiento de hardware.')
elif causaM_1 == '1' or causaM_2 == '1' or causaM_3 == '1':
    print('Al menos una de las compurtadoras requieren un mantemiento de hardware.')
else:
    print('Ninguna requiere un mantenimiento de hardware.')

