def filtracion():
    filtro = ["OBCION 1 (Filtrar por Categoria)", "OBCION 2 (Filtrar por Prioridad)", "OBCION 3 (Filtrar por Estado)", "OBCION 4 (Mostrar todas las tareas)"]
    for opcion in filtro:
        print(opcion)

    eleccion = int(input("¿Cómo te gustaría filtrar o mostrar las tareas? (1-4): "))

    if eleccion == 1:
        categoria = input("Ingresa la categoría que deseas filtrar: ")
        filtrar_por_categoria(categoria)
    elif eleccion == 2:
        prioridad = input("Ingresa la prioridad (alta, media, baja): ")
        filtrar_por_prioridad(prioridad)
    elif eleccion == 3:
        estado = input("Ingresa el estado (Completo(1), Incompleto(2), En proceso(3)): ")
        filtrar_por_estado(estado)
    elif eleccion == 4:
        mostrar_todas_las_tareas()
    else:
        print("Opción inválida. Intenta de nuevo.")

def leertareas():
    with open("tareas.txt", "r") as archivo:
        lineas = archivo.readlines()
        if lineas:
            print("Lista de Tareas:")
            for linea in lineas:
                print(linea.strip())
        else:
            print("No hay tareas registradas.")

def mostrar_todas_las_tareas():
    print("Mostrando todas las tareas registradas:")
    leertareas()  

def filtrar_por_categoria(categoria):
    with open("tareas.txt", "r") as archivo:
        lineas = archivo.readlines()
        print(f"Tareas en la categoría '{categoria}':")
        mostrar_tareas_filtradas(lineas, "Categoría", categoria)

def filtrar_por_prioridad(prioridad):
    with open("tareas.txt", "r") as archivo:
        lineas = archivo.readlines()
        print(f"Tareas con prioridad '{prioridad}':")
        mostrar_tareas_filtradas(lineas, "Prioridad", prioridad)

def filtrar_por_estado(estado):
    with open("tareas.txt", "r") as archivo:
        lineas = archivo.readlines()
        print(f"Tareas con estado '{estado}':")
        mostrar_tareas_filtradas(lineas, "Estado", estado)


def mostrar_tareas_filtradas(lineas, filtro_tipo, valor_filtro):
    mostrar = False
    for linea in lineas:
        if filtro_tipo in linea and valor_filtro.lower() in linea.lower():
            mostrar = True
        elif "------------------------------" in linea and mostrar:
            print(linea.strip())
            mostrar = False
        if mostrar:
            print(linea.strip())
