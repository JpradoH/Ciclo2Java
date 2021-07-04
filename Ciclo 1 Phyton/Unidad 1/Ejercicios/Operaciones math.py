#pow es la operacion de potencia definiendo base y exponente
pot = pow(2, 10)
#print(pot)
'''raiz=sqrt(81) genra un error porque la operacion sqrt que 
significa raizcuadrada, esta funcion depende de de la liberia
math'''
'''operaciones matematicascon libreria math y las diferentes 
maneras de usarla'''
#opcion 1
import math 
raiz = math.sqrt(81)
#print(raiz)
#opcion 2
import math as m
raiz = m.sqrt(81)
#print(raiz)
#opcion 3
'''de esta forma se hace referencia de forma muy espesifica 
que funcion se desea trabajar, ya sea sqrt(raiz), cos(coseno), 
tan(tangente)'''
from math import sqrt 
raiz = sqrt(81)
#print(raiz)
#si se desea usar todos los paquetes en este sentido se pondra asterisco * pero solo si se va ausar realmente
from math import *
from funciones import *
import os
os.system('cls')

var1 = 2
var2 = 10
pot = pow(var1, var2)
#pot = pow(2, 10)
#raiz = sqrt(81)
#coseno = cos(45)
#tang = tan(90)
'''
formas de imprimir usando str .format
'''
#print('{} elevado a {} es: {}'.format(var1, var2, pot))
#print(str(var1) +' elevado a ' + str(var2) + ' es: '+ str(pot))
#print('potencia:'+str(pot))
'''
print(raiz)
print(coseno)
print(tang)

print(sumar(10, 15))
print(secante(90))
'''