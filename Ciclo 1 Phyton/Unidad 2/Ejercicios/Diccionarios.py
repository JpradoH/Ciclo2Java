#se compone de un valor llamado llave y un valor,ambos pueden ser int, float,bool
#los diccionario pueden contener tuplas condiocionales if,elif,else,
# listas o hasta otro diccionario.
'''dicionario = {'total': 55} 
print(dicionario)

otrodiccionario = {'copia': 123.23}
print(otrodiccionario)

dicionariovacio = {}
print(dicionariovacio)

varriadodicionario = {'total': 55, 'descuento': True, 15:'15'}
print(varriadodicionario)

diccionarioexcel = {'nombre':5+2, 'telefono':336547, 'edad':35, 'ciudad':'bogota'}
print(diccionarioexcel)

#una de las formas de abreviar la funcion es usando = dict
#que remplaza ={}. ejemplo
dicionario1 = dict(total = 55, descuento= True, subtotal = 15)
print(dicionario1)'''

'''#asi se pueden llamar a las llaves que ahi dentro de un diccionario definido
usuario = {
    'nombre': 'Nombre del usuario',
    'edad' : 23, 
    'curso': 'Curso de Python',
    'skills':{
        'programacion' : True,
        'base_de_datos': False
    },
    'No medallas' : 10
}
#cada elemento de la llave que se requiera debe ir entre [' ']
print(usuario['curso'])
print(usuario['skills']['base_de_datos'])'''

#agregar valores a un diccionario vacio {}
diccionario = dict()
print(diccionario)
#se le declara que ['marca'] sera igual a un valor y sera impreso
#especificamente de forma posterior.
diccionario['marca'] = 'Mazda'
print(diccionario['marca'])