# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Crear un Diccionario llamado 'informacion_personal'

informacion_personal = {
    "nombre": "Sofía Pico",
    "edad": 30,
    "ciudad": "Sucumbíos",
    "profesion": "Estudiante"
}

# Acceder al valor de la clave 'ciudad' y modificarlo
informacion_personal["ciudad"] = "Napo"  # Cambiamos de Sucumbíos a Napo

# Verificar si la clave 'telefono' existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999492948"

# Eliminar la clave 'edad' ya que no es necesaria
del informacion_personal["edad"]

# Imprimir el diccionario final después de todas las operaciones
print("Diccionario final:")
print(informacion_personal)

# Ejemplo de Escritura en un archivo usando el diccionario
file_name = "informacion_personal.txt"

# Modo de apertura "w" para escritura
with open(file_name, "w") as archivo:
    archivo.write("Información Personal:\n")
    for clave, valor in informacion_personal.items():
        archivo.write(f"{clave}: {valor}\n")

# Lectura del archivo para verificar el contenido
with open(file_name, "r") as archivo:
    contenido = archivo.read()
    print("\nContenido del archivo:")
    print(contenido)

# Ejemplo adicional de Escritura en un archivo usando líneas predefinidas
otro_file_name = "ejemplo_escritura.txt"
with open(otro_file_name, "w") as archivo_escritura:
    # Escribimos varias líneas de texto
    archivo_escritura.write("Línea 1: Esto es una prueba.\n")
    archivo_escritura.write("Línea 2: Escribiendo en archivos con Python.\n")
    lineas = ["Línea 3: Otro ejemplo.\n", "Línea 4: Finalizando el ejemplo.\n"]
    archivo_escritura.writelines(lineas)

# Lectura del archivo recién escrito
with open(otro_file_name, "r") as archivo_lectura:
    contenido_archivo = archivo_lectura.read()
    print("\nContenido del archivo ejemplo_escritura.txt:")
    print(contenido_archivo)
