# Nombre 1
# Nombre 2

def inicializa():
    digi = ['.***..','*.....','*.*...','**....','**.*..','*..*..','***...','****..','*.**..','.**...']
    return digi

def lectura(nombre):
    ent = open(nombre)
    cant = int(ent.readline())
    l1 = ent.readline().rstrip('\n')
    l2 = ent.readline().rstrip('\n')
    l3 = ent.readline().rstrip('\n')
    l1 = l1.split(' ')
    l2 = l2.split(' ')
    l3 = l3.split(' ')
    ent.close()e
    listad = []
    i = 0
    while i < cant:
        d = l1[i] + l2[i] + l3[i]
        listad.append(d)
        i = i + 1
    sal = open('brailesalida.txt', 'w')
    salida = ''
    for elem in listad:
        posi = digitosb.index(elem)
        salida = salida + str(posi)
    sal.write(salida+'\n')
    sal.close()

if __name__ == "__main__":
    digitosb = inicializa()
    numeros = lectura('brailedatos.txt')
