alumnos_registrados = []
profesores_registrados = []
cusos = []


class Usuario():
    def __init__(self, nombre, apellido, email, contrasenia):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasenia = contrasenia

    def __str__(self):
        return f"Nombre = {self.__nombre}, Apellido = {self.__apellido}, E-mail = {self.__email}, Contraseña = {self.__contrasenia}"

    def validar_credenciales(mail, passw):
        if (mail != str or passw != str):
            return False
        else:
            return True
# !_____________________


class Estudiante(Usuario):
    def __init__(self, nombre=str, apellido=str, email=str, contrasenia=str, legajo=int, anio_inscripcion_carrera=int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera

    def __str__(self):
        return "Estudiante: " + super().__str__() + f", Legajo = {self.__legajo}, Año Inscripcion en la Carrera = {self.__anio_inscripcion_carrera}"

    def matricular_en_curso(curso):
        pass


# !_____________________


class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, titulo, anio_egreso):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso

    def __str__(self):
        return "Profesor: " + super().__str__() + f", Titulo = {self.__titulo}, Año de Egreso = {self.__anio_egreso}"

    def dictar_curso(curos):
        pass


# !_____________________


class Curso (Estudiante, Profesor):
    def __init__(self, nombre, contrasenia_matriculacion):
        self.__nombre = nombre
        self.__contrasenia_matriculacion = contrasenia_matriculacion

    def __str__(self):
        return f"Curso: Nombre = {self.__nombre}, Contraseña de Matriculacion = {self.__contrasenia_matriculacion}"

    def __generar_contrasenia__():
        passw = 0
        return passw

# !__________funciones___________


def Buscar_alumno():
    return str
    pass


def Buscar_existencia():
    return boolean


def agregar_a_lista(lista_de, ob):
    lista_de.append(ob)


#!---------Objetos-----------
usuario_uno = Usuario("Azul", "Vega", "Azul.vega@gmail.com", "2424a")
print(usuario_uno)
print("\n")

alumno_uno = Estudiante(
    "Lautaro", "Vega", "Lautaro.vega@gmail.com", "2424a", 5858, 2023)
print(alumno_uno)
print("\n")

prof_uno = Profesor("Gustavo","Ramirez","Gustavo.Ramirez@gmail.com", "3883a","Ingeniero", 2000)
print(prof_uno)
print("\n")

curso_uno = Curso("matematicas", "asdf4")
print(curso_uno)
