# 2. Descuento en medicinas
# Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia (cargar por teclado el precio de ese medicamento)
# sabiendo que todos los medicamentos tienen un descuento del 35%.
# Mostrar el precio actual, el monto del descuento y el monto final a pagar

# Dates
medicamento = float(input('¿Cual es el precio de su medicamento? '))

# Process
descuento = medicamento - (medicamento * 0.65)
precio_final = medicamento - descuento

# Results
print('Se le aplicará un descuento del 35%, que son ',descuento)
print('El precio final del producto con el descuento es de ', precio_final)
