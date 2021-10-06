#     • 9. Comisión de Vendedores
# Una empresa debe calcular el total de comisiones que debe abonar por ventas realizadas por sus vendedores,
# para ello le solicita un sistema que le permita calcular dicho montos.
# Se tiene conocimiento que la empresa tiene cuatro categorías de vendedores (1 a 4).
# Usted debe solicitar el ingreso de la categoría del vendedor y el total de la venta
# (el proceso termina cuando se ingrese una categoría igual a cero)
# y acumular las comisiones de las ventas rendidas por los vendedores de diferentes en base a los siguientes cálculos:
# a) Categoría 1: cobra una comisión de 10%
# b) Categoría 2: cobra una comisión de 25%
# c) Categoría 3: cobra una comisión de 30%
# d) Categoría 4: cobra una comisión de 40%
# Una vez procesadas todas las ventas mostrar el total de comisiones a pagar
# por cada categoría de vendedores que tiene la empresa junto con el total general

categoria = int(input('Ingrese su categoría de vendedor (1 a 4, con 0 corta el programa): '))
ventas1 = 0
ventas2 = 0
ventas3 = 0
ventas4 = 0

while categoria != 0:
    ventas = int(input('Ingrese el total de ventas que realizó en este mes\n(son comas ni puntos)'))
    if categoria == 1:
        ventas1 += ventas
        comision1 = round(((10 * ventas1) / 100), 2)
        cate1 = ventas + comision1
    elif categoria == 2:
        ventas2 += ventas
        comision2 = round(((25 * ventas2) / 100), 2)
        cate2 = ventas + comision2
    elif categoria == 3:
        ventas3 += ventas
        comision3 = round(((30 * ventas3) / 100), 2)
        cate3 = ventas + comision3
    elif categoria == 4:
        ventas4 += ventas
        comision4 = round(((40 * ventas4) / 100), 2)
        cate4 = ventas + comision4
    else:
        print('Error, indique una categoría válida')

    categoria = int(input('Ingrese su categoría de vendedor (1 a 4, con 0 corta el programa): '))
print()
print('RESULTADOS:')
print()
if ventas1 > 0:
    print('Categoria 1 deberá pagar una comisión de $', comision1 )
if ventas2 > 0:
    print('Categoria 2 deberá pagar una comisión de $', comision2 )
if ventas3 > 0:
    print('Categoria 3 deberá pagar una comisión de $', comision3)
if ventas4 > 0:
    print('Categoria 4 deberá pagar una comisión de $', comision4 )
