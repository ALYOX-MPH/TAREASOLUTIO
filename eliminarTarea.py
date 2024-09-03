def eliminartareas ():
    with open ("tareas.txt", "r") as leer:
     leerlinea = leer.read()
     eliminar = leerlinea.remove()
     print(eliminar)