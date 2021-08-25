milista = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
'''
i = 0
largo = len(milista)
while i < largo:
    print(milista[i])
    i = i + 1
print("Se acabo la lista")

for elemento in milista:
    print(elemento)

i = -1
while i >=  -5:
    print(milista[i])
    i = i - 1

for i in range(5):
    print(milista[i])


print(milista[1:3])
print(milista[1:])
print(milista[:3])
print(milista[:])

milista = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
otra = milista[:]
milista[2] = 'Cosa nueva'
print(milista)
print(otra)
'''
print(milista)
milista.append('Hola')
print(milista)
print("Se acabo la lista")