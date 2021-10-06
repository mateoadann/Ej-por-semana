# Dates
edad1 = int(input('Edad participante 1: '))
edad2 = int(input('Edad participante 2: '))
edad3 = int(input('Edad participante 3: '))
minima = int(input(' Ingrese la edad mínima: '))

# Process
if edad1 >= minima and edad2 >= minima and edad3 >= minima:
    mensaje = ' Todos '
else:
    mensaje = 'No todos '

mensaje = mensaje + ' complen con la edad minima'

# Results
print(mensaje)
