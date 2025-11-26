precio_unidad = 14.99
cantidad = 25
cliente_vip = False
codigo_promo = "VERANO2024"

subtotal = precio_unidad * cantidad

aplica_descuento = ( (cantidad >= 20 and codigo_promo == "VERANO2024") or cliente_vip ) and (subtotal > 300)

if aplica_descuento:
    subtotal -= subtotal * 0.15
    
iva = subtotal * 0.21

total = subtotal + iva

print(f"En total son {total} euros")