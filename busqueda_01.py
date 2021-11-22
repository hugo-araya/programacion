def inicializa():
    lista = [3,7,4,1,2,8,9,15]
    return lista

def respuesta(ok):
    if ok == True:
        print ('El elemento esta en la lista')
    else:
        print ('El elemento NO esta en la lista')

def busqueda(lista, elem):
    largo = len(lista)
    i = 0
    ok = False
    while i < largo:
        if elem == lista[i]:
            ok = True
        i = i + 1
    return ok

if __name__ == "__main__":
    elem = 8
    lista = inicializa()
    ok = busqueda(lista, elem)
    respuesta(ok)
