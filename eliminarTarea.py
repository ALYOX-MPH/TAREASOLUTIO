def eliminar_tarea():
    titulo_a_eliminar = input("Ingresa el título de la tarea que deseas eliminar: ")

    with open("tareas.txt", "r") as archivo:
        lineas = archivo.readlines()

    with open("tareas.txt", "w") as archivo:
        saltar = False
        for linea in lineas:
            if linea.startswith("Título:") and titulo_a_eliminar.lower() in linea.lower():
                saltar = True 
            elif linea.startswith("------------------------------"):
                if saltar:
                    saltar = False  # Ya dejo de saltarrrrr por fin 
                else:
                    archivo.write(linea)
            elif not saltar:
                archivo.write(linea)

    print(f"Tarea con título '{titulo_a_eliminar}' eliminada (si existía).")