import random
alumnos_registrados = []
profesores_registrados = []
lista_cursos = []

class Usuario(): #!!!---Super clase
    def __init__(self, nombre=str, apellido=str, email=str, contrasenia=str): #!--- se ponde =str para remarcar que el valor del atributo tiene que ser en este caso String
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasenia = contrasenia
    
    #!get-set---------> Get solo devuleve el valor del atributo, y set solo cambia el valor del atributo.
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

    def get__contrasenia(self):
        return self.__contrasenia
    def set__contrasenia(self, contrasenia=str):
        self.__contrasenia = contrasenia  
     #!<-----------------------        
    def __str__(self): #!!!---cuando se imprime el objeto aparece sin nada se imprime esta cadena
        return f"Nombre = {self.__nombre}, Apellido = {self.__apellido}, E-mail = {self.__email}, Contraseña = {self.__contrasenia}"

    def validar_credenciales(self, email: str, contrasena: str):
        if email == self.get_email() and contrasena == self.get__contrasenia():
            return True
        else:
            return False     

# !_____________________
class Estudiante(Usuario):
    def __init__(self, nombre=str, apellido=str, email=str, contrasenia=str, legajo=int, anio_inscripcion_carrera=int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.__mis_cursos =[] #!!!---no se pone como argumento, porque se agregan con set_mis_cursos()
    #!get-set ---------------->
    def get_mis_cursos(self):
        return self.__mis_cursos
    def set_mis_cursos(self, curso=object):
        self.__mis_cursos.append(curso)
    #!<----------------------
    def __str__(self):
        return "Estudiante: " + super().__str__() + f", Legajo = {self.__legajo}, Año Inscripcion en la Carrera = {self.__anio_inscripcion_carrera}"

    def Matricular_en_curso(self, curso: object, contrasenia=str):
        if (buscar_curso(curso.get_nombre(), self.__mis_cursos)):  #!!!--- se usa la fun buscar_curso para validar si ya tiene ese curso o no.
            print(f"Usted ya estaba anotado en {curso.get_nombre()}") #!!!--- curso.get_nombre nos da solo el nombre del curso que ya esta anotado
        else:
            if (contrasenia == curso.get_contrasenia()): #!!si la contraseña es igual se agrega el objeto curso a mis_cursos[]
                self.__mis_cursos.append(curso)
                print(f"Materia: {curso.get_nombre()} agregada a Mis Cursos..")#!!!--- se informa
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

    def Dictar_curso(self): #!!!--- Funcion que crea cursos.
        nombre = input("Ingrese el nombre del curso: ")
        nuevo_curso = Curso(nombre)
        self.__mis_cursos.append(nuevo_curso)
        lista_cursos.append(nuevo_curso)
        print(nuevo_curso)
# !_____________________
class Curso (): #!!cursos es un objeto que no depende de los otros. 
    def __init__(self, nombre=str): #!! solo se le pasa el nombre
        self.__nombre = nombre
        self.__contrasenia_matriculacion = self.__generar_contrasenia() #!!! cuando se crea el curso (solo con el nombre) se activa la fun generar_contraceña
        self.__archivos = [] #!!---Este es para la segunda parte del tp. (ahora Creo que no hay que hacer nada)
    
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
    #!<------------------------------------

    def __str__(self):
        return f"Curso: Nombre = {self.__nombre}, Contraseña de Matriculacion = {self.__contrasenia_matriculacion}"

    def __generar_contrasenia(self): #!!Fun que crea contraseñas de matriculacion. 
        l_random = random.randint(0,26)
        n_random = random.randint(0,9)
        
        nums = ["1","2","3","4","5","6","7","8","9","0"]
        abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        
        contracenia = f"{nums[n_random]}{abc[l_random]}{nums[n_random]}{abc[l_random]}{nums[n_random]}{abc[l_random]}"
        return  contracenia      
# !__________funciones___________
def mostrar_listas(lista = list): #!!!--------- Muestra los nombres de la lista enumerados para que el usuario elija.
    print("----------------------------")
    for i,valor in enumerate(lista):
        print(f"{i+1}. {valor.get_nombre()}\n")
        
def mostrar_mis_cursos(lista_objetos = list, indice = int): ##!!!--- muestra mis_cursos[] (dea del profesor o del alumno)
    mis_cursos = lista_objetos[indice].get_mis_cursos()
    mostrar_listas(mis_cursos)
        
def buscar_usuario(lista = list, email = str, contrasenia = str): #!!!--- Comprueba si el Alumno o profesor existe o no con el mail (falta que comprueve la contraseña)
    for indice, valor in enumerate(lista): 
        if valor.validar_credenciales(email , contrasenia):
          return True, indice #!!!--- si lo encuentra Retorna True y el indice de donde se encuentra
    return False, 0 #!___ 0 po
    
def mostrar_cursos(lista = list): #!!! muestra todos los cursos que estan anotados en el sistema con el formato que se pide.
    cursos_prdenados = sorted(lista, key=lambda x: x.get_nombre())
    for i in cursos_prdenados: 
        print(f"Materia: {i.get_nombre()}\t\tCarrera: Tecnicatura Universitaria en Programación\n")

def existencia_alumno(mail:str,registrados):
    for i in registrados:  
        obtener_email = i.get_email()
        if (obtener_email==mail):
            return True
    return False

#!---------Creacion de Objetos-----------Crea Estudiantes/profesores/y cursos y los agrega a la listas (la que estan arriba de todo)
alumno_uno = Estudiante("Lautaro", "Vega", "Lautaro.vega@gmail.com", "2424a", 5858, 2023)
alumno_dos = Estudiante("Maria", "Gomez", "Maria.g@gmail.com", "1234a", 5050, 2022)
alumno_tres = Estudiante("Victoria", "Sosa", "Vicky.ss@gmail.com", "2444a", 3030, 2023)
alumnos_registrados.append(alumno_uno)
alumnos_registrados.append(alumno_dos)
alumnos_registrados.append(alumno_tres)

prof_uno = Profesor("Gustavo", "Ramirez","Gustavo.Ramirez@gmail.com", "3883a", "Ingeniero", 2005)
prof_dos = Profesor("Bettiana", "apellidoRaro","bettiana.123@gmail.com", "1010a", "Ingeniera", 2000)
prof_tres = Profesor("Veronica", "Zanches","Veronica.z@gmail.com", "5050b", "Ingeniera", 1999)
profesores_registrados.append(prof_uno)
profesores_registrados.append(prof_dos)
profesores_registrados.append(prof_tres)

curso_uno = Curso("Programacion I")
curso_dos = Curso("Matematicas")
curso_tres = Curso("Estadistica")
lista_cursos.append(curso_uno)
lista_cursos.append(curso_dos)
lista_cursos.append(curso_tres)

#!!!----- se agrega algunso cursos a algunos profesores y alumos ----
prof_uno.set_mis_cursos(curso_tres)
prof_dos.set_mis_cursos(curso_dos)
prof_tres.set_mis_cursos(curso_uno)

alumno_tres.set_mis_cursos(curso_uno)
alumno_tres.set_mis_cursos(curso_dos)
alumno_tres.set_mis_cursos(curso_tres)

print("\n")
mostrar_mis_cursos(alumnos_registrados, 0)
mostrar_mis_cursos(alumnos_registrados,1)
mostrar_mis_cursos(alumnos_registrados,2)

mostrar_mis_cursos(profesores_registrados,0)

print(alumno_tres.get_email())
print(curso_uno)
