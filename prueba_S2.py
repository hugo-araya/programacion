import matplotlib.pyplot as plt

def lectura_camas(nombre):
    ar = open(nombre)
    X = []
    Y = []
    for linea in ar:
        linea = linea.rstrip('\n')
        lista = linea.split(',')
        X.append(lista[0])
        Y.append(int(lista[3]))
    return X, Y

def Graficar(X, Y):
    plt.title('Grafico de datos')
    plt.plot(X, Y)
    plt.show()

def Detalle(X, Y):
    i = 0
    while i < len(X):
        print('En el dia', X[i], 'hay', Y[i], 'camas ocupadas.' )
        i = i + 1

if __name__ == "__main__":
    X, Y = lectura_camas('ventiladores_ocupados.csv')
    Graficar(X, Y)
    Detalle(X, Y)
