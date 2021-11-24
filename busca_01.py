def inicializa():
    lista = [7,20,5,1,32,44,27,2,9]
    elemento = 7
    return lista, elemento

def busqueda(lista, elemento):
    largo = len(lista)
    esta = False
    i = 0
    while i < largo:
        if elemento == lista[i]:
            esta = True
        i = i + 1
    return esta

def muestra_resultado(resultado,elemento):
    if resultado == True:
        print ('El elemento',elemento,'esta en la lista')
    else:
        print ('El elemento',elemento,'NO esta en la lista')
    return

if __name__ == '__main__':
    lista, elemento = inicializa()
    resultado = busqueda(lista, elemento)
    muestra_resultado(resultado, elemento)
