# 6. Precio de venta
# Conociendo el precio de lista de un artículo, determinar:
# Precio de venta al contado (10% de descuento)
# Precio de venta con tarjeta (5% de recargo)

# Dates
precio_lista = float(input(' Ingrese el valor de su producto: '))

# Process
precio_contado = precio_lista - (precio_lista * 0.10)
precio_tarjeta= precio_lista - (precio_lista * 0.05)

# Results
print('Si usted va a pagar de contado, se le aplica un 10% de descuento. El precio final es: ', precio_contado)
print('Si usted va a pagar con tarjeta, se le aplica un 5% de descuento. El precio final es: ', precio_tarjeta)
