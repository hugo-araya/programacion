ar = open('datos.txt')
for linea in ar:
    linea.rstrip('\n')
    dato = linea.split(',')
    largo = len(dato)
    i = 0
    salida = ''
    while i< largo:
        salida = salida + dato[i] + ' - '
        i = i + 1
    print(salida)
ar.close()
