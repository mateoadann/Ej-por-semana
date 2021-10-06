import random
# 7. Juego de Dados: Pares e Impares
# Desarrollar un programa para simular un juego de dados con las siguientes reglas:
# Participan 3 jugadores: el campeón y 2 retadores.
# Antes de comenzar el juego, se debe ingresar el récord del campeón.
# En las dos primeras rondas, compiten sólo los retadores:
# se lanzan 2 dados. Si la suma de ambos es impar, gana el retador 1; si no, gana el retador 2.
# Primera ronda: el ganador obtiene tantos puntos como indica la suma de los dados
# Segunda ronda: a los puntos de la primera ronda, el ganador suma tantos puntos como indique el dado de mayor valor,
# y al perdedor se le restan tantos puntos como indique el dado de menor valor
# Ronda final: se suma a la competencia el campeón actual, que participa con un puntaje equivalente a su récord.
# Se pide:
# Mostrar en cada ronda el valor de los dados y los puntajes de cada retador.
# Si ninguno de los retadores supera al campeón, este mantiene su puesto. En caso contrario,
# el que obtenga mayor puntaje será el ganador.
# Al terminar, informar si alguno de los retadores llegó a tener más puntos que el record.

dado_1 = random.randint(1, 6)
dado_2 = random.randint(1, 6)

#JUGADOR 1
nombre_1 = input('Nombre del jugador N°1: ')
player_1 = [0]
jugador_1 = [nombre_1, player_1]


#JUGADOR 2
nombre_2 = input('Nombre del jugador N°2: ')
player_2 = [0]
jugador_2 = [nombre_2, player_2]

record = int(input('Ingrese el record del campeon: '))
print()
print('Ronda N°1:')
print('El valor del dado uno es:', dado_1)
print('El valor del dado dos es:', dado_2)
campeon = 'Jugador 3'
ganador = [campeon, record]

suma = dado_1 + dado_2

print('La suma de los dados es:', suma)

if suma % 2 == 0:
    player_1[0] = suma
    print(jugador_1)
    print(jugador_2[0], 'no suma puntos')
else:
    player_2[0] = suma
    print(jugador_2)
    print(jugador_1[0], 'no suma puntos')


dado_3 = random.randint(1, 6)
dado_4 = random.randint(1, 6)

print()
print('RONDA N°2: ')
print('El valor del dado 1 es de:', dado_3)
print('El valor del dado 2 es de:', dado_4)


winner = max(dado_3, dado_4)
loser = min(dado_3, dado_4)

if player_1[0] == suma:
    player_1[0] = suma + winner
    print(jugador_1)
elif player_2[0] == suma:
    player_2[0] = suma + winner
    print(jugador_2)

if player_1[0] != suma + winner:
    player_1[0] = -loser
    print(jugador_1)
elif player_2[0] != suma + winner:
    player_2[0] = -loser
    print(jugador_2)

win = max(player_1[0], player_2[0])
loss = min(player_1[0], player_2[0])

if win == player_1[0]:
    finalista = jugador_1
else:
    finalista = jugador_2


if loss == player_1[0]:
    perdedor = jugador_1
else:
    loss = jugador_2

print()
print('RONDA FINAL')
print(ganador, 'vs', finalista)
print()

if win == player_1[0] and win > ganador[1]:
    ganador = jugador_1
    print('El ganador es', ganador)
elif win == ganador[1]:
    print('Hay empate!!')
elif win == player_2[0] and win > ganador[1]:
    ganador = jugador_2
    print('El ganador es', ganador)
else:
    print('El ganador sigue siendo', ganador)

print('Fin del programa')



