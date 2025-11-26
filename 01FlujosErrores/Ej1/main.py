transacciones_brutas = ('Error', '34.50', 120, '40', 800, 'invalido', 450, 1500, '35.9')
suma_transacciones_validas = 0
meta_critica = 500

for i in transacciones_brutas:
    try:
        transaccion = float(i)
        
        if transaccion >= meta_critica:
            print("ALERTA: TRANSACCION CRITICA DETECTADA")
            break
        else:
            suma_transacciones_validas += transaccion
    except ValueError:
        print("Dato no numerico encontrado")
        continue

print(f"Transacciones completadas correctamente: {suma_transacciones_validas}")