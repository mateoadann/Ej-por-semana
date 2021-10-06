import random
# 8. Lanzamiento de dados
# Simular un juego en el que se lanzan dos dados.
#  Si ambos dados son iguales o la suma entre ellos es impar, gana el usuario. En caso contrario, gana la máquina

print('Usuario VS Máquina...')
print('Si la suma de los dos dados sale impar gana el usuario de lo contratrio la máquina gana.')

dado_1 = random.randint(1,15)
dado_2 = random.randint(1,15)

suma = dado_1 + dado_2

if (suma % 2) == 0 :
    print('Ganadora la Máquina...')
else:
    print('Usuario Ganador...')

print('Dado 1:',dado_1)
print('Dado 2:',dado_2)
print('La suma es:', suma)