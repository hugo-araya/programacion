#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Autores: Autor 1 -- Autor 2 -- Autor 3

#import <biblioteca>
#import haraya
import haraya as HA
import os
#from haraya import *
#import haraya
#Declaración de funciones.

if __name__ == "__main__":
    HA.presentacion()

    numero = input("Ingrese numero: ")
    status, numero = HA.valida_real(numero)
    if status == True:
        print('Numero es real: ', numero)
    else:
        print('No corresponde a un numero real')
    HA.fin()




# No escribir codigo en este nivel.