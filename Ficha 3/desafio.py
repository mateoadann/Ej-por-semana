import random
print()
j1 = input("Nombre de jugador 1:")
print()
j2 = input("Nombre de jugador 2:")
print()
print("Empieza", j1)
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)
print("Dado 1 de", j1, ":", d1)
print("Dado 2 de", j1, ":", d2)
print("Dado 3 de", j1, ":", d3)
print()
total1 = 0
if d1 == d2 == d3:
    total1 += 6
elif d1 == d2 and d3 != d2:
    print("Se tira de nuevo el dado N°3")
    d3 = random.randint(1, 6)
    print()
    print("Valor del dado 3:", d3)
    if d3 == d2:
        total1 += 6
    else:
        total1 += 0

elif d1 == d3 and d2 != d1:
    print("Se tira de nuevo el dado N°2")
    print()
    d2 = random.randint(1, 6)
    print("Valor del dado 2:", d2)
    if d2 == d1:
        total1 += 6
    else:
        total1 += 0

elif d2 == d3 and d1 != d3:
    print("Se tira de nuevo el dado N°1")
    print()
    d1 = random.randint(1, 6)
    print("Valor del dado 1:", d1)
    if d1 == d3:
        total1 += 6
    else:
        total1 += 0
elif d1 != d2 != d3:
    total1 += 0

print()
print("Ahora tira", j2)
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)
print("Dado 1 de", j2, ":", d1)
print("Dado 2 de", j2, ":", d2)
print("Dado 3 de", j2, ":", d3)
print()
total2 = 0


if d1 == d2 == d3:
    total2 += 6
elif d1 == d2 and d3 != d2:
    print("Se tira de nuevo el dado N°3")
    d3 = random.randint(1, 6)
    print()
    print("Valor del dado 3:", d3)
    if d3 == d2:
        total2 += 6
    else:
        total2 += 0

elif d1 == d3 and d2 != d1:
    print("Se tira de nuevo el dado N°2")
    print()
    d2 = random.randint(1, 6)
    print("Valor del dado 2:", d2)
    if d2 == d1:
        total2 += 6
    else:
        total2 += 0

elif d2 == d3 and d1 != d3:
    print("Se tira de nuevo el dado N°1")
    print()
    d1 = random.randint(1, 6)
    print("Valor del dado 1:", d1)
    if d1 == d3:
        total2 += 6
    else:
        total2 += 0
elif d1 != d2 != d3:
    total2 += 0
print()
print("total de punto", j1, ":", total1)
print("Total de puntos", j2, ":", total2)
