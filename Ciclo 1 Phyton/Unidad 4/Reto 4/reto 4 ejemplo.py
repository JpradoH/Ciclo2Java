#todo lo visto es solo un ejemplo de como se podria ejecutar el reto 4 
l = []
cad = 'hola hola mundo mundo hola abc'
cad = cad.split()
for c in cad:
    t = (c, cad.count(c))
    l.append(t)
conj = set(l)
l2 = list(conj)
l2.sort()
print(l2)

#opcion dos para resolver y y tener en cuenta en el reto 4
def palabras_rep(frase: str):
    l = []
    cad = frase.split()
    for c in cad:
        if cad.count(c) > 1:
            t = (c, cad.count(c))
            l.append(t)
    conj = set(l)
    l2 = list(conj)
    l2.sort()
    return l2

print(list(map(palabras_rep, 'hola hola mundo mundo hola abc'.split('123'))))