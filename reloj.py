
def proceso(nombre):
    ent = open(nombre)
    sal = open('grado_salida.txt', 'w')
    grado = int(ent.readline())
    if (grado % 6) == 0:
        sal.write('Y'+'\n')
    else:
        sal.write('N'+'\n')
    sal.close()

if __name__ == '__main__':
    proceso('grado.txt')
