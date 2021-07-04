def parqueadero_buses(cantidad:int, numero_bus:int)->int:
    lote = numero_bus % 3 # % (porcetaje) residuo modulo permite optener el residuo de una division

#Funcion If nos permite evaluvar varias condiciones definiendo la mejor opcion.
    if lote == 0:
        lote = 3
    return lote

#Input permite la interaccio con el usuario solicitandole informacion para la ejecucion del codigo.

cbuses = int(input('Ingrese la cantidad de buses: ')) #datos que ingersa el usurio
nbus = int(input('Ingrese el numero del bus: ')) #datos que ingersa el usurio

if nbus > cbuses:
    print('Elnumero del bus no puede ser mayor a la cantidad de buses')
#else no permite evaluar otra condicion dentro de la funcion if.
else: 
    print('El bus {} debe parquear en el lote {}'.format(nbus,parqueadero_buses(cbuses, nbus)))
    