# Dates
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
dominio = input(' Ingrese su dominio: ')
# Process
if nombre[0] == apellido[0]:
    email = nombre + '.' + apellido
else:
    email = nombre[0] + '.' + apellido

email = email + '@' + dominio
# Resultados
print('La dirección de correo es: ', email)
