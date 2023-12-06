import csv

def ingresar_datos():
    # Solicitar al usuario que ingrese los datos
    nombre = input("Ingrese el nombre del jugador: ")
    estado_partida = input("Ingrese el estado de la partida: ")
    dificultad = input("Ingrese la dificultad: ")
    porcentaje = float(input("Ingrese el porcentaje completado: "))
    tiempo = float(input("Ingrese el tiempo jugado: "))
    puntaje = int(input("Ingrese el puntaje: "))

    # Retornar los datos ingresados como una lista
    return [nombre, estado_partida, dificultad, porcentaje, tiempo, puntaje]

def escribir_csv(datos, ruta_archivo):
    # Verificar si el archivo CSV ya existe
    existe_archivo = True
    try:
        with open(ruta_archivo, 'r') as archivo_existente:
            pass
    except FileNotFoundError:
        existe_archivo = False

    # Escribir datos en el archivo CSV
    with open(ruta_archivo, mode='a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)

        # Si el archivo no existe, escribir encabezados
        if not existe_archivo:
            encabezados = ["Nombre", "Estado Partida", "Dificultad", "Porcentaje", "Tiempo", "Puntaje"]
            escritor_csv.writerow(encabezados)

        # Escribir los datos proporcionados
        escritor_csv.writerow(datos)

    print(f"Los datos se han añadido correctamente al archivo {ruta_archivo}")

def leer_csv(ruta_archivo,k):
    datos = []

    with open(ruta_archivo, 'r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)

        # Saltar la primera línea (encabezados)
        next(lector_csv, None)

        # Leer las líneas restantes
        for linea in lector_csv:
            datos.append(linea)
        # Ordenar los datos por puntaje (última columna)
        datos_ordenados = sorted(datos, key=lambda x: int(x[-1]), reverse=True)

        # Devolver el top K de filas
    return datos_ordenados[:k]
        


if __name__ == "__main__":
    
    eleccion=int(input("Seleccion opcion 1 (escribir en csv) o 2 (leer en csv): "))
    # Ruta del archivo CSV
    ruta_archivo_csv = "DB\DB.csv"

    if eleccion==1:
        # Solicitar al usuario que ingrese los datos
        datos_ingresados = ingresar_datos()
        # Escribir los datos en el archivo CSV
        escribir_csv(datos_ingresados, ruta_archivo_csv)
    else:
        # Llamar a la función para leer los datos
        datos_leidos = leer_csv(ruta_archivo_csv,3)

        # Mostrar los datos leídos
        print("Datos leídos del archivo CSV:")
        for fila in datos_leidos:
            print(fila)
    
