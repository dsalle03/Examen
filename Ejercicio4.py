class alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        return "El alumno se llama {}, y su nota es {}.".format(self.nombre, self.nota)


david = alumno("David Sallé", 10)
print(david)
daniel = alumno("Daniel López", 2.99)
print(daniel)
mia = alumno("Mia Colina", 8)
print(mia)
eva = alumno("Eva García", 8)
print(eva)


