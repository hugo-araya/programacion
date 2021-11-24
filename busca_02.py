def inicializa():
    lista = [7,20,5,1,32,44,27,2,9]
    elemento = 320
    return lista, elemento

def busqueda(lista, elemento):
    largo = len(lista)
    contador = 0
    esta = False
    i = 0
    while i < largo and esta != True:
        contador = contador + 1
        if elemento == lista[i]:
            esta = True
        i = i + 1
    return esta, contador

def muestra_resultado(resultado,elemento, contador):
    if resultado == True:
        print ('El elemento',elemento,'es encontrado en', contador, 'iteraciones')
    else:
        print ('El elemento',elemento,'NO es encontrado en', contador, 'iteraciones')
    return

if __name__ == '__main__':
    lista, elemento = inicializa()
    resultado, contador = busqueda(lista, elemento)
    muestra_resultado(resultado, elemento, contador)
