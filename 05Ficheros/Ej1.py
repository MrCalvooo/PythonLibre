"""
Mi Primer Gestor de Notas Persistente
Objetivo: Crear un script de Python que permita crear un archivo de texto, añadir información de forma segura y leer su contenido completo.
Instrucciones del Ejercicio:
1. Creación y Escritura Inicial:
    ◦ Crea un script llamado notas.py.
    ◦ Utilizando la estructura recomendada with open() as f: (que garantiza el cierre automático del archivo), abre un archivo llamado mis_notas.txt en modo escritura ('w').
    ◦ Escribe una línea inicial que diga: "--- Registro de Notas Personales ---".
    ◦ Nota importante: Recuerda que el método write() no añade automáticamente saltos de línea, por lo que deberás incluir el carácter \n al final de la cadena.
2. Adición de Contenido (Modo Añadir):
    ◦ Solicita al usuario por consola que introduzca una nota o pensamiento (usa input()).
    ◦ Abre de nuevo el archivo mis_notas.txt, pero esta vez en modo añadir ('a') para evitar que se sobrescriba el contenido previo.
    ◦ Escribe la nota del usuario en una nueva línea dentro del archivo.
3. Lectura Robusta del Archivo:
    ◦ Implementa una estructura try-except para manejar posibles errores, como el FileNotFoundError (en caso de que intentes leer el archivo y este no exista por algún motivo).
    ◦ Dentro del bloque try, abre el archivo en modo lectura ('r').
    ◦ Usa el método read() para obtener todo el contenido del archivo como una única cadena y muéstralo por pantalla.
    ◦ Si ocurre el error de "archivo no encontrado", muestra un mensaje amigable al usuario
"""

def escribir_inicio():
    with open("notas.txt", "w") as f:
        f.write("--- Registro de Notas Personales ---\n")

def leer_fichero():
    try:
        with open("notas.txt", "r") as f:
            for linea in f:
                print(linea)
    except FileNotFoundError:
        print("El archivo no existe")

escribir_inicio()
with open("notas.txt", "a") as f:
    contenido = input("Contenido a escribir en el fichero: ")
    f.write(contenido + "\n")
leer_fichero()