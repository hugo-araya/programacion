def inicializa():
    lista = [3, 7, 4, 1, 2, 8, 9, 15]
    return lista

def respuesta(ok, cont):
    if ok == True:
        print ('El elemento esta en la lista y hace', cont, 'preguntas.')
    else:
        print ('El elemento NO esta en la lista', cont, 'preguntas.')

def busqueda(lista, elem):
    largo = len(lista)
    i = 0
    ok = False
    contador = 0
    while i < largo:
        contador = contador + 1
        if elem == lista[i]:
            ok = True
            break
        i = i + 1
    return ok, contador

if __name__ == "__main__":
    elem = 8
    lista = inicializa()
    ok, cont = busqueda(lista, elem)
    respuesta(ok, cont)
