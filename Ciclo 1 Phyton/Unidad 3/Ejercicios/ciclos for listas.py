lista = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
#imprimir lista copleta
'''print(lista)'''
#imprimir primer componente [1,2,3]
'''print(lista[0])'''
#imprimir primer componente [1,2,3]
#imprimir el valor del primer componente [1,2,3]=[1]
'''print(lista[0][0])'''
#imprimir con un for la lista contenida en la primer componente
for x in range(len(lista[0])):
    print(lista[0][x])
#imprimir cada elemento entero de cada lista contenida en la lista
for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])
        