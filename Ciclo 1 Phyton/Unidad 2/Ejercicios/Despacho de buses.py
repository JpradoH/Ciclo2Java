def despacho_buses(personas_bus: int, personas_estacion: int)->bool:
    """ La estación de Megabus
    Parámetros:
      personas_bus (int): Número de personas en el bus que va a detenerse
      personas_estacion (int): Número de personas esperando el bus en la estación
    Retorno:
      bool: Retorna el valor True si se debe despachar un bus nuevo y retorna False de lo contrario.
    """
    total_personas = personas_bus + personas_estacion
    if total_personas > 200:
        return True
    else:
        return False

print(despacho_buses(50,200))
print(despacho_buses(170,10))
print(despacho_buses(50,10))
print(despacho_buses(50,50))