import random

def lectura_archivo(nombre, cant):
    ent = open(nombre)
    lista = []
    i = 0
    while i < cant:
        nro = int(ent.readline())
        lista.append(nro)
        i = i + 1
    ent.close()
    return lista

def inicializar():
    lista = lectura_archivo('repetidos_con.txt', 1000)
    elem = random.randint(1,1000)
    return lista, elem

def busqueda(lista, elem):
    largo = len(lista)
    respuesta = False
    i = 0
    cont = 0
    while i < largo:
        cont = cont + 1
        if elem == lista[i]:
            respuesta = True
            return respuesta, cont
        i = i + 1
    return respuesta, cont

def desplegar(respuesta, cont, elem):
    if respuesta == True:
        print('El elemento', elem,'se encuentra en la lista (',cont,')')
    else:
        print('El elemento', elem,'NO se encuentra en la lista (',cont,')')
    print(lista)

if __name__ == '__main__':
    lista, elem = inicializar()
    respuesta, cont = busqueda(lista, elem)
    desplegar(respuesta, cont, elem)