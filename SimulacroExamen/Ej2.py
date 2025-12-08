nombres = ["Ana", "Luis", "Carlos", "Marta", "Eva"]
edades = [17, 22, 19, 15, 28]
mayores = 0
media = 0
mayor_edad = 0
mayor_nombre = ""
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
    if edad > 17:
        mayores += 1
    if edad > mayor_edad:
        mayor_edad = edad
        mayor_nombre = nombre
    media += edad
media /= len(nombres)
print("*****************RESUMEN*****************")
print(f"Personas mayores de edad: {mayores}")
print(f"La persona con mas edad es: {mayor_nombre} con {mayor_edad} años")
print(f"Media de edad: {media}")