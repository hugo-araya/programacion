'''
archi = open('ar_s2.txt','a')

linea=archi.readline()
while linea != '':
    linea = linea.rstrip('\n')
    print(linea)
    linea=archi.readline()
archi.close()

for linea in archi:
    linea = linea.rstrip('\n')
    print(linea)
archi.close()

lineas = archi.readlines()
print(lineas)
archi.close()
linea2 = []
for elem in lineas:
    elem = elem.rstrip('\n')
    linea2.append(elem)
    print(elem)
print(linea2)

i = 0
while i < 5:
    linea = input("Ingrese algo: ")
    archi.write(linea+'\n')
    i = i + 1
archi.close()

lista = ['Algo 1\n', 'Algo 2\n', 'Algo 3\n', 'Algo 4\n', 'Algo 5\n',]
archi.writelines(lista)
'''
import math

import matplotlib.pyplot as plt
x = []
y = []
i = 0
while i < 10:
    j = math.cos(i)
    x.append(i)
    y.append(j)
    i = i + 0.1

plt.grid()
plt.plot(x,y)
plt.show()










