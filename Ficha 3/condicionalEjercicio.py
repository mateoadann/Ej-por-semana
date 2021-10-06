# Dates
num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
num3 = int(input('Ingrese el tercer número: '))

# Process
if num1 > num2:
    mayor = num1
else:
    mayor = num2

if num3 > mayor:
    mayor = num3

# Results
print('El número mayor es: ', mayor)
