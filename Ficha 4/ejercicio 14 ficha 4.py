import random
#     • 14. Tarifas de Peaje
# La empresa de peajes AED Pase-Pase S.R.L, festeja su séptimo aniversario y, por tal motivo,
# el día de hoy ofrece premios a a sus clientes.
# Estos premios se calculan de la siguiente manera:
# 1) Cada vez que pasa un cliente, se sortea un número del 0 al 9.
# Si el número coincide con el último dígito de la patente del vehículo, se le cobra la tarifa promocional de $50,
# si no, se le cobra la tarifa estándar de $90
# 2) Independientemente de la tarifa que deba pagar, si el último dígito de la patente es 7,
# entonces recibe un descuento del 50%, en caso contrario un descuento del 10%.
# Desarrolle un programa en Python que le solicite al usuario los dígitos de su patente (únicamente los dígitos),
# simule su paso por el peaje e indique el monto a abonar.
suerte = random.randint(0, 9)
print(suerte)
patente = input('Ingrese los 3 números de su patente: ')

tarifa = 90

if patente[-1] == suerte:
    tarifa = 50
    print('SUERTE! Accede a la tarifa de $', tarifa)
else:
    print('MALA SUERTE! Accede a la tarifa habitual de $', tarifa)


if patente[-1] == 7:
    tarifa = round(((tarifa * 50) / 100), 2)
    print('MUCHA SUERTE!!!! El valor de su tarifa es de $', tarifa)
else:
    tarifa = (tarifa * 10) / 100
    print('CASI!! El valor de su peaje es de $', tarifa)