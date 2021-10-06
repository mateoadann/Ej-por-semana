import random
# 7. Tirada de moneda
# Programar una tirada de una moneda (opciones: cara o cruz) aleatoriamente.
# Permitir que un jugador apueste a cara o cruz y luego informar si acertó o no con su apuesta.

apuesta = int(input('APUESTE! 1 para cara, 2 para cruz -> '))
moneda = random.randint(1,2)

if apuesta == 1 and moneda == 1:
    print('Muy bien, apostó por Cara y salió Cara!!')

elif apuesta == 2 and moneda == 2:
        print('Muy bien, apostó por Cruz y salió Cruz!!')

else:
    print('Una lastima no acertó... ')