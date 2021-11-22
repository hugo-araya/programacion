# Busqueda binaria

def inicializa():
    lista = [1,2,3,4,7,8,9,11,15,16]
    return lista

def respuesta(ok, cont):
    if ok == True:
        print ('El elemento esta en la lista y hace', cont, 'preguntas.')
    else:
        print ('El elemento NO esta en la lista', cont, 'preguntas.')

def busqueda(lista, elem):
    sal = open('error.txt', 'w')
    largo = len(lista)
    lf = largo - 1
    li = 0
    ok = False
    contador = 0
    while (lf - li) != 1:
        print(li, lf, ok)
        sal.write(str(li)+" "+str(lf)+" "+str(ok)+'\n')
        pm = (li+lf)//2
        if lista[pm] == elem:
            ok = True
            return ok, contador
        else:
            if elem > lista[pm]:
                li = pm
            else:
                lf = pm
        contador = contador + 1
    if ok == False:
        if lista[li] == elem or lista[lf] == elem:
            ok = True
    return ok, contador

if __name__ == "__main__":
    elem = 160
    lista = inicializa()
    ok, cont = busqueda(lista, elem)
    respuesta(ok, cont)
