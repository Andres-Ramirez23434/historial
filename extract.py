import os

def analizar_archivo(ruta):
    # Obtener información básica del archivo
    info_archivo = {
        'Ruta': ruta,
        'Tamaño (en bytes)': os.path.getsize(ruta),
        'Es directorio': os.path.isdir(ruta),
        'Es archivo': os.path.isfile(ruta),
        'Es enlace simbólico': os.path.islink(ruta),
    }

    # Si es un archivo de texto, leer las primeras líneas
    if os.path.isfile(ruta) and ruta.lower().endswith(('.txt', '.csv', '.log')):
        try:
            with open(ruta, 'r', encoding='utf-8') as archivo:
                lineas = [next(archivo) for _ in range(5)]  # Lee las primeras 5 líneas
            info_archivo['Contenido (primeras líneas)'] = lineas
        except Exception as e:
            info_archivo['Error al leer contenido'] = str(e)

    return info_archivo

if __name__ == "__main__":
    ruta_archivo = input("Ingrese la ruta del archivo a analizar: ")

    if os.path.exists(ruta_archivo):
        resultado = analizar_archivo(ruta_archivo)
        for clave, valor in resultado.items():
            print(f"{clave}: {valor}")
    else:
        print("La ruta especificada no existe.")
