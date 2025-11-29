nombre_proyecto = "Lanzamiento App Móvil"
lista_tareas = ["Diseño UX", "Integración API", "Test de Seguridad", "Marketing", "Despliegue Final"]
presupuesto_base = 15000

def asignar_riesgo(tareas_a_analizar):
    for i in range(len(tareas_a_analizar)):
        if "Seguridad" in tareas_a_analizar[i]:
            tareas_a_analizar[i] += " Riesgo CRITICO"
            
def calcular_gasto_adicional(base, riesgo: float) -> float:
    if riesgo > 1:
        riesgo = riesgo / 100
    if riesgo > 0.2:
        base += base * 0.1
    return base

def main():
    asignar_riesgo(lista_tareas)
    print(f"Listado de tareas: {lista_tareas}")
    presupuesto_final = calcular_gasto_adicional(presupuesto_base, 30)
    print(f"Presupuesto final: {presupuesto_final}")

main()