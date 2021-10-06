# 7. Precio del boleto
# Se desea conocer el precio de un boleto de viaje en ómnibus de media distancia.
# Para el cálculo del mismo se debe considerar el monto base (que se cobra siempre),
# más un valor extra calculado en base a la cantidad de kilómetros a recorrer:
# Por cada kilómetro a recorrer se cobra $0.30 de adicional.

# Dates
precio_base = 100
cant_kilometros = int(input(' Ingrese la cantidad de kilometros que va a recorrer: '))

# Process
precio_adicional = 0.30 * cant_kilometros
precio_boleto = precio_adicional + precio_base

# Results
print(' El valor de su boleto es: ', precio_boleto)

