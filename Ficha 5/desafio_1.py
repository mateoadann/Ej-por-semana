# Datos: Se ingresa un cierta cantidad de segundos.

seg = int(input('Ingrese la cantidad de segundos -> '))
horas = (seg // 3600)
minutos = (seg % 3600) //60
segundos = seg-((horas*3600)+(minutos*60))

print(horas, ':', minutos, ':', segundos,)

horas2 = int(input('Ingrese la cantidad de horas -> '))
minutos2 = int(input('Ingrese la cantidad de minutos -> '))
segundos2 = int(input('Ingrese la cantidad de segundos -> '))

final1 = (horas2*3600)
final2 = (minutos2*60)
final3 = (segundos2*1)
print(final1 + final2 + final3)

#Primera ejecución - Cantidad de segundos a ingresar:  6551
#Segunda ejecución - Cantidad de segundos a ingresar:  21720
#Tercera ejecución - Cantidad de segundos a ingresar:  3123
#Cuarta ejecución - Cantidad de segundos a ingresar: 57862
