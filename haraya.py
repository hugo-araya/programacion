def valida_entero(numero):
    pass

def valida_mail(correo):
    pass

def valida_real(numero):
    contar = numero.count('.')
    if contar > 1:
        return False, numero
    else:
        if contar == 0:
            if numero.isdigit() == True:
                real = float(numero)
                return True, real
            else:
                return False, numero
        if contar == 1:
            dividir = numero.split(".")
            if dividir[0].isdigit() == True:
                ok1 = True
            else:
                if len(dividir[0]) == 0:
                    ok1 = True
                else:
                    ok1 = False
            if dividir[1].isdigit() == True:
                ok2 = True
            else:
                if len(dividir[1]) == 0:
                    ok2 = True
                else:
                    ok2 = False

            if (ok1 == True) and (ok2 == True):
                real = float(numero)
                return True, real
            else:
                return False, numero

def presentacion():
    print("Creador: Hugo Araya Carrasco")
    print("------------------------------")

def fin():
    print('-------------')
    print("Eso es todo")
    print("-------------")



