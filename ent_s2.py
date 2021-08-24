
milista = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
'''
i = 0
while i < len(milista):
    print(milista[i])
    i = i + 1
print("Fin.....")

for elem in milista:
    print(elem)
print("Fin ......")

for i in range(len(milista)):
    print(milista[i])
print ("Fin ....")

print(milista)
print(milista[1:3])
print(milista[1:])
print(milista[:3])
print(milista[:])

otra = milista[:]
print(milista)
print(otra)
milista[2] = "Otra cosa"
print(milista)
print(otra)


milista = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
milista.insert(1, 'Hola')
print(milista)
milista.append('Seis')
print(milista)
'''
print(milista)
milista.append('dos')
print(milista)
ix = milista.index('dos')
print(ix)
nuevo = milista[ix+1:]
print(nuevo)
ix = nuevo.index('dos')
print(ix)


