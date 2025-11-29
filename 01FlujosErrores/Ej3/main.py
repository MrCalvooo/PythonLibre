lecturas_sensor = [25.5, "28.0", 35, "Invalido", 100.1, 15.2, "tres", 42.0]
temperaturas_validas = []

def procesar_lectura(valor_bruto):
    try:
        # Intentar convertir el valor a float
        valor_numerico = float(valor_bruto)
    except ValueError:
        print(f"Error de formato: El valor '{valor_bruto}' no es numérico")
        return None  # Devuelve None si el valor no es numérico
    else:
        # Verificar si el valor está en el rango válido
        if 0.0 < valor_numerico < 50.0:
            return valor_numerico
        else:
            raise ValueError(f"Temperatura fuera del rango normal (0.0°C a 50.0°C): {valor_numerico}")

for i in lecturas_sensor:
    try:
        valor = procesar_lectura(i)
    except ValueError:
        pass
    else:
        if valor is not None:
            temperaturas_validas.append(valor)

print(f"Temperaturas validadas: {temperaturas_validas}")