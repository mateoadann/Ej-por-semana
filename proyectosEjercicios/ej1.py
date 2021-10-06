#Imprimir por pantalla la tabla de cualquier número

#tabla = int(input('Ingrese el número para ver su tabla: '))

#for mul in range(1,11):
    #print(tabla,'x',mul,'=',tabla * mul)
#else:
    #print('Listo')


#HACE UN TRIAGULO CON ASTERISCOS:
#def imprimir(num):
 #   for x in range(1, (num + 1)):
  #      print('*' * x)

#imprimir(int(input('ingrese un número: ')))

# PROGRAMA ECO:
#def eco(word):
   # print('ECO -> ', word)
   # while word != 'exit':
   #     word = input('Ingrese una palabra: ')
    #    print('ECO -> ', word)
   # else:
    #    print('Fin del programa...')

#eco(input('Ingrese una palabra: '))

#LISTAS, FUNCIONES Y NÚMEROS AL CUADRADO

#def cuadrado(num1, num2, num3):
   # lista = [num1, num2, num3]
   # cuadra = [num1 * num1, num2 * num2, num3 * num3]
   # print('El primer resultado es:', lista[0], 'y su cuadrado es:', cuadra[0])
   # print('El segundo resultado es:', lista[1], 'y su cuadrado es:', cuadra[1])
   # print('El tercer resultado es:', lista[2], 'y su cuadrado es:', cuadra[2])

#cuadrado(int(input('Ingrese el primer número: ')), int(input('Ingrese el segundo número: ')), int(input('Ingrese el tercer número: ')))

"""
def multiplo(a, b):
    ej1 = a / b
    ej2 = b / a

    for x in str(ej1):
        if x == '.':
            return 'Tiene coma'

    for x in str(ej2):
        if x == '.':
            return 'Tiene coma'"""

    #if type(ej1) == int:
        #return 'A es múltiplo de B'
    #else:
       #return 'A NO es múltiplo de B'

    #if type(ej2) == int:
        #return 'A es múltiplo de B'
    #else:
        #return 'A NO es múltiplo de B'

#multiplo(int(input('Ingrese un número "A": ')), int(input('Ingrese un número "B": ')))

"""def sumando(*nums):
    total = 0
    for n in nums:
        total += n
    return total"""

"""print(sumando(21, 1000, 420, 12))"""

def multiplicando(*nums):
    total = 0