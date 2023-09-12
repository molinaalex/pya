# 3. Ingresar nombre de un estudiante y 4 calificaciones (con decimal) de la asignatura de Arte.
# Solicitar el nombre y las calificaciones al usuario
nombre = input("Ingrese el nombre del estudiante: ")
calif1 = float(input("Ingrese la primera calificación: "))
calif2 = float(input("Ingrese la segunda calificación: "))
calif3 = float(input("Ingrese la tercera calificación: "))
calif4 = float(input("Ingrese la cuarta calificación: "))
# Calcular los porcentajes de cada calificación
porcentaje1 = calif1 * 0.15
porcentaje2 = calif2 * 0.25
porcentaje3 = calif3 * 0.30
porcentaje4 = calif4 * 0.30
# Calcular el promedio basado en los porcentajes
promedio = porcentaje1 + porcentaje2 + porcentaje3 + porcentaje4
# Mostrar el nombre, los porcentajes y el promedio final
print("Nombre:", nombre)
print("Porcentaje de la primera calificación:", round(porcentaje1, 1))
print("Porcentaje de la segunda calificación:", round(porcentaje2, 1))
print("Porcentaje de la tercera calificación:", round(porcentaje3, 1))
print("Porcentaje de la cuarta calificación:", round(porcentaje4, 1))
print("Promedio final:", round(promedio, 1))