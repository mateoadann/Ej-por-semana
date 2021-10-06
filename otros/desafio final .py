
import random
print()
print("-"*50)
print("          ### LANZAMIENTO DE DADOS ###")
print("-"*50)
print()
print()
j1 = input("[] Nombre de jugador 1:")
print()
j2 = input("[] Nombre de jugador 2:")
print("-"*50)
print()
print("[] Empieza", j1)
print()
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)
print()
print("() Dado 1 de", j1, ":", d1)
print("() Dado 2 de", j1, ":", d2)
print("() Dado 3 de", j1, ":", d3)
print()
total1 = 0
if d1 == d2 == d3:
    print("\n[] 3 dados iguales, suma 6 puntos")
    print()
    total1 += 6
elif d1 == d2 and d3 != d2:
    print("# Se tira de nuevo el dado N°3")
    d3 = random.randint(1, 6)
    print()
    print("# Valor del dado 3:", d3)
    print()
    if d3 == d2:
        print("\n[] 3 dados iguales, suma 6 puntos")
        total1 += 6
    else:
        print("[] Dados de distinto valor, no suma puntos")
        total1 += 0

elif d1 == d3 and d2 != d1:
    print("# Se tira de nuevo el dado N°2")
    print()
    d2 = random.randint(1, 6)
    print("# Valor del dado 2:", d2)
    if d2 == d1:
        print("\n[] 3 dados iguales, suma 6 puntos")
        total1 += 6
    else:
        print("[] Dados de distinto valor, no suma puntos")
        total1 += 0

elif d2 == d3 and d1 != d3:
    print("# Se tira de nuevo el dado N°1")
    print()
    d1 = random.randint(1, 6)
    print("# Valor del dado 1:", d1)
    print()
    if d1 == d3:
        print("\n[] 3 dados iguales, suma 6 puntos")
        total1 += 6
    else:
        print("[] Dados de distinto valor, no suma puntos")
        total1 += 0
elif d1 != d2 != d3:
    print("[] Dados de distinto valor, no suma puntos")
    total1 += 0
print("-"*50)
print()
print("[] Ahora tira", j2)
print()
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)
print("() Dado 1 de", j2, ":", d1)
print("() Dado 2 de", j2, ":", d2)
print("() Dado 3 de", j2, ":", d3)
print()
total2 = 0


if d1 == d2 == d3:
    print("\n[] 3 dados iguales, suma 6 puntos")
    total2 += 6
elif d1 == d2 and d3 != d2:
    print("# Se tira de nuevo el dado N°3")
    d3 = random.randint(1, 6)
    print()
    print("# Valor del dado 3:", d3)
    print()
    if d3 == d2:
        print("\n[] 3 dados iguales, suma 6 puntos")
        total2 += 6
    else:
        print("[] Dados de distinto valor, no suma puntos")
        total2 += 0

elif d1 == d3 and d2 != d1:
    print("# Se tira de nuevo el dado N°2")
    print()
    d2 = random.randint(1, 6)
    print("# Valor del dado 2:", d2)
    print()
    if d2 == d1:
        print("\n[] 3 dados iguales, suma 6 puntos")
        total2 += 6
    else:
        print("[] Dados de distinto valor, no suma puntos")
        total2 += 0

elif d2 == d3 and d1 != d3:
    print("# Se tira de nuevo el dado N°1")
    print()
    d1 = random.randint(1, 6)
    print("# Valor del dado 1:", d1)
    print()
    if d1 == d3:
        print("\n[] 3 dados iguales, suma 6 puntos")
        total2 += 6
    else:
        print("[] Dados de distinto valor, no suma puntos")
        total2 += 0
elif d1 != d2 != d3:
    print("[] Dados de distinto valor, no suma puntos")
    total2 += 0

print()
print("-"*50)
print("() Total de puntos de", j1, ":", total1)
print("() Total de puntos de", j2, ":", total2)
print("-"*50)

print()
print("             ###### RONDA 2 ######")
print()
print("-"*50)
print("          ### EMPIEZA", j1, "###")
print("-"*50)
print()
paridad = int(input('[] Ingrese 1 para apostar a una suma impar o ingrese 2 para apostar por una suma par: '))
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)
print()
print("[] Dado 1 de", j1, ":", d1)
print("[] Dado 2 de", j1, ":", d2)
print("[] Dado 3 de", j1, ":", d3)
suma = d1 + d2 + d3

mayor = (max(d1, d2, d3))
menor = (min(d1, d2, d3))
print()
print('[] La suma de los dados dio: ', suma)
print()
print("-"*50)
print()
if paridad == 1 and suma % 2 != 0:
    print('[] Apostó al impar y la suma de sus dado dio impar por lo tanto ganó la apuesta ')
    print()
    print("[] Se suma el mayor dado")
    total1 += mayor
elif paridad == 1 and suma % 2 == 0:
    print('[] Apostó al impar pero la suma de los dados dio par por lo tanto perdió la apuesta')
    print()
    print("[] Se resta el menor dado")
    total1 -= menor
elif paridad == 2 and suma % 2 == 0:
    print('[] Apostó al par y la suma de sus dados dio par por lo tanto gano la apuesta')
    print()
    print("[] Se suma el mayor dado")
    total1 += mayor
elif paridad == 2 and suma % 2 != 0:
    print('[] Apostó al par pero la suma de los dados dio impar por lo tanto perdio la apuesta')
    print()
    print("[] Se resta el menor dado")
    total1 -= menor

print()

print("El total de",j1,"es de:",total1)
# resultado = total * 2

if paridad == 2 and d1 % 2 == 0 and d2 % 2 == 0 and d3 % 2 == 0:
    total1 = total1 * 2
    print()
    print("[] Como todos los dados son de la paridad elegida, su puntaje se duplica")
    print('[] El resultado final es: ', total1)
elif paridad == 1 and d1 % 2 != 0 and d2 % 2 != 0 and d3 % 2 != 0:
    total1 = total1 * 2
    print()
    print("[] Como todos los dados son de la paridad elegida, su puntaje se duplica")
    print('[] El resultado final es: ', total1)

print()

# jugador2

print("-"*50)
print("          ### AHORA TIRA", j2, "###")
print("-"*50)
print()
paridad = int(input('[] Ingrese 1 para apostar a una suma impar o ingrese 2 para apostar por una suma par: '))
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)
print()
print("[] Dado 1 de", j2, ":", d1)
print("[] Dado 2 de", j2, ":", d2)
print("[] Dado 3 de", j2, ":", d3)
suma = d1 + d2 + d3

mayor = (max(d1, d2, d3))
menor = (min(d1, d2, d3))
print()
print('[] La suma de los dados dio: ', suma)
print()
print("-"*50)
if paridad == 1 and suma % 2 != 0:
    print('[] Apostó al impar y la suma de sus dado dio impar por lo tanto ganó la apuesta ')
    print()
    print("[] Se suma el mayor dado")
    total2 += mayor
elif paridad == 1 and suma % 2 == 0:
    print('[] Apostó al impar pero la suma de los dados dio par por lo tanto perdió la apuesta')
    print()
    print("[] Se resta el menor dado")
    total2 -= menor
elif paridad == 2 and suma % 2 == 0:
    print('[] Apostó al par y la suma de sus dados dio par por lo tanto gano la apuesta')
    print()
    print("[] Se suma el mayor dado")
    total2 += mayor
elif paridad == 2 and suma % 2 != 0:
    print('[] Apostó al par pero la suma de los dados dio impar por lo tanto perdio la apuesta')
    print()
    print("[] Se resta el menor dado")
    total2 -= menor

print()

print("El total de",j2,"es de:",total2)

if paridad == 2 and d1 % 2 == 0 and d2 % 2 == 0 and d3 % 2 == 0:
    total2 = total2 * 2
    print()
    print("[] Como todos los dados son de la paridad elegida, su puntaje se duplica")
    print('[] El resultado final es: ', total2)
elif paridad == 1 and d1 % 2 != 0 and d2 % 2 != 0 and d3 % 2 != 0:
    total2 = total2 * 2
    print()
    print("[] Como todos los dados son de la paridad elegida, su puntaje se duplica")
    print('[] El resultado final es: ', total2)

print()
print("-"*50)
print("            ### RESULTADOS ###")
print("-"*50)
print()
print("[] El total de", j1, "es: ", total1)
print()
print("[] El total de", j2, "es: ", total2)
print()
print("-"*50)
if total1 > total2:
    print("    \t¡¡El ganador es", j1, "!!")
elif total2 > total1:
    print("    \t¡¡El ganador es", j2, "!!")
else:
    print("    \t¡¡Ambos jugadores empataron!!")

print("-"*50)
