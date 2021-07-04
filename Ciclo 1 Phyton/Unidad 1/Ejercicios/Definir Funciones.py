#crear una funición
'''def sumar(n1, n2)->float:
    suma = n1 + n2
    return suma
print(sumar(10, 25))
'''
#Otra forma

def imprime_cosas():
    '''ejemplo de lo quepuede hacer la funcion imprimi_cosas() al ejecutar help'''
    #codigo de la función
    print("la clase esta genail")
    print("python es lo maximo")
imprime_cosas()
help(imprime_cosas)

#utilizar funciones dentro de otras funciones previamente definidas
def repetir_cosas(): 
    imprime_cosas()
    imprime_cosas()
repetir_cosas()

