import random
# 12. Cartas de Truco
# Desarrollar un programa que genere al azar tres cartas simulando una mano de truco. A continuación deberá:
# Informar si entre las cartas se encuentra el as de espadas
# Verificar si las tres cartas son del mismo palo. Si es así, mostrar la suma de las dos mayores.
# En caso contrario, informarlo.

palos = 'Espada', 'Basto', 'Oro', 'Copa'
num_1 = random.randint(1, 12)
num_2 = random.randint(1, 12)
num_3 = random.randint(1, 12)

palo_1 = random.choice(palos)
palo_2 = random.choice(palos)
palo_3 = random.choice(palos)

carta_1 = num_1, palo_1
carta_2 = num_2, palo_2
carta_3 = num_3, palo_3

print(carta_1, carta_2, carta_3)

if palo_1 == palo_2 and palo_1 == palo_3 and palo_2 == palo_3:
    print('Las tres cartas son del mismo palo... ')
else:
    print('Las cartas NO son del mismo palo...')

if num_1 == 1 and palo_1 == 'Espada':
    print('La primera carta es el As de espada.')
elif num_2 == 1 and palo_2 == 'Espada':
    print('La segunda carta es el As de espada.')
elif num_3 == 1 and palo_3 == 'Espada':
    print('La tercer carta es el As de espada.')
else:
    print('Ninguna carta es el As de espada.')
