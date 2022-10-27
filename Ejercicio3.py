class alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota



david = alumno("David Sallé", 10)
daniel = alumno("Daniel López", 2.99)
mia = alumno("Mia Colina", 8)
eva = alumno("Eva García", 8)
clase = [david, daniel, mia, eva]

def constructor(clase):
    lista_clase = []
    for i in clase:
        lista_clase.append(i)
        print("El alumno", i.nombre, "ha sido creado con existo")
    return lista_clase

constructor(clase)

def calificacion(clase):
    print("Los alumnos aprobados son:")
    for i in clase:
        if i.nota >= 5:
            print(i.nombre)

    print("Los alumnos suspensos son:")
    for i in clase:
        if i.nota < 5:
            print(i.nombre)


calificacion(clase)