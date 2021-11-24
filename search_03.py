import random

def lista_con_repetidos(largo):
    l = []
    i = 0
    while i < largo:
        l.append(random.randint (1,2000000))
        i = i + 1
    return l

def lista_sin_repetidos(largo):
    l = []
    i = 0
    while i < largo:
        nro = random.randint (1,2000000)
        if nro not in l:
            l.append(nro)
            i = i + 1
    return l

def grabar_archivo(nombre,l):
    sal = open(nombre,'w')
    for elem in l:
        sal.write(str(elem)+'\n')
    sal.close()

if __name__ == '__main__':
    limite = 1000000
    l1 = lista_con_repetidos(limite)
    l2 = lista_sin_repetidos(limite)
    grabar_archivo('repetidos_con.txt',l1)
    grabar_archivo('repetidos_sin.txt',l2)