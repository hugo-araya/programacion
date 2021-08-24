#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Nombre del autor: Hugo Araya Carrasco

# import <biblioteca>
# from <biblioteca> import <modulo>
# import <biblioteca> as <alias>

#Declaración de funciones
def calculo_dv(rut):
    return True

def verifica(rut):
    guion = rut.count('-')
    if guion != 1:
        return False
    else:
        parte = rut.split('-')
        if len (parte[1]) != 1:
            return False
        else:
            if parte[1] != 'k':
                if not(parte[1].isdigit()):
                    return False
        # La primera parte
        if not(parte[0].isdigit()):
            return False
        else:
            ok1 = calculo_dv(rut)
            return ok1

#Código principal
if __name__ == '__main__':
    rut = input("RUT: ")
    ok = verifica(rut)
    if ok == True:
        print("Rut esta validado")
    else:
        print("Rut incorrecto")

    print ('eso es todo')

