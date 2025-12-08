nombres_equipos = ["Rayo Vallecano", "Atletico de Madrid", "Betis", "Real Madrid", "Barsa", "Real Valladolid",
                  "Real Sociedad"]
puntos = []
partidos_ganados = [4, 3, 2, 1, 3, 1, 2]
partidos_empatados = [1, 2, 3, 2, 2, 4, 2]
partidos_perdidos = [1, 1, 1, 3, 1, 1, 2]

def puntos_total():
    for nombre, ganado, empatadado, perdido in zip(nombres_equipos, partidos_ganados, partidos_empatados, partidos_perdidos):
        points = (ganado * 3) + (empatadado * 2)
        print(f"Puntos del {nombre}: {points}")
        puntos.append(points)

def clasificacion():
    clasi = []
    for nombre, point in zip(nombres_equipos, puntos):
        clasi.append((point, nombre))
    clasi.sort(reverse=True)
    posicion = 1
    for point, nombre in clasi:
        print(f"{posicion}: {nombre}: {point}")
        posicion += 1

puntos_total()
clasificacion()