def lectura(nombre):
    ar = open(nombre)
    candidatos = int(ar.readline().rstrip('\n'))
    linea = ar.readline()
    linea = linea.rstrip('\n')
    votos = linea.split(' ')
    ar.close()
    return votos

def proceso(votos):
    sal = open('salida_votos.txt','w')
    total = 0
    for voto in votos:
        total = total + int(voto)

    status = False
    for voto in votos:
        voto = int(voto)
        porcentaje = voto * 100 / total
        if porcentaje >= 45:
            status = True
    if status == True:
        sal.write('1'+'\n')
    else:
        # La segunda condicion.
        sal.write('2' + '\n')
    sal.close()

if __name__ == "__main__":
    votos = lectura('votos.txt')
    proceso(votos)
