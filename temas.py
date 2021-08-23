'''
milista = ['uno', 'dos', 'tres', 'cuatro', 'cinco']

i = 0
largo = len(milista)
while i < largo:
    elem = milista[i]
    print (elem)
    i = i + 1
print ('Fin del While')

for elem in milista:
    print(elem)
print ('Fin del For')

for i in range(2,largo):
    print(milista[i])


print('\n\nEjemplo de copia vs aasignacion\n')
milista = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
nueva = milista[:]
print(milista)
print(nueva)
milista[3] = 'otro'
print (milista)
print(nueva)

milista = ['uno', 'dos', 'tres', 'cuatro', 'cinco'] 
lista2 = ["Hola", "Jovenes"] 
lista2.extend(milista)
print(milista)
'''
milista = ['uno','dos','tres','cuatro', 'cinco']
milista.sort()
print(milista)