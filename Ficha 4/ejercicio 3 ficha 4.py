#3. Jornal de un Operario
#Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal de un determinado operario.
#Usted deberá cargar por teclado el código de turno que el operario trabajó ese día
#(1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas.
#La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno.
#Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora.


turno = int(input('Ingrese el turno de trabajo (1 para diurno o 2 para nocturno) : '))
horas = int(input('Ingrese la cantidad de horas trabajadas: '))
diurno = 35.50
nocturno = 40.60

if turno == 1:
    pago = round((horas * diurno), 2)
    print('Ya que usted trabajó', horas, 'hora/s, su suedo será de: $' + str(pago))
elif turno == 2:
    pago = round((horas * nocturno), 2)
    print('Ya que usted trabajó', horas, 'hora/s, su sueldo es de: $'+str(pago))
else:
    print('ERROR')

print()
print('Fin del programa')
