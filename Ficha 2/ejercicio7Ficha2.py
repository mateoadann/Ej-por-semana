# 7. Votación en el Congreso
# En el Congreso se vota la sanción de una ley muy importante.
# Desarrollar un programa que permita ingresar la cantidad de votos a favor y en contra, e informe el porcentaje obtenido en cada caso.

# Dates
votos_favor = int(input('Ingrese la cantidad de votos a favor: '))
votos_contra = int(input('Ingrese la cantida de votos en contra: '))

#Process
votos_totales = votos_favor + votos_contra
porcentaje_favor = (votos_favor*100) / votos_totales
porcentaje_contra = (votos_contra*100) / votos_totales

# Results
print('El total de votos fue: ', votos_totales)
print('Un ', porcentaje_favor, '%, votó a favor ')
print('Un ', porcentaje_contra, '%, votó en contra ')
