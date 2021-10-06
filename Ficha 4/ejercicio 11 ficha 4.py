# 11. Galería de arte
# Una galería de arte desea preparar un catálogo de sus cuadros más famosos.
# Se realiza una prueba con tres cuadros y por cada uno se ingresa el año en que fue creado. El programa deberá:
# Verificar si todos los cuadros son anteriores al siglo XX (El siglo XX es el siglo pasado. Se inició en el año 1901 y terminó en el año 2000).
# Determinar si alguna de las obras fue creada en un año que se ingresa por teclado.
# Informar la diferencia en años entre la obra más nueva y la más antigua.

obra_1 = int(input('Ingrese el año en el que fue creada la primer obra: '))
obra_2 = int(input('Ingrese el año en el que fue creada la segunda obra: '))
obra_3 = int(input('Ingrese el año en el que fue creada la tercer obra: '))

if 2000 >= obra_1 > 1901 and 2000 >= obra_2 > 1901 and 2000 >= obra_3 > 1901:
    print('Todos los cuadros fueron creados en el siglo XX.')
elif obra_1 > 2000 and obra_2 > 2000 and obra_3 > 2000:
    print('Todas las obras fueron creadas en el siglo XI')
else:
    print('Todas la obras no fueron credas en siglo XX')

reciente = min(obra_1, obra_2, obra_3)
antigua = max(obra_1, obra_2, obra_3)
diferencia = antigua - reciente
print('Entre la obra mas antigua y la obra mas nueva hay', diferencia, ' años')
