import matplotlib.pyplot as plt

def lectura(nombre, region):
    ar = open(nombre)
    X = []
    Y = []
    for linea in ar:
        linea = linea.rstrip('\n')
        lista = linea.split(',')
        if lista[1] == region:
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
    region = input('Indique el codigo de la región a consultar: ')
    X, Y = lectura('casos_por_region.csv', region)
    Graficar(X, Y)
    Detalle(X, Y)