
def proceso(nombre):
    ent = open(nombre)
    sal = open('grado_salida.txt', 'w')
    grado = int(ent.readline())
    i = 0
    lista = []
    while i <=180:
        divisible = i % 6
        if divisible == 0:
            lista.append(i)
        i = i + 1
    print(lista)
    if grado in lista:
        sal.write('Y'+'\n')
    else:
        sal.write('N'+'\n')
    sal.close()

if __name__ == '__main__':
    proceso('grado.txt')
