segundos = 9545
SEGUNDOS_POR_MINUTO = 60
SEGUNDOS_POR_HORA = 3600

horas_enteras = segundos // SEGUNDOS_POR_HORA
segundos_restantes_despues_de_horas = segundos % SEGUNDOS_POR_HORA
print(f"Numero de horas que tienen {segundos}: {horas_enteras} y restan {segundos_restantes_despues_de_horas}")

minutos_enteros = segundos_restantes_despues_de_horas // SEGUNDOS_POR_MINUTO
segundos_finales = segundos_restantes_despues_de_horas / SEGUNDOS_POR_MINUTO
print(f"{minutos_enteros} y {segundos_finales}")

duracion_decimal = float(horas_enteras)
print(f"Total: {duracion_decimal}")