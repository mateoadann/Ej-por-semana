s = 'hola'
#    0123

print(s)
print('La primera letra es: ', s[0])
print('La segunda letra es: ', s[1])
print('La tercera letra es: ', s[2])
print(' La última letra es: ', s[3])

# Tamaño de la secuencia: Cadena de caracteres.
# len (cadena_caracteres)
# La función len me devuelve la cantidad de caracteres que tiene una cadena de caracteres.
tamaño = len(s)
print('Cantidad total de caracteres', tamaño)
print('El último caracter es: ', s[tamaño -1])

# Operador * (Repetir)
nombre = 'Guido'
replicado = (nombre + ' ') * 4
print(replicado)

# La función "Round" sirve para redondear un número.
notaFinal = 5.73168
print(round(notaFinal))
print(round(notaFinal, 2))
print(round(notaFinal, 3))

#Tupla
t = 14, 35, 65
print(t)
print(t[2])
print(t[1])

mayor = max(5, 7, 23, 6)
print('mayor' , mayor)
