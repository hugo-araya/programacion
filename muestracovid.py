import matplotlib.pyplot as plt

def lectura(nombre):
    ar = open(nombre)
    fecha = ar.readline()
    fecha = fecha.rstrip('\n')
    X = fecha.split(',')
#   X = ((ar.readline()).rstrip('\n')).split(',')
    XX = list(range(len(X)))
    casos = ar.readline()
    casos = casos.rstrip('\n')
    casos = casos.split(',')
    Y = []
    for elem in casos:
        Y.append(float(elem))
    return X, Y

def graficar(X, Y):
    plt.title('Resumen por mes')
    plt.bar(X, Y)
    plt.show()

def finalizar(X, Y):
    print('Son', len(Y), 'dias' )

def datos_resumen_por_mes(X, Y):
    nro = 3
    X1 = []
    Y1 = []
    while nro <13:
        if nro <10:
            X1.append('2020-0'+str(nro))
        else:
            X1.append('2020-'+str(nro))
        nro = nro + 1
    nro = 1
    while nro <10:
        X1.append('2021-0'+str(nro))
        nro = nro + 1
    largo = len(X)
    i = 0
    ii = 0
    suma = 0
    while i < largo:
        if X[i].find(X1[ii]) != -1:
            suma = suma + Y[i]
            i = i + 1
        else:
            Y1.append(suma)
            suma = 0
            ii = ii + 1
    Y1.append(suma)
    return X1, Y1

if __name__ == "__main__":
    X, Y = lectura('TotalesNacionalesResumen.csv')
    X1, Y1 = datos_resumen_por_mes(X, Y)
    graficar(X1, Y1)
    finalizar(X, Y)
#   xr, yr = resumen_por_mes(X, Y)
