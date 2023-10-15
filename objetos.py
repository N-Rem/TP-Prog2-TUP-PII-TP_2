alumnos_registrados = []
profesores_registrados = []
lista_cursos = []


class Usuario():
    def __init__(self, nombre, apellido, email, contrasenia):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasenia = contrasenia

    def __str__(self):
        return f"Nombre = {self.__nombre}, Apellido = {self.__apellido}, E-mail = {self.__email}, Contraseña = {self.__contrasenia}"

    def validar_credenciales(self):
        if isinstance(self.__email, str) and isinstance(self.__contrasenia, str):
            if not (self.__email.isdigit()) and not (self.__contrasenia.isdigit()):
                return True
            else:
                return False
        else:
            return False
# !_____________________


class Estudiante(Usuario):
    def __init__(self, nombre=str, apellido=str, email=str, contrasenia=str, legajo=int, anio_inscripcion_carrera=int, mis_cursos=[]):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.mis_cursos = mis_cursos

    def __str__(self):
        return "Estudiante: " + super().__str__() + f", Legajo = {self.__legajo}, Año Inscripcion en la Carrera = {self.__anio_inscripcion_carrera}"

    def Matricular_en_curso(self, curso: object, contrasenia=str, ):
        if not (busca_curso(self.__mis_cursos, curso.__nombre)):
            if (contrasenia == curso.__contrasenia_matriculacion):
                self.__mis_cursos.append(curso)
                print(f"Usted de Matriculo en {curso.__nombre}")
            else:
                print("Contraseña no valida..")
        else:
            print(f"Usted ya esta anotado en {curso.__nombre}")


def busca_curso(lista=list, nombre=str):
    for i in lista:
        if i.__nombre == nombre:
            return True
        else:
            return False

# !_____________________

class Profesor(Usuario):
    def __init__(self, nombre=str, apellido=str, email=str, contrasenia=str, titulo=str, anio_egreso=int, mis_cursos=[]):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.mis_cursos = mis_cursos

    def __str__(self):
        return "Profesor: " + super().__str__() + f", Titulo = {self.__titulo}, Año de Egreso = {self.__anio_egreso}"

    def Dictar_curso(self):
        nombre = input("Ingrese el nombre del curso: ")
        nuevo_curso = Curso(nombre)
        self.__mis_cursos.append(nuevo_curso)
        lista_cursos.append(nuevo_curso)
        print(nuevo_curso)
    
    def Mostrar_mis_cursos(self):
        return mostrar_listas(self.__mis_cursos)

# !_____________________

class Curso (Estudiante, Profesor):
    def __init__(self, nombre=str, contrasenia_matriculacion = None, archivos=list):
        self.__nombre = nombre
        self.__contrasenia_matriculacion = self.__generar_contrasenia()
        self.__archivos = archivos

    def __str__(self):
        return f"Curso: Nombre = {self.__nombre}\nContraseña de Matriculacion = {self.__contrasenia_matriculacion}"

    def __generar_contrasenia(self):
        self.__contrasenia_matriculacion = "0"
        
# !__________funciones___________

def mostrar_listas(lista = list):
    for i in lista:
        print(i + "\n")


def buscar_usuario(lista = list, email = str):
    for valor, indice in lista: 
        if valor.__email == email:
          return True, indice
        else: return False
    
def mostrar_cursos(lista = list):
    for i in lista: 
        print(f"Materia: {i.__nombre}\t\tCarrera: Tecnicatura Universitaria en Programación\n")

def agregar_a_lista(lista_de, ob):
    lista_de.append(ob)


#!---------Objetos-----------
usuario_uno = Usuario("Azul", "Vega", "Azul.vega@gmail.com", "20424")
print(usuario_uno)
print("\n")

alumno_uno = Estudiante("Lautaro", "Vega", "Lautaro.vega@gmail.com", "2424a", 5858, 2023)

prof_uno = Profesor("Gustavo", "Ramirez","Gustavo.Ramirez@gmail.com", "3883a", "Ingeniero", 2000)
print(prof_uno)
print("\n")

curso_uno = Curso("matematicas")

print(curso_uno)

print(usuario_uno, "\n ", usuario_uno.validar_credenciales())
prof_uno.dictar_curso()
