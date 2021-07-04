def compra_producto(valor_producto:int, nro_cuotas:int)->dict:
    valor_compra = {}
    if nro_cuotas >= 1 and nro_cuotas <= 18:
        cuota1 = valor_producto * 15 / 100
        deuda1 = valor_producto - cuota1
        valor_cuota = 0.0
        if nro_cuotas <= 6:
            valor_cuota = (deuda1 * 1.10) / nro_cuotas
        elif nro_cuotas <= 12:
            valor_cuota = (deuda1 * 1.12) / nro_cuotas
        else:
            valor_cuota = (deuda1 * 1.15) / nro_cuotas                    
        pago_total = cuota1 + (valor_cuota * nro_cuotas)
        valor_compra = {'valor_producto':int(valor_producto),'cuota_inicial':int(cuota1),'nro_cuotas':int(nro_cuotas),'valor_cuota':int(valor_cuota),'valor_final_producto': int(pago_total)}
    return valor_compra

print(compra_producto(1200000, 7))
print(compra_producto(8500000, 20))
print(compra_producto(6390000, 14))
'''print(compra_producto(2000000, 17))
print(compra_producto(1350000, 0))'''