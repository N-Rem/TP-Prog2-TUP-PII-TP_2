import random
from datetime import date
alumnos_registrados = []
profesores_registrados = []
lista_cursos = []

class Usuario(): #!!!---class padre
    def __init__(self, nombre=str, apellido=str, email=str, contrasenia=str): #!--- se ponde =str para remarcar que el valor del atributo tiene que ser en este caso String
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasenia = contrasenia
    
    #!get-set---------> Get solo devuleve el valor del atributo, y set solo cambia el valor del atributo.
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre=str):
        self.__nombre = nombre
    
    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self, apellido=str):
        self.__apellido = apellido
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email=str):
        self.__email = email    

    @property
    def contrasenia(self):
        return self.__contrasenia
    @contrasenia.setter
    def contrasenia(self, contrasenia=str):
        self.__contrasenia = contrasenia  
     #!<-----------------------        
    def __str__(self): #!!!---cuando se imprime el objeto aparece sin nada se imprime esta cadena
        return f"Nombre = {self.__nombre}, Apellido = {self.__apellido}, E-mail = {self.__email}, Contraseña = {self.__contrasenia}"

    def validar_credenciales(self, email: str, contrasena: str):
        if email == self.__email and contrasena == self.__contrasenia:
            return True
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
    @property
    def mis_cursos(self):
        return self.__mis_cursos
    @mis_cursos.setter
    def mis_cursos(self, curso=object):
        self.__mis_cursos.append(curso)
    #!<----------------------
    def __str__(self):
        return "Estudiante: " + super().__str__() + f", Legajo = {self.__legajo}, Año Inscripcion en la Carrera = {self.__anio_inscripcion_carrera}"

    def Matricular_en_curso(self, curso= object, contrasenia=str):
        if (buscar_curso(curso.nombre, self.__mis_cursos)):  #!!!--- se usa buscar_curso para validar si ya tiene ese curso o no.
            print(f"Usted ya estaba anotado en {curso.nombre}") #!!!--- curso.nombre nos da solo el nombre del curso que ya esta anotado
        else:
            if (contrasenia == curso.contrasenia): #!!si la contraseña es igual se agrega el objeto curso a mis_cursos[]
                if(buscar_curso(curso.nombre, tecnicatura_uno.cursos()) ):    
                    if(buscar_curso(self.nombre, tecnicatura_uno.alumnos())):
                        self.__mis_cursos.append(curso)
                        print(f"Materia: {curso.nombre} agregada a Mis Cursos..")#!!!--- se informa
                    else:
                        print("el alumno no se encontro en la carrera....")
                elif (buscar_curso(curso.nombre, tecnicatura_dos.cursos()) ):    
                    if(buscar_curso(self.nombre, tecnicatura_dos.alumnos())):
                        self.__mis_cursos.append(curso)
                        print(f"Materia: {curso.nombre} agregada a Mis Cursos..")#!!!--- se informa

                    else:
                        print("el alumno no se encontro en la carrera....")
                else:
                    print("--------------no se encontro el alumno en inigun curso-----")
            else:
                print("Contraseña no valida..")
                   
    def Desmatricular (self, curso = object, confirm = str):
        if (confirm == "s"):
            for i, obj in enumerate(self.__mis_cursos):
                if obj == curso:
                    print(f"Se borro el curso: {self.__mis_cursos[i].nombre}")
                    print(self.__mis_cursos[i])
                    del self.__mis_cursos[i]
                    
        else: 
            print("No se Borro ningun curso..")

    def Mostrar_archivos(self, indice): 
       curso = self.__mis_cursos[indice]
       print (f"\n\n\t\t{curso.nombre}")
       for i in curso.archivos:
           print (i)
#--
def buscar_curso(curso=str, lista=list):
    for i in lista:
        if curso == i.nombre:
            return True
    return False
# !_____________________
class Profesor(Usuario):
    def __init__(self, nombre=str, apellido=str, email=str, contrasenia=str, titulo=str, anio_egreso=int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.__mis_cursos = []
        
    @property
    def mis_cursos(self):

        return self.__mis_cursos
    @mis_cursos.setter
    def mis_cursos(self, curso=object):
        self.__mis_cursos.append(curso)

    def __str__(self):
        return "Profesor: " + super().__str__() + f", Titulo = {self.__titulo}  ,  Año de Egreso = {self.__anio_egreso} , "

    def Dictar_curso(self): #!!!--- agrega nuevos cursos para dictar.
        nombre = input("Ingrese el nombre del curso: ")
        nuevo_curso = Curso(nombre)
        self.__mis_cursos.append(nuevo_curso)
        lista_cursos.append(nuevo_curso)
        print(nuevo_curso)
   
# !_____________________
class Curso (): #!!no depende de los otros. 
    __codigo = 0
    def __init__(self, nombre=str): #!! solo se le pasa el nombre
        self.__nombre = nombre
        self.__contrasenia_matriculacion = self.__generar_contrasenia() #!!! cuando se crea el curso (solo con el nombre) se activa generar_contraceña
        self.__archivos = []
        self.__codigo = Curso.__codigo
        Curso.__codigo += 1
    #!set, get nombre y archivos
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre=str):
        self.__nombre = nombre
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo=int):
        self.__codigo = codigo
    @property
    def contrasenia (self):
        return self.__contrasenia_matriculacion
    
    @property 
    def archivos(self):
        return self.__archivos
    @archivos.setter
    def archivos(self, archivos):
        self.__archivos.append(archivos)
    #!<------------------------------------

    def __str__(self):
        return f"   \tCurso: \n   \tNombre = {self.__nombre} \n   \tContraseña de Matriculacion = {self.__contrasenia_matriculacion}\n     \tCodigo: {Curso.__codigo}"

    def __generar_contrasenia(self): #!crea contraseñas matriculacion. 
        l_random = random.randint(0,26)
        n_random = random.randint(0,9)
        
        nums = ["1","2","3","4","5","6","7","8","9","0"]
        abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        
        contracenia = f"{nums[n_random]}{abc[l_random]}{nums[n_random]}{abc[l_random]}{nums[n_random]}{abc[l_random]}"
        return  contracenia      
    
    def Ingresar_archivo(self,nombre,formato):
        nuevo_archivo= Archivo(nombre,formato)
        self.__archivos.append(nuevo_archivo)
        print(nuevo_archivo)

#!__________Carrera______________
class Carrera():
    def __init__(self, nombre=str, cant_anios=str, cantidad_materias = int):
        self.__nombre = nombre
        self.__cant_anios = cant_anios
        self.__cantidad_materias = cantidad_materias
        self.__alumnos = []
        self.__cursos = []

    @property
    def nombre(self):
        return self.__nombre
    @property
    def cant_anios(self):
        return self.__cant_anios
    
    def __str__(self):
        return f"Carrera: Nombre = {self.__nombre}, Cantidad de Años = {self.__cant_anios}"
    
    @property
    def cantidad_materias(self):
        return self.__cantidad_materias
    @property
    def alumnos(self):
        return self.__alumnos 
    @alumnos.setter
    def alumnos(self, alumnos):
        self.__alumnos.append(alumnos)
     
    @property   
    def cursos(self):
        return self.__cursos
    @cursos.setter
    def cursos(self,cursos):
        self.__cursos.append(cursos)

#!__________Archivo______________
class Archivo():
    def __init__(self, nombre = str, formato = str):
        self.__nombre = nombre
        self.__formato = formato
        self.__fecha = date.today()
        
    def __str__(self):
        return f"Archivo\nNombre = {self.__nombre}\nFecha = {self.__fecha}\nFormato = {self.__formato}\n"

# !__________funciones___________
def mostrar_listas(lista = list): #!!! --------- Muestra la lista enumeradas para que el usuario elija.
    print("----------------------------")
    for i,valor in enumerate(lista):
        print(f"{i+1}. {valor.nombre}\n")
        
def mostrar_mis_cursos(lista_objetos = list, indice = int): ##!!!--- muestra mis_cursos[] (del profesor o del alumno)
    mis_cursos = lista_objetos[indice].mis_cursos
    mostrar_listas(mis_cursos)
        
def buscar_usuario(lista = list, email = str, contrasenia = str): #!!!--- Comprueba si el Alumno o profesor existe con el mail
    for indice, valor in enumerate(lista): 
        if valor.validar_credenciales(email , contrasenia):
          return True, indice #!!!--- si lo encuentra Retorna True y el indice de donde se encuentra
    return False, 0 
    
def mostrar_cursos(lista = list): #!!! muestra todos los cursos que estan anotados en el sistema con el formato que se pide.
    cursos_ordenados = sorted(lista, key=lambda x: x.nombre)
    for i in cursos_ordenados: 
        print(f"Materia: {i.nombre}\t\tCarrera: Tecnicatura Universitaria en Programación\n")

def existencia_alumno(mail=str,registrados=list):
    for i in registrados:  
        obtener_email = i.email
        if (obtener_email==mail):
            return True
    return False

#!---------Creacion de Objetos-----------
lautaro = Estudiante("Lautaro", "Vega", "Lautaro.vega@gmail.com", "2424a", 5858, 2023)
maria = Estudiante("Maria", "Gomez", "Maria.g@gmail.com", "1234a", 5050, 2022)
vicky = Estudiante("Victoria", "Sosa", "Vicky.ss@gmail.com", "2444a", 3030, 2023)
fabri = Estudiante("Fabri", "Sola", "fabri.s@gmail.com", "444a", 4030, 2023)

alumnos_registrados.append(lautaro)
alumnos_registrados.append(maria)
alumnos_registrados.append(vicky)
alumnos_registrados.append(fabri)
#!------------------------------------------Profesores---

gustavo_r = Profesor("Gustavo", "Ramirez","Gustavo.Ramirez@gmail.com", "3883a", "Ingeniero", 2005)
bettiana = Profesor("Bettiana", "Azul","bettiana.123@gmail.com", "1010a", "Ingeniera", 2000)
veronica_z = Profesor("Veronica", "Zanches","Veronica.z@gmail.com", "5050b", "Ingeniera", 1999)
profesores_registrados.append(gustavo_r)
profesores_registrados.append(bettiana)
profesores_registrados.append(veronica_z)
#!-----------------------Cusos--------
porg_uno = Curso("Programacion I")
mates_uno = Curso("Matematicas")
arquitectura = Curso("Arquitectura")
prog_tres = Curso("Programacion II")
estadistica = Curso("Estadistica")
analisis_uno = Curso("Analisis I")

lista_cursos.append(porg_uno)
lista_cursos.append(mates_uno)
lista_cursos.append(arquitectura)
lista_cursos.append(prog_tres)
lista_cursos.append(estadistica)
lista_cursos.append(analisis_uno)

#!!!----- se agrega algunso cursos a algunos: profesores 
gustavo_r.mis_cursos = arquitectura
bettiana.mis_cursos = mates_uno
veronica_z.mis_cursos =porg_uno
veronica_z.mis_cursos = estadistica
#!!!----y alumnos ----
vicky.mis_cursos = porg_uno
vicky.mis_cursos=mates_uno
vicky.mis_cursos=arquitectura

#!---Crea archivos
archivo_uno = Archivo("java", "pfd")
archivo_dos = Archivo("JS", "pfd")
#!--- Agrega cursos
porg_uno.archivos = archivo_uno
porg_uno.archivos = archivo_dos

#!-------------------Crea Carrea-------
tecnicatura_uno = Carrera("Tecnicatura I","3",3)
tecnicatura_uno.cursos = porg_uno
tecnicatura_uno.cursos=mates_uno
tecnicatura_uno.cursos=arquitectura

tecnicatura_uno.alumnos=vicky
tecnicatura_uno.alumnos=fabri


tecnicatura_dos = Carrera("tecnicatura II", "2",3)
tecnicatura_dos.cursos=estadistica
tecnicatura_dos.cursos=analisis_uno
tecnicatura_dos.cursos=prog_tres

tecnicatura_dos.alumnos=lautaro
tecnicatura_dos.alumnos=maria
