from xmlrpc.client import MAXINT

numeros = []
def mayor_num() -> float:
    mayor = 0
    for num in numeros:
        if num > mayor:
            mayor = num
    return mayor

def menor_num() -> float:
    menor = MAXINT
    for num in numeros:
        if num < menor:
            menor = num
    return menor

def media() -> float:
    media = 0
    for num in numeros:
        media += num
    return media / len(numeros)

while True:
    palabra = input("Ingresa números (FIN para salir): ")
    if palabra.upper() == "FIN":
        break
    try:
        numero = float(palabra)
        numeros.append(numero)
    except ValueError:
        print("Por favor ingresa un número válido.")

for num in numeros:
    print(f"Numero: {num}")

print(f"Numero mayor: {mayor_num()}")
print(f"Numero menor: {menor_num()}")
print(f"Media de numeros: {media()}")