# Dates
precio_lista = float(input('Ingrese el precio de lista: '))

# Process
descuento = float(precio_lista * 10 / 100)
precio_contado = float(precio_lista - descuento)
recargo = float(precio_lista * 5 / 100)
precio_tarjeta = float(precio_lista + recargo)

# Results
print('El precio contado es $ ', precio_contado)
print('El precio con tarjeta es $ ', precio_tarjeta)
print('FIN')
