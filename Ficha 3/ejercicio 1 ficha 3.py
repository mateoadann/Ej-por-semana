# 1. Plazo fijo
# Desarrollar un programa que cargue por teclado la cantidad de dinero depositada en plazo fijo por un cliente de un banco
# y calcular el saldo que tendrá esa cuenta al vencer el plazo fijo, sabiendo que el interés pactado era de 2.3%
# y que el banco cobra una tasa fija de gastos por servicios financieros igual $20 por cuenta.

# Dates:
saldo = float(input('Ingrese el saldo a depositar (plazo fijo de 12 meses): '))

# Process:
final = (saldo * 0.23) * 12
# Results
print('Al finalizar el plazo fijo usted tendrá', final + saldo)
print('El saldo final es de ', (final + saldo) - 20)
