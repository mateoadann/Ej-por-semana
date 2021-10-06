# 13. Cálculo de Precios con Descuento
# Una empresa nos solicitó un programa que nos permita calcular los precios de los productos que vende al público
# Para ello, nuestro programa debe pedir el precio unitario, la cantidad que se vendió y si se pagó en efectivo o no.
# En base a esto determinar
# El Precio final sin descuentos del articulo (precio unitario por cantidad)
# Calcular un descuento si el usuario pago en efectivo y la cantidad vendida es superior a 10 unidades del 15%
# caso contrario solo aplicar un 5% de descuento

precioU = float(input('Ingrese el valor del valor por pasaje: '))
cantPasaje = int(input('Ingrese la cantidad de pasajes vendidos: '))
pagoEfectivo = True

precioFinal = precioU * cantPasaje

if cantPasaje > 10:
    pagoEfectivo = True
    descuento_1 = round(((precioFinal * 15) / 100), 2)
    print('El precio total de los pasajes con un %15 de descuento es de $', (precioFinal - descuento_1))
elif cantPasaje <= 10:
    pagoEfectivo = False
    descuento_2 = round(((precioFinal * 5) / 100), 2)
    print('El precio final de los pasajes con un %5 de descuento es de $', (precioFinal-descuento_2))
else:
    print('No se se agrega ningún descuento.')
