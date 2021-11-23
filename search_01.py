def inicializar():
    lista = [3,6,2,8,4,10,9,1,45,23,11]
    elem = 110
    return lista, elem

def busqueda(lista, elem):
    largo = len(lista)
    respuesta = False
    i = 0
    while i < largo:
        if elem == lista[i]:
            respuesta = True
        i = i + 1
    return respuesta

def desplegar(respuesta):
    if respuesta == True:
        print('El elemento se encuentra en la lista')
    else:
        print('El elemento NO se encuentra en la lista.')

if __name__ == '__main__':
    lista, elem = inicializar()
    respuesta = busqueda(lista, elem)
    desplegar(respuesta)