def  pereira_es_potencia(x:int, y:int)->bool:
    r = False
    if y == 1 or y == 0 or y < 0: #if y <= 1:
        r = False
    elif x ** 1 == y:
        r = True
    elif x ** 2 == y:
        r = True
    elif x ** 3 == y:
        r = True
    elif x ** 4 == y:
        r = True
    elif x ** 5 == y:
        r = True
    return r
print(pereira_es_potencia(2, 3))