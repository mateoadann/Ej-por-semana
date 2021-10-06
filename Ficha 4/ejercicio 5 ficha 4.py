import random
#5. Tarjeta de Bingo
# Realizar un programa que genere 15 números aleatorios enteros en el rango del 1 al 100,
# que representaria la tarjeta de bingo de una persona.
# Una vez generados los números aleatorios solicitar al usuario que ingrese 3 numeros enteros y a partir de allí
# mostrar los siguientes mensajes:
# Si el usuario no marcó ninguno de los números indicarlo diciendo "El jugador tiene mala suerte, no marcó ninguna casilla"
# Caso contrario mostrar "El jugador marcó algún numero de la tarjeta".

numeros = random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),\
          random.randint(1,100), random.randint(1,100),random.randint(1,100),random.randint(1,100),\
          random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),\
          random.randint(1,100),random.randint(1,100),random.randint(1,100)


num_1 = int(input('Ingrese un número: '))
num_2 = int(input('Ingrese otro número: '))
num_3 = int(input('Ingrese un último número: '))

if num_1 in numeros or num_2 in numeros or num_3 in numeros:
    print('Acertó al menos un número...')
else:
    print('NO acertó en ningún número...')