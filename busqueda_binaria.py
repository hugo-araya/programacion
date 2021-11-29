# Busqueda binaria

def inicializa():
    ent = open('repetidos_sin.txt')
    i = 0
    lista= []
    while i <1000:
        nro = int(ent.readline().rstrip('\n'))
        lista.append(nro)
        i = i + 1
    lista.sort()
    ent.close()
    return lista

def respuesta(ok, cont):
    if ok == True:
        print ('El elemento esta en la lista y hace', cont, 'preguntas.')
    else:
        print ('El elemento NO esta en la lista', cont, 'preguntas.')

def busqueda(lista, elem):
    sal = open('error.txt', 'w')
    sal.write(str(elem)+'\n')
    largo = len(lista)
    lf = largo - 1
    li = 0
    ok = False
    contador = 0
    while (lf - li) != 1:
        pm = (li+lf)//2
        sal.write(str(li)+" "+str(lf)+" "+str(ok)+" "+str(lista[pm])+('\n'))
        contador = contador + 1
        if lista[pm] == elem:
            ok = True
            return ok, contador
        else:
            if elem > lista[pm]:
                li = pm
            else:
                lf = pm
    if ok == False:
        contador = contador + 1
        if lista[li] == elem or lista[lf] == elem:
            ok = True
    return ok, contador

if __name__ == "__main__":
    elem = 92732
    lista = inicializa()
    ok, cont = busqueda(lista, elem)
    respuesta(ok, cont)
