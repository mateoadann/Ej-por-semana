# 10. Terreno
# Se ingresan las medidas de frente y fondo de un terreno.
# Determinar si es cuadrado o rectangular y calcular su superficie.

print('Determinamos si el terreno es cuadrado o rectangulo...')
largo = float(input('Ingrese el largo del terreno: '))
ancho = float(input('Ingrese el ancho del terreno: '))

superficie = (largo * 2) + (ancho * 2)

if largo == ancho:
    print('El terreno es cuadrado.')
    print('La superficie que ocupa es de unos', superficie, 'm2')
else:
    print('El terreno es un rectangulo.')
    print('La superficie que ocupa es de unos', superficie, 'm2')

print('Fin del programa...')
