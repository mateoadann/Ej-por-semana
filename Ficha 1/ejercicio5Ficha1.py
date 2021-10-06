# Converción de unidades
# Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en:
# Yardas
# Pulgadas
# Centímetros
# Metros
# Sabiendo que: 1 pie = 12 pulgadas, 1 yarda = 3 pies,  1 pulgada = 2.54 centímetros, 1 metro = 100 centímetros.

# Dates
pie = float(input(' Ingrese una medida en pie: '))

# Process
pulgada = pie * 12
yarda = pie / 3
centrimetros = 30.48 * pie
metros = pie / 3.28

# Results
print('Son ', round(pulgada, 2), ' pulgadas')
print('Son ', round(yarda, 2), ' yardas')
print('Son ', round(centrimetros, 2), ' centimetros')
print('Son ', round(metros, 2), ' metros')
print('Fin')
