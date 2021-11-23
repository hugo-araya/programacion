import random

def lista_aleatoria(largo):
    l = []
    i = 0
    while i < largo:
        l.append(random.randint (1,1000))
        i = i + 1
    return l

def inicializar():
    lista = lista_aleatoria(1000)
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