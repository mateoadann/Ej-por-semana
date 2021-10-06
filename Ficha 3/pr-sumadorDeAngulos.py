# 7 de abril practico miercoles
# Ej 14 Sumador de angulos.

# Dates
print('Angulo 1')
grados = int(input('Ingrese grados: '))
minutos = int(input('Ingrese minutos: '))
segundos = int(input('Ingrese segundos: '))
angulo1 = grados, minutos, segundos
print('Angulo 2')
grados = int(input('Ingrese grados: '))
minutos = int(input('Ingrese minutos: '))
segundos = int(input('Ingrese segundos: '))
angulo2 = grados, minutos, segundos
print(angulo1, " + ", angulo2)

# Process
# Convertir angulos en segundos
ang1_seg = angulo1[0] * 3600 + angulo1[1] * 60 + angulo1[2]
ang2_seg = angulo2[0] * 3600 + angulo2[1] * 60 + angulo2[2]
suma_segundos = ang1_seg + ang2_seg
print(ang1_seg, "+", ang2_seg, " = ", suma_segundos)

# Convertir la suma a grados, minutos y segundos.
grados = suma_segundos // 3600
resto_seg = suma_segundos % 3600
# segundos a minutos
minutos = resto_seg // 60
segundos = resto_seg % 60
# pasamos el resultado a una tupla
suma = grados, minutos, segundos

# Results
print('La suma en segundos es: ', suma_segundos)
print('La suma en sexageciamal es: ', suma)
