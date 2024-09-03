
class Tarea:
    def __init__(self, titulo, descripcion, fecha_limite, prioridad):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.prioridad = prioridad
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "✔️" if self.completada else "❌"
        return f"{self.titulo} - {self.descripcion} - {self.fecha_limite} - {self.prioridad} - {estado}"