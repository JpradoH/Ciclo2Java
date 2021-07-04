# saca "El valor es 12
print ("El valor es {}".format(12))

# saca "El valor es 12.3456
print ("El valor es {}".format(12.3456))

# Tres conjuntos {}, el primero para el primer parámetro de format(), el segundo para el segundo
# y así sucesivamente.
# saca "Los valores son 1, 2 y 3"
print ("Los valores son {}, {} y {}".format(1,2,3))

# Entre las llaves podemos poner la posición del parámetro. {2} es el tercer parámetro de format()
# {0} es el primer parámetro de format.
# saca "Los valores son 3, 2 y 1" siempre y cuando este dentro del rango de posicion.
print ("Los valores son {2}, {1} y {0}".format(1,2,3))

#re fiere al tema de parametros por omicion.
# saca "2 y 1"
print ("{pepe} y {juan}".format(juan=1, pepe=2))
