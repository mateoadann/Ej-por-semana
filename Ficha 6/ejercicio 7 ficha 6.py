#     • 7. Censo
# Desarrollar un programa que permita procesar los datos del último censo de una pequeña población.
# Por cada habitante se ingresa:
# sexo (M/F) y edad. La carga de datos finaliza al ingresar cualquier otro valor para sexo.
#
# El programa debe informar:
# a) A qué sexo corresponde la mayor cantidad de habitantes (considerar que puede ser igual)
# b) Cantidad de mujeres en edad escolar (4 a 18 años inclusive)
# c) Si hay algún varón que supere los 80 años de edad.

sexo = input('Indique su sexo:\n(M/F, con cualquier otra letra corta el programa): ')
cant_f = 0
cant_m = 0
escolar = 0
mayores = 0


while sexo == 'M' or sexo == 'F':
    edad = int(input('Ingrese su edad: '))
    if sexo == 'F':
        cant_f += 1
    else:
        cant_m += 1
    if sexo == 'F' and 3 < edad < 19:
        escolar += 1
    if sexo == 'M' and 80 < edad < 100:
        mayores += 1
    sexo = input('Ingrese su sexo:\n(M/F, con cualquier otra letra corta el programa) ')


print()
print('RESULTADOS:')
print()
if cant_m < cant_f:
    print('Hay mas mujeres que hombres...')
elif cant_m == cant_f:
    print('Hay la misma cantidad de hombres que mujeres...')
else:
    print('Hay mas hombres que mujeres...')
if escolar > 0:
    print('Hay ', escolar, 'chicas en edad escolar.')
else:
    print('No hay chicas en edad escolar...')
if mayores > 0:
    print('La cantidad de hombres mayores a 80 años es de: ', mayores)
else:
    print('No hay hombres mayores a 80 años...')

