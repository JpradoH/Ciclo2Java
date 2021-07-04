def tiempo_caida_libre(altura:int, masa:int)->str:
    a = altura
    gravedad = 9.807
    operacion1= 2*a/gravedad
    operacion2= operacion1 **(1/2)
    tiempo = round(operacion2, 2)
    mensaje = 'El tiempo que tarda un balón de ' + str(int(masa))+'kg en caída libre desde una altura de ' +str(int(altura))+'m en impactar en el suelo es de: '+ str(float(tiempo))+'seg'
    return mensaje

print(tiempo_caida_libre(10, 85))
print(tiempo_caida_libre(15, 20))
print(tiempo_caida_libre(8, 50))
print(tiempo_caida_libre(12, 8))