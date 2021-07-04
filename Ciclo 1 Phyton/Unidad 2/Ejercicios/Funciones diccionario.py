#funcion len hace el mismo metodo que en los str que es contar 
#solo que no se centara en el conteo de campos de un valor de 0 a no
#si no que contara el numero de llaves dentro del diccionario
versiones = dict(python=2.7, zope=2.13, plone=5.1)
len(versiones)

usuario = {
    'nombre': 'Nombre del usuario',  #llave 1 nombre.
    'edad' : 23,                     #llave 2 edad.
    'curso': 'Curso de Python',      #llave 3 curso.
    'skills':{                       #llave 4 skills
        'programacion' : True,   #llave 1 programacion.
        'base_de_datos': False   #llave 2 base_de_datos
    },
    'No medallas' : 10               #llave 5 No medallas.
}
print(len(usuario))
print(len(usuario["skills"]))