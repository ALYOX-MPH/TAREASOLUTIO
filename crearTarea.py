def crear_tarea():
    titulo = input("Título de la tarea: ")
    descripcion = input("Descripción de la tarea: ")
    fecha_limite = input("Fecha límite (YYYY-MM-DD): ")
    prioridad = input("Prioridad (alta, media, baja): ")
    categoria = input("Defina una categoria para la tarea: ")
    estado = input("Estado (Completo(1), Incompleto(2), En proceso(3)): ")
    tarea = (titulo, descripcion, fecha_limite, prioridad,categoria,estado)

    print("Tarea agregada.")
    
    almacenado(tarea)

def almacenado(tarea):
    tarea_escrita = f"Título: {tarea[0]}\nDescripción: {tarea[1]}\nFecha Límite: {tarea[2]}\nPrioridad: {tarea[3]}\nCategoria: {tarea[4]}\nEstado: {tarea[5]}\n------------------------------\n"

    with open("tareas.txt", "a") as crear:
        crear.write(tarea_escrita)
    








