nombres_productos = ["Monitor", "Teclado", "Ratón", "Webcam", "Disco Duro"]
precios = [250.50, 45.99, 12.00, 60.75, 150.99]
stock = [10, 20, 35, 15, 5]

def valor_total() -> float:
    valor_inventario = 0
    for precio, cantidad in zip(precios, stock):
        valor_inventario += precio * cantidad
    return valor_inventario

def productos_criticos():
    productos_reposicion_normal = []
    for cantidad, prod in zip(stock, nombres_productos):
        if cantidad <= 5:
            productos_reposicion_normal.append(prod)
    return productos_reposicion_normal

def comprension_listas():
    # Usamos comprensión de listas para crear la lista de productos con stock <= 5
    productos_reposicion_compacta = [prod for prod, cantidad in zip(nombres_productos, stock) if cantidad <= 5]
    return productos_reposicion_compacta

def main():
    print(f"Valor total del inventario actual: {valor_total()}")
    print(f"Productos con stock menor o igual a 5 (función normal): {productos_criticos()}")
    print(f"Productos con stock menor o igual a 5 (comprensión de listas): {comprension_listas()}")

main()
