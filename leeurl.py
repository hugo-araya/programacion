from urllib.request import urlopen
with urlopen('http://www.utalca.cl') as response:
    for line in response:
        line = line.decode('utf-8')
        line = line.rstrip('\n')
        if (line.find('keywords') != -1):
            print(line)