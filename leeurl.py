from urllib.request import urlopen
lista = ['www.ucm.cl','www.utalca.cl','www.emol.cl']
for direc in lista:
    ok = False
    with urlopen('http://'+direc) as response:
        for line in response:
            line = line.decode('utf-8')
            line = line.rstrip('\n')
            if (line.find('keywords') != -1):
                ok = True
                posi = line.index('content=')
                palabras = line[posi+9:]
                print(palabras)
                print('\n')
        if ok == False:
            print('Pagina sin Keyword: ', direc)
            print('\n')