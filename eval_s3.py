import matplotlib.pyplot as plt

def lectura(nombre):
    ar = open(nombre)
    X = []
    Y = []
    for linea in ar:
        linea = linea.rstrip('\n')
        lista = linea.split(',')
        if lista[0] == 'Maule':
            X.append(lista[2])
            Y.append(float(lista[5]))
    ar.close()
    return X, Y

def Graficar(X, Y):
    plt.title('Evaluacion primera')
    plt.bar(X, Y)
    plt.xticks(rotation = 90)
    plt.show()

def Detalle(X, Y):
    i = 0
    while i < len(X):
        print (X[i], ' --- ', Y[i])
        i = i + 1

if __name__ == "__main__":
    X, Y = lectura('casos_por_region.csv')
    Graficar(X, Y)
    Detalle(X, Y)