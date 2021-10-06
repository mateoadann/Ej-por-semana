# 2. Fecha como cadena
# Desarrollar un programa que cargue por teclado una cadena de caracteres que se supone representa
# una fecha en formato 'dd/mm/aaaa', y muestre por separado el día, el mes y el año.
# Ejemplo: si la cadena ingresada es '16/03/2016' el programa debe mostrar: 'Día: 16  -  Mes: 03  -  Año: 2016'.

# Dates:

dia = input('Día: ')
mes = input('Mes: ')
año = input('Año: ')
fecha = dia, mes, año

print(dia +'/' + mes + '/' + año)
print('Día:',fecha[0], '- Mes:', fecha[1], '- Año:', fecha[2])
