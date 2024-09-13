import leerTareas
import crearTarea
import eliminarTarea
import actualizarTarea

print ("--------TAREASOLUTION--------")

print ("Selecione la obcion que quiere realizar.")
menu_principal = ["OBCION 1 (Crear Tareas)","OBCION 2 (Veer tareas)","OBCION 3 (Actualizar Tareas)","OBCION 4 (Eliminar Tareas)"]

for menu_principall in menu_principal:
    print(menu_principall)

decicion = int(input("Que decea realizar ? "))

if decicion == 1:
  crearTarea.crear_tarea()
elif decicion == 2:
    leerTareas.filtracion()
elif decicion == 3:
    actualizarTarea.actualizar_tarea()
elif decicion == 4:
     eliminarTarea.eliminar_tarea()
else:
    print("El valor es invalido, con las obciones sugeridas")