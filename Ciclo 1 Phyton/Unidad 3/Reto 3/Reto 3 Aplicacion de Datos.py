def analisis_datos_nav(lista_datos_nav: list) ->dict:
    lista_enteros = []
    lista_flotantes = []
    lista_cadenas = []
    lista_booleanos =[]
    lista_tuplas = []
    lista_listas = []
    lista_diccionarios =[]
    for elem in lista_datos_nav:
        if type(elem) == int:
            lista_enteros.append(elem)
        elif type(elem) == float:
            lista_flotantes.append(elem)
        elif type(elem) == str:
            lista_cadenas.append(elem)
        elif type(elem) == bool:
            lista_booleanos.append(elem)
        elif type(elem) == tuple:
            lista_tuplas.append(elem)
        elif type(elem) == list:
            lista_listas.append(elem)
        elif type(elem) == dict:
            lista_diccionarios.append(elem)
    
    app_datos = {
        'int': lista_enteros,
        'float': lista_flotantes,
        'str': lista_cadenas,
        'bool': lista_booleanos,
        'tuple': lista_tuplas,
        'list': lista_listas,
        'dict': lista_diccionarios
    }
    return app_datos

print(analisis_datos_nav(
    [560, 'a', False, 10, 23.2, True, 'x', (1, ), {'a':'a'}, [23, 'b']]))
print(analisis_datos_nav(
    ['xyz', 0.2, 10, 23.2, '0', (0.1, 3.0,), {}, [True, '1']]))
print(analisis_datos_nav(
    [560, 'a', {'m':'m', 1:1}, 'x',(1, ), {'a':'a'},[23]]))
print(analisis_datos_nav(
    [110, 23.2, 0,3, True, False,(1, 2, 3),[23]]))
print(analisis_datos_nav(
    ['123','hola', True, 'x', (1, ), {'a':'a'}, [23, 'm']]))
