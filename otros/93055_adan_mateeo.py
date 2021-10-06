# MATEO ADAN 93055 1K2
# Turno 02 – Enunciado 03 [T2E3]
#
# Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo cadena de caracteres.
# El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del texto,
# y que cada palabra de ese texto está separada de las demás por un espacio en blanco.
# El programa debe incluir al menos una función simple con parámetros y retorno de resultado,
# debe procesar el texto caracter a caracter (a razón de uno por vuelta de ciclo), y debe hacer lo siguiente sin usar un menú de opciones:
#
# 1: Determinar la cantidad de palabras que tienen dos dígitos seguidos y no tienen "n" (mayúscula o minúscula).
# Por ejemplo, el texto: "El curso 1k06 rinde a la tarde." tiene una sola palabra que cumple la condición ("1k06").
#
# 2: Determinar el porcentaje de palabras (respecto del total de palabras del texto) que comienzan y terminan con vocal.
# Por ejemplo, en el texto: "Una oca es casi igual a un ganso." hay 3 palabras que cumplen la condición: "Una", "oca" y "a".
# Como el texto completo tiene 8 palabras, el porcentaje pedido es 37.5%.
#
# 3: Determinar la cantidad de palabras que comienzan con el primer caracter del texto (en mayúscula o en minúscula).
# Por ejemplo, en el texto: "En Córdoba este verano será eterno."
# Hay tres palabras que cumplen la condición (incluida la primera palabra del texto): "En", "este" y "eterno".
#
# 4: Determinar el promedio de caracteres por palabra de aquellas que tienen la expresión "pe"
# (con cualquiera de sus letras en minúscula o en mayúscula). Por ejemplo, en el texto:
# "Pedro es genial pero no va a venir." hay 2 palabras que cumplen la condición ("Pedro" y "pero").
# Entre la dos suman 9 caracteres y por lo tanto es el promedio pedido es 4.5 letras por palabra.
# Por "caracteres", se entiende "cualquier tipo de símbolo, sea este un dígito, una letra, o cualquier otro que pueda aparecer".


def es_vocal(caracter):
    return caracter in "aeiouáéíóú"


def es_letra(car):
    return car >= 'a' and car <= 'z'


def calcular_porcentaje(cantidad, total):
    porcentaje = 0
    if total > 0:
        porcentaje = cantidad * 100 / total
    return porcentaje


def principal():

    texto = input('Ingrese un texto (finaliza con punto): ')
    texto = texto.lower()

    cont_letras = cont_palabras = letras_totales = 0
    anterior = ''
    pal_termina_vocal = cant_vocales = cant_cons_totales = 0
    cant_cons_palabra = pal_mayor_cant_cons = posicion_pal_may_cons = 0
    primer_letra = primer_letra_palabra = ''
    es_primer_letra = True
    pal_primer_letra_con_st = 0
    tiene_st = tiene_s = False

    for car in texto:
        # Dentro de la palabra
        if car != ' ' and car != '.':
            cont_letras += 1

            if es_letra(car):
                letras_totales += 1
                if es_vocal(car):
                    cant_vocales += 1
                else:
                    cant_cons_totales += 1
                    cant_cons_palabra += 1
            elif car == 'ñ':
                letras_totales += 1
                cant_cons_totales += 1

            if es_primer_letra:
                primer_letra = car
                es_primer_letra = False

            if cont_letras == 1:
                primer_letra_palabra = car

            if car == 's':
                tiene_s = True
            else:
                if tiene_s and car == 't':
                    tiene_st = True
                tiene_s = False

        # Fuera de la palabra
        else:
            if cont_letras > 0:
                cont_palabras += 1

            if es_vocal(anterior):
                pal_termina_vocal += 1

            if cont_palabras == 1 or pal_mayor_cant_cons < cant_cons_palabra:
                pal_mayor_cant_cons = cant_cons_palabra
                posicion_pal_may_cons = cont_palabras

            if primer_letra == primer_letra_palabra and tiene_st:
                pal_primer_letra_con_st += 1

            # Reinicio de contadores
            cont_letras = 0
            cant_cons_palabra = 0
            tiene_st = False

        anterior = car

    print('Estadisticas del texto: ')
    print('Cantidad de palabras que terminaron en vocal:', pal_termina_vocal)
    porc_vocales = calcular_porcentaje(cant_vocales, letras_totales)
    porc_consonantes = calcular_porcentaje(cant_cons_totales, letras_totales)
    print('Porcentaje de consonantes en todo el texto', porc_consonantes.__round__(2), '%')
    print('Porcentaje de vocales en todo el texto ', porc_vocales.__round__(2), '%')
    print('La palabra ubicada en la posicion', posicion_pal_may_cons,
          'fue la que tuvo la mayor cantidad de consonantes del texto, con un total de', pal_mayor_cant_cons)
    print('Cantidad de palabras que comenzaron con primera letra de todo el texto y además incluyeron “st”:', pal_primer_letra_con_st)


if __name__ == '__main__':
    principal()
