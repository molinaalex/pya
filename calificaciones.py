# 2. Ingresar 3 calificaciones (con decimales) para la asignatura de Ciencias de un estudiante,
# Solicitar las tres calificaciones al usuario
calif1 = float(input("Ingrese la primera calificación: "))
calif2 = float(input("Ingrese la segunda calificación: "))
calif3 = float(input("Ingrese la tercera calificación: "))
# Calcular el promedio
promedio = (calif1 + calif2 + calif3) / 3
# Mostrar el promedio
print("El promedio de las calificaciones es:", round(promedio, 1))
