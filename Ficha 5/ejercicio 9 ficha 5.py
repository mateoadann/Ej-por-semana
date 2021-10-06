import random
# 9. ¿Piedra, Papel o Tijera?
# Desarrollar un programa que permita al usuario jugar contra la computadora el clásico “Piedra, Papel o Tijera”
# y determine cuál de ellos es el ganador.
# Las reglas son:
# La piedra aplasta (o rompe) la tijera. (Gana la piedra).
# La tijera corta el papel. (Gana la tijera).
# El papel envuelve la piedra. (Gana el papel)
# Si los dos jugadores eligen el mismo elemento, empatan.

lista = ['Piedra', 'Papel', 'Tijera']

jug_1 = random.choice(lista)
print('Jugador 1',jug_1)
jug_2 = random.choice(lista)
print('Jugador 2', jug_2)
print()
if jug_1 == 'Piedra' and jug_2 == 'Tijera':
    print('El ganador es el Jugador 1.')
elif jug_1 == 'Piedra' and jug_2 == 'Papel':
    print('El ganador es el Jugador 2.')
elif jug_1 == 'Tijera' and jug_2 == 'Piedra':
    print('El ganador es el jugador 2.')
elif jug_1 == 'Tijera' and jug_2 == 'Papel':
    print('El ganador es el jugador 1')
elif jug_1 == 'Papel' and jug_2 == 'Tijera':
    print('El ganador es el jugador 2')
elif jug_1 == 'Papel' and jug_2 == 'Piedra':
    print('El ganador es el jugador 1')
elif jug_2 == 'Tijera' and jug_1 == 'Tijera':
    print('Hay empate.')
elif jug_1 == 'Piedra' and jug_2 == 'Piedra':
    print('Hay empate.')
elif jug_2 == 'Papel' and jug_1 == 'Papel':
    print('Hay empate.')
else:
    print('nose que pasó je')