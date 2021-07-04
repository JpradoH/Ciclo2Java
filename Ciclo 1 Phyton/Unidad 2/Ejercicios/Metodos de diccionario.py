'''diccionario = {'Eduardo': 1, 'Fernando':2, 'Uriel':3, 'Rafael': 4}
print(diccionario)

print(diccionario.keys())  #imprime solo las llaves  

print(diccionario.values()) #imprime solo los valores

'''
'''#acceder a un valor determinado en el diccionario
versiones = dict(python=2.7, zope=2.13, plone=5.1, django=2.1)
versiones['zope']

#metodo clear() limpia o elimina el contenido del diccionario.
versiones = dict(python=2.7, zope=2.13, plone=5.1)
print(versiones)
#compueba el metodo clear()
versiones.clear()
print(versiones)'''

#metodo copy() realiza una copia del diccionario
versiones = dict(python=2.7, zope=2.13, plone=5.1)
otra_versiones = versiones.copy()
print(versiones == otra_versiones)
#comprueba el metodo copy()
print(versiones)
print(otra_versiones)