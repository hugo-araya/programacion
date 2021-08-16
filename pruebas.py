#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Autores: Autor 1 -- Autor 2 -- Autor 3

# import <biblioteca>
import haraya as ha
#from haraya import *
#import haraya
#Declaración de funciones.

if __name__ == "__main__":
    ha.presentacion()
    numero = input("Ingrese numero: ")
    status, numero = ha.valida_real(numero)
    if status == True:
        print('Numero es real: ', numero)
    else:
        print('No corresponde a un numero real')
    ha.fin()




# No escribir codigo en este nivel.