#3. Importe como cadena
# Desarrollar un programa que cargue por teclado un importe (cantidad de dinero) expresado como número en coma flotante y
# muestre un mensaje con esa cantidad pero en dos formatos: en uno debe aparecer precedida por el signo '$'
# y en el otro debe aparecer precedida por la palabra "pesos".

# Dates:
num = float(input('Ingrese el importe: '))
print('$' + (str(num)) )
print( str(num), 'pesos')


