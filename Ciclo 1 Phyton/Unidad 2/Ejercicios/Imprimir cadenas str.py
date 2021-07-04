#imprimr cadenas de str de varias formas
camellos = 42
ver ='Hevisto %d camellos' % camellos #% cumple funcion de .format. he imprimir str
ver1 ='Hevisto {} camellos'.format(camellos) # #una forma de imprimir str
ver2 ='Hevisto '+str(camellos)+ ' camellos' #una forma de imprimir str

print(ver)
print(ver1)
print(ver2)