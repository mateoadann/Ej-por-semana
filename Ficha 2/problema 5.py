# 29 de Marzo. Lunes
# G es una Constante
# Función ptencia pow(base, exponente)
# Operador ** 10 ** -8

G = 6.673 * pow(10, -8)
m1 = float(input(' Ingrese la masa del cuerpo 1: '))
m2 = float(input(' Ingrese la masa del cuerpo 2: '))
# Distancia entre los cuerpos.
d = float(input('Ingrese la distancia '))

# Process
# Usando función pow: f = (G*m1*m2) / pow(d, 2)
f = (G*m1*m2) / d**2
print(f)
