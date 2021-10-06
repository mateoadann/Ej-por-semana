#     • 5. Menú de Opciones Básico
# Diseñar un programa que según la opción ingresada por el usuario permita realizar las siguientes operaciones:
#
# Si la opción es 1 mostrar la superficie de un triángulo.
# Si la opción ingresada es 2 mostrar el perímetro del triángulo.
# Si la opción ingresada es 3 informar la longitud del lado menor.
# Si la opción ingresada no fue ni 1, 2 o 3 informar un mensaje de error.
# Para ello usted deberá ingresar por teclado el número de opción y el valor de los tres lados del triángulo.


print('Opción 1: Se muestra el area del triangualo.')
print('Opción 2: Se muestra el perímetro del triángulo.')
print('Opción 3: Se muestra la longitud de lado menos del triángulo.')
print('Opción 4: Salir.')
option = int(input('Ingrese la opción que quiera: '))

while option != 4:
    lado_a = float(input('Ingrese la medidad del lado A: '))
    lado_b = float(input('Ingrese la medidad del lado B: '))
    lado_c = float(input('Ingrese la medidad del lado C (base): '))
    if option == 1:
        altura = pow((lado_a * lado_b),2)
        base = lado_c
        area = round(((base * altura) / 2), 2)
        print('El area del tríangulo es', area, 'm2')
    elif option == 2:
        perimetro = lado_a + lado_b + lado_c
        print('El perímetro del tríangulo es', perimetro, 'm')
    elif option == 3:
        lado_M = min(lado_a, lado_b, lado_c)
        if lado_M == lado_a:
            print('EL lado menor de triángulo es el lado A', lado_a)
        elif lado_M == lado_b:
            print('EL lado menor de triángulo es el lado B', lado_b)
        else:
            print('EL lado menor de triángulo es el lado C', lado_c)

    print()
    option = int(input('Ingrese la opción que quiera: '))

print()
print('Fin del programa.')