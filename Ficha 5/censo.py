sexo = input('Ingrese su sexo (M/F) ->')
cant_hombres, cant_mujeres = 0, 0

while sexo=='M' or sexo=='F':
    # Datos adicionales ->
    edad = int(input('Ingrese su edad ->'))
    # Proceso
    if sexo == 'M':
        cant_hombres += 1
    else:
        cant_mujeres += 1
    # Segunda lectura:
    sexo = input('Ingrese su sexo(M/F) ->')

# Results
if cant_mujeres == cant_hombres:
    print('Son la misma cantidad de hombres que mujeres. ')

else:
    if cant_hombres > cant_mujeres:
        print('Hay mas hombres. ')
    else:
        print('Hay mas mujeres')
