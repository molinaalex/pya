# 4. Una tienda necesita programa en Python que permita calcular al total de una venta, el
# porcentaje asociado al IVA (19%).
# Solicitar el monto de la venta al usuario
monto_venta = float(input("Ingrese el monto de la venta: "))
# Calcular el IVA
iva = monto_venta * 0.19
# Calcular el monto total a pagar (monto + IVA)
total_pagar = monto_venta + iva
# Mostrar el IVA y el total a pagar
print("IVA (19%):", round(iva, 2))
print("Total a pagar:", round(total_pagar, 2))