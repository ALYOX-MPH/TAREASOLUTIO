import clasificadorTarea


def creartareas (creartarea):
    with open ("tareas.txt", "w") as crear:
     crear.write(creartarea)

def crear_tarea(tareas):
    titulo = input("Título de la tarea: ")
    descripcion = input("Descripción de la tarea: ")
    fecha_limite = input("Fecha límite (YYYY-MM-DD): ")
    prioridad = input("Prioridad (alta, media, baja): ")
    tarea = clasificadorTarea(titulo, descripcion, fecha_limite, prioridad)
    tareas.append(tarea)
    print("Tarea agregada.")