# 9. Edad mínima
# Ingresar por teclado las edades de 3 participantes de un concurso.
# Informar si todos cumplen con la edad mínima establecida para el mismo, también ingresada por teclado.
print()
print('Para poder jugar hay que verficar la edad de los 3 participantes...')
edadMinima = int(input('Ingrese la edad minina para poder jugar: '))
print()
edad_1 = int(input('Ingrese la edad del primer participante: '))
print()
edad_2 = int(input('Ingrese la edad del segundo participante: '))
print()
edad_3 = int(input('Ingrese la edad del tercer participante: '))
print()
if edad_1 >= edadMinima and edad_2 >= edadMinima and edad_3 >= edadMinima:
    print('Todos los participantes pueden jugar... ')
else:
    print('Un participante no cumple con la edad minima para jugar.')

print('Fin del programa...')


