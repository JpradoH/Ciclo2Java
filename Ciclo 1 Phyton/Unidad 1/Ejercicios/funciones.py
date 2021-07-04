'''
en este ejercicio se realizo funciones modulares imprimiendo
en el archivo Operaciones math, realizando importes de 
funciones aqui definidas
'''

from math import cos

def sumar(n1, n2)->int:
    '''esta funcion permite sumar dos numeros recibidos como 
    argumentos y retorna el total'''
    suma = n1 + n2
    return suma

def secante(n)->float:
    sec = 1 / cos(n)
    return sec
    
def restar(n1, n2)->int:
    resta = n1 - n2
    return resta
'''print(restar(n2=3, n1=2))
print(restar(3, 1))'''

'''def saludar(nombre, mensaje="hola"):
    print(mensaje, nombre)
    return 'hola sopla cotopla'
print(saludar('pepe grillo'))'''