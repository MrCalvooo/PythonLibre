num1 = 0
num2 = 0
cadena = ""
salir = True

while (salir):
    try:
        cadena = input("Desea salir? (SALIR): ")
        if cadena == "SALIR":
            break
        
        num1 = float(input("Numerador: "))
        num2 = float(input("Denominador: "))
        
        if num2 == 0:
            raise ZeroDivisionError
    except ValueError:
        print("Error, numero no valido")
        continue
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        continue
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
    
print("ADIOS :)")