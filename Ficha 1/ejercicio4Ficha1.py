# 4. Últimos dígitos
# Desarrolle un programa que cargue un número entero por teclado,
# y muestre el último dígito del mismo (por un lado) y los dos últimos dígitos (por otro lado)

# Dates
entero = int(input('Ingrese un número entero: '))

# Process
operation1 = entero % 10
operation2 = entero % 100
operation3 = entero % 1000

# Results
print('último dígito del número', operation1)
print('Los dos últimos dígitos del número', operation2)
print('Los tres últimos dígitos del número', operation3)
