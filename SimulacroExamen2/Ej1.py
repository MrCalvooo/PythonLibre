nombres = ["Ana", "Beto", "Carlos", "Diana", "Elena", "Felipe"]
notas = [7.5, 4.0, 9.5, 6.0, 3.5, 8.0]
alumnos_aprobados = []

for nombre, nota in zip(nombres, notas):
    if nota >= 7.0:
        nota += 0.5

    if nota >= 5.0:
        alumnos_aprobados.append(nombre)

print(f"Alumnos aprobados: {alumnos_aprobados}")