def desperdicio_de_gaseosa(amigo_1:dict, amigo_2:dict, amigo_3:dict, capacidad_boton:float)->str:
   capacidad_disp_a1 = amigo_1['capacidad_vaso'] - amigo_1['capacidad_actual']
   capacidad_disp_a2 = amigo_2['capacidad_vaso'] - amigo_2['capacidad_actual']
   capacidad_disp_a3 = amigo_3['capacidad_vaso'] - amigo_3['capacidad_actual']
   if capacidad_boton > capacidad_disp_a1:
       return amigo_1['nombre']
   elif capacidad_boton > capacidad_disp_a2:
       return amigo_2['nombre']
   elif capacidad_boton > capacidad_disp_a3:
       return amigo_3['nombre']
   else:
       return 'nadie'
a1 = {
    'nombre': 'Maria',
    'capacidad_vaso': 150.0,
    'capacidad_actual': 50.0,
}

a2 = {
    'nombre': 'Anamaria',
    'capacidad_vaso': 250.0,
    'capacidad_actual': 200.0,
}

a3 = {
    'nombre': 'Jorge',
    'capacidad_vaso': 200.0,
    'capacidad_actual': 160.0,
}

cantidad = float(input('Ingrese la cantidad de gaseosa: '))
print('A {} se le riega la gaseosa'.format(desperdicio_de_gaseosa(a1, a2, a3, cantidad)))
