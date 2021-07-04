
'''ejemplo ciclos con for'''

#crear una lista por asignacion
#la lista debe tener 2 elementos
#cada elemento debe ser una lista de 5 enteros
lista =[[1,3,5,7,9], [2,4,6,8,10]]
for k in range(len(lista)):
#calcular y mostrar la suma de cada lista contenida en la principal
    suma = 0
    for x in range(len(lista[k])):
        suma = suma + lista[k][x]
        print (suma)
        
#for x in range(len(lista[1])):
#...print(lista[1][x])

for y in range(len(lista)):
    for x in range(len(lista[y])):
        print (lista[y][x])
