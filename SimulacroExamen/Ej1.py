dinero = 60
balon = int(input("Ingrese el coste del balon: "))
descuento = int(input("Ingrese el descuento del balon en porcentaje: "))
if descuento > 1:
    descuento = descuento / 100
balon = balon - (balon * descuento)
dinero -= balon
print(f"El coste total es {balon} y te quedan {dinero} euros")