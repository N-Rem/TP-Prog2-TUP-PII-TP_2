alumnos_registrados = []
profesores_registrados = []
lista_cursos = []

class Usuario():
    def __init__(self, nombre, apellido, email, contrasenia):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasenia = contrasenia
    
    #!get-set--------->
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre=str):
        self.__nombre = nombre
    
    def get_apellido(self):
        return self.__apellido
    def set_apellido(self, apellido=str):
        self.__apellido = apellido
    
    def get_email(self):
        return self.__email
    def set_email(self, email=str):
        self.__email = email    
     #!<-----------------------        
    def __str__(self):
        return f"Nombre = {self.__nombre}, Apellido = {self.__apellido}, E-mail = {self.__email}, Contraseña = {self.__contrasenia}"

    def validar_credenciales(self): #!!!isinstance(variable, tipo de dato): bool 
        if isinstance(self.__email, str) and isinstance(self.__contrasenia, str):
            if not (self.__email.isdigit()) and not (self.__contrasenia.isdigit()): #!!isdigit():bool
                return True
            else:
                return False
        else:
            return False
# !_____________________
class Estudiante(Usuario):
    def __init__(self, nombre=str, apellido=str, email=str, contrasenia=str, legajo=int, anio_inscripcion_carrera=int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.__mis_cursos =[]
    #!get-set ---------------->
    def get_mis_cursos(self):
        return self.__mis_cursos
    def set_mis_cursos(self, curso=object):
        self.__mis_cursos.append(curso)
    #!<----------------------
    def __str__(self):
        return "Estudiante: " + super().__str__() + f", Legajo = {self.__legajo}, Año Inscripcion en la Carrera = {self.__anio_inscripcion_carrera}"

    def Matricular_en_curso(self, curso: object, contrasenia=str):
        if (buscar_curso(curso.get_nombre(), self.__mis_cursos)):
            print(f"Usted ya estaba anotado en {curso.get_nombre()}")
        else:
            if (contrasenia == curso.get_contrasenia()):
                self.__mis_cursos.append(curso)
                print(f"Materia: {curso.get_nombre()} agregada a Mis Cursos..")
            else:
                print("Contraseña no valida..")       
#--
def buscar_curso(curso=str, lista=list):
    for i in lista:
        if curso == i.get_nombre():
            return True
    return False
# !_____________________
class Profesor(Usuario):
    def __init__(self, nombre=str, apellido=str, email=str, contrasenia=str, titulo=str, anio_egreso=int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.__mis_cursos = []

    def get_mis_cursos(self):
        return self.__mis_cursos
    def set_mis_cursos(self, curso=object):
        self.__mis_cursos.append(curso)

    def __str__(self):
        return "Profesor: " + super().__str__() + f", Titulo = {self.__titulo}, Año de Egreso = {self.__anio_egreso}"

    def Dictar_curso(self):
        nombre = input("Ingrese el nombre del curso: ")
        nuevo_curso = Curso(nombre)
        self.__mis_cursos.append(nuevo_curso)
        lista_cursos.append(nuevo_curso)
        print(nuevo_curso)
# !_____________________
class Curso ():
    def __init__(self, nombre=str, archivos=list):
        self.__nombre = nombre
        self.__contrasenia_matriculacion = self.__generar_contrasenia()
        self.__archivos = archivos
    
    #!set, get nombre y archivos
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre=str):
        self.__nombre = nombre
    
    def get_contrasenia (self):
        return self.__contrasenia_matriculacion
        
    def get_archivos(self):
        return self.__archivos
    def set_archivos(self, archivos =str):
        self.__archivos.append(archivos)

    def __str__(self):
        return f"Curso: Nombre = {self.__nombre}, Contraseña de Matriculacion = {self.__contrasenia_matriculacion}"

    def __generar_contrasenia(self):
        contracenia = "000"
        return  contracenia      
# !__________funciones___________
def mostrar_listas(lista = list):
    for i,valor in enumerate(lista):
        print(f"{i+1}. {valor.get_nombre()}\n")
        
def mostrar_mis_cursos(lista_objetos = list, indice = int):
    mis_cursos = lista_objetos[indice].get_mis_cursos()
    mostrar_listas(mis_cursos)
        
def buscar_usuario(lista = list, email = str):
    for indice, valor in enumerate(lista): 
        objeto_lista = valor.get_email()
        if objeto_lista == email:
          return True, indice
    return False, 0
    
def mostrar_cursos(lista = list):
    for i in lista: 
        print(f"Materia: {i.get_nombre()}\t\tCarrera: Tecnicatura Universitaria en Programación\n")

#!---------Objetos-----------
alumno_uno = Estudiante("Lautaro", "Vega", "Lautaro.vega@gmail.com", "2424a", 5858, 2023)
alumno_dos = Estudiante("Maria", "Gomez", "Maria.g@gmail.com", "1234a", 5050, 2022)
alumno_tres = Estudiante("Victoria", "Sosa", "Vicky.ss@gmail.com", "2444a", 3030, 2023)
alumnos_registrados.append(alumno_uno)
alumnos_registrados.append(alumno_dos)
alumnos_registrados.append(alumno_tres)
print(alumno_tres.get_email())

prof_uno = Profesor("Gustavo", "Ramirez","Gustavo.Ramirez@gmail.com", "3883a", "Ingeniero", 2005)
prof_dos = Profesor("Bettiana", "apellidoRaro","bettiana.123@gmail.com", "1010a", "Ingeniera", 2000)
prof_tres = Profesor("Veronica", "Zanches","Veronica.z@gmail.com", "5050b", "Ingeniera", 1999)
profesores_registrados.append(prof_tres)
profesores_registrados.append(prof_dos)
profesores_registrados.append(prof_uno)

curso_uno = Curso("Programacion I")
curso_dos = Curso("Matematicas")
curso_tres = Curso("Estadistica")
lista_cursos.append(curso_uno)
lista_cursos.append(curso_dos)
lista_cursos.append(curso_tres)

prof_uno.set_mis_cursos(curso_uno)
prof_dos.set_mis_cursos(curso_dos)
prof_tres.set_mis_cursos(curso_tres)

alumno_tres.set_mis_cursos(curso_uno)
alumno_tres.set_mis_cursos(curso_dos)
alumno_tres.set_mis_cursos(curso_tres)

print("\n")

mostrar_mis_cursos(alumnos_registrados, 0)
mostrar_mis_cursos(alumnos_registrados,1)
mostrar_mis_cursos(alumnos_registrados,2)

mostrar_mis_cursos(profesores_registrados,2)
