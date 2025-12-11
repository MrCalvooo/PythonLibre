inventario = {}
def agregar_producto(id_producto, stock_inicial):
    try:
        id_prod = int(id_producto)
        stock = int(stock_inicial)
    except ValueError:
        print("Error: ID o stock deben ser números enteros.")
        return
    inventario[id_prod] = stock

def consultar_stock(id_producto):
    prod = inventario.get(id_producto)
    if prod is None:
        print("No existe un producto con dicho ID registrado")
    else:
        print(prod)

agregar_producto("101", "50")
agregar_producto(202, 10)
agregar_producto("trescientos", 5)
print(inventario)

consultar_stock(101)
consultar_stock(999)
consultar_stock("doscientos")