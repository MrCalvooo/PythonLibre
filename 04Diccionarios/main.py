registro_personal = {}

def agregar_registro(nombre_emple: str, **detalles):
    if nombre_emple not in registro_personal:
        registro_personal[nombre_emple] = {}
    registro_personal[nombre_emple].update(detalles)

def calcular_puntuacion_final(nombre_empleado):
    if nombre_empleado not in registro_personal:
        print("Empleado no registrado")
        return None
    else: 
        ventas = registro_personal[nombre_empleado].get("ventas", 0) * 0.6
        satisfaccion = registro_personal[nombre_empleado].get("satisfaccion", 0) * 0.4
        print(f"Total de {nombre_empleado}: {ventas + satisfaccion}")

def main():
    agregar_registro("Juan", ventas = 1500, satisfaccion = 500)
    agregar_registro("Maria", ventas = 2000)
    agregar_registro("Luis", satisfaccion = 9)
    
    calcular_puntuacion_final("Juan")
    calcular_puntuacion_final("Maria")
    calcular_puntuacion_final("Luis")

main()