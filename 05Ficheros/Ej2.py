"""
El Puntero Viajero
Vamos a poner esto en práctica con un script que manipule la posición del puntero.
Objetivo: Crear un archivo con varias líneas, leerlo hasta el final, y luego usar seek para volver a leer solo una parte específica sin cerrar y reabrir el archivo.
Pasos a seguir:
1. Preparación: Crea un archivo llamado practica_puntero.txt en modo escritura ('w') y escribe las siguientes tres líneas (no olvides los \n):
    ◦ Línea 1: Python es genial
    ◦ Línea 2: Aprendiendo a usar seek
    ◦ Línea 3: Fin del ejercicio
2. Lectura Completa: Abre el archivo en modo lectura y escritura ('r+'). Usa f.read() para leer todo el contenido e imprímelo.
3. Comprobación: Usa print(f.tell()) para ver en qué byte se ha quedado el puntero tras la lectura (debería estar al final del archivo).
4. Retroceso al Inicio: Usa f.seek(0) para volver al principio del archivo.
5. Lectura Parcial:
    ◦ Mueve el puntero exactamente al inicio de la segunda línea (tendrás que contar o calcular los bytes, o simplemente probar con un número como f.seek(25)).
    ◦ Lee el resto del archivo desde esa posición con f.read() e imprímelo.
6. Desplazamiento desde el final: Usa f.seek(0, 2) para situarte al final del archivo y añade una cuarta línea con f.write()
"""

with open("practica_puntero.txt", "w") as f:
    f.write("Python es genial\n")
    f.write("Aprendiendo a usar seek\n")
    f.write("Fin del ejercicio\n")

with open("practica_puntero.txt", "r+") as f:
    print(f.read())
    print(f.tell())
    f.seek(0)
    # Segunda linea, cada carácter = 1 byte
    f.seek(17)
    print(f.read())

with open("practica_puntero.txt", "a") as f:
    f.seek(0, 2)
    f.write("Linea 4")