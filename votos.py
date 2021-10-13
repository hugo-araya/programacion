def lectura(nombre):
    ent = open(nombre)
    cant = int(ent.readline())
    linea = (ent.readline()).rstrip('\n')
    votos_string = linea.split(' ')
    votos = []
    for voto in votos_string:
        votos.append(int(voto))
    suma_votos = sum(votos)
    votos.sort(reverse=True)
    porcentajes = []
    for voto in votos:
        porcentaje = voto * 100 / suma_votos
        porcentajes.append(porcentaje)
    ent.close()
    return porcentajes

def resultado(porcentajes):
    sal = open('votos_salida.txt', 'w')
    cand1 = porcentajes[0]
    cand2 = porcentajes[1]
    if cand1 >= 45:
        sal.write('1'+'\n')
    else:
        if cand1 >= 40:
            if cand1 >= cand2+10:
                sal.write('1'+'\n')
            else:
                sal.write('2'+'\n')
    sal.close()



if __name__ == "__main__":
    porcentajes = lectura('votos.txt')
    resultado(porcentajes)