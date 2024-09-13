def actualizar_tarea():
    titulo_a_editar = input("Ingresa el título de la tarea que deseas editar: ")

    with open("tareas.txt", "r") as archivo:
        lineas = archivo.readlines()

    tarea_nueva = []
    tarea_encontrada = False

    for linea in lineas:
        if titulo_a_editar in linea:
            tarea_encontrada = True
            print("Tarea encontrada. Ingresa los nuevos valores.")
            nuevo_titulo = input("Nuevo título: ")
            nueva_descripcion = input("Nueva descripción: ")
            nueva_fecha = input("Nueva fecha límite (YYYY-MM-DD): ")
            nueva_prioridad = input("Nueva prioridad (alta, media, baja): ")

            tarea_nueva.append(f"Título: {nuevo_titulo}\n")
            tarea_nueva.append(f"Descripción: {nueva_descripcion}\n")
            tarea_nueva.append(f"Fecha Límite: {nueva_fecha}\n")
            tarea_nueva.append(f"Prioridad: {nueva_prioridad}\n")
        else:
            tarea_nueva.append(linea)

    if tarea_encontrada:
        with open("tareas.txt", "w") as archivo:
            archivo.writelines(tarea_nueva)
        print("Tarea actualizada.")
    else:
        print(f"No se encontró ninguna tarea con el título '{titulo_a_editar}'.")