def lectura(nombre):
    ar = open(nombre)
    palabras = []
    for linea in ar:
        linea = linea.rstrip('\n')
        palabras.append(linea)
    ar.close()
    return palabras

def proceso(datos):
    sal = open('salida.txt','w')
    for palabra in datos:
        if palabra.find('i') != -1:
            sal.write('N'+'\n')
        else:
            sal.write('S'+'\n')
    sal.close()

if __name__ == "__main__":
    datos = lectura('laino.txt')
    proceso(datos)
