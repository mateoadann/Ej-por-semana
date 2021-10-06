print('Hola! Vamos a crear un usario... ')
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = int(input('Cuantos años tiene? '))
numero = int(input('Ingrese un número que le guste... '))

if nombre[0] == apellido[0]:
    usuario = nombre + '.' + apellido + str(numero)
else:
    usuario = nombre[0]+ '.' + apellido + str(numero)
print('Su usuario será: ', usuario)

if edad >= 18:
    print('Por ser mayor de edad, tendrá todo el contenido disponible...')
elif edad == 0:
    print('Usted no puede tener 0 años...')
    edad = int(input('Ingrese nuevamente su edad: '))
    if edad >= 18 or edad < 99:
        print('Por ser mayor de edad, tendrá todo el contenido disponible...')
    elif edad < 18:
        print('Tendrá contenido bloqueado por de menor de edad... ')
    elif edad >= 99:
        print('Lo siento no puede tener mas de 99 años ')
    else:
        print('Error')
elif edad < 18:
    print('Tendrá contenido bloqueado por ser menor de edad... ')
else:
    print('Error')
