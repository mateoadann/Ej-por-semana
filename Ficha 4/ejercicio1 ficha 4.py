#Generador de Dirección de Mail
#Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego,
# proponga una dirección de mail para el nombre y apellido ingresado de acuerdo a las siguientes reglas:
#Componer la dirección de correo de la siguiente manera:
#<primera letra del nombre><apellido>@<dominio>
#Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= frc.utn.edu.ar la dirección de mail sería:
#fsteffolani@frc.utn.edu.ar
#Pero si la primera letra del nombre y la primera letra del apellido son la misma entonces utilizar:
#<nombre>.<apellido>@<dominio>
#Por ejemplo para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar la dirección de mail sería:
#soledad.steffolani@colegiorosarito.edu.ar

#DATES:
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
dominio = input('Ingrese un dominio (gmail.com/hotmail.com - sin el @: ')

if nombre[0] != apellido[0]:
    print('Su mail es:', nombre[0] + apellido + '@' + dominio)
elif nombre[0] == apellido[0]:
    print('Su Mail es:', nombre+apellido+'@'+dominio)
else:
    print('ERROR')

print('Fin del programa')