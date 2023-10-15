alumnos_registrados = []
profesores_registrados = []
cusos= []

class Usuario():
    def __init__ (self, nombre, apellido, email, contrasenia):
        self.__nombre: nombre 
        self.__apellido: apellido
        self.__email: email
        self.__contrasenia: contrasenia
    
    def __str__(self):
        return f"Usuario: Nombre = {self.__nombre}, Apellido = {self.__apellido}, E-mail = {self.__email}, Contraseña = {self.__contrasenia}"
    
    def validar_credenciales(mail, passw): 
        if (mail != str or passw != str):
            return False
        else: return True
# !_____________________        
        
class Estudiante(Usuario): 
    def __init__ (self, nombre, apellido, email, contrasenia, legajo, anio_inscripcion_carrera):
        Usuario.__init__(self, nombre, apellido, email, contrasenia)
        self.__legajo: legajo
        self.__anio_inscripcion_carrera: anio_inscripcion_carrera
    
    def __str__ (self):
        return f"Usuario: Nombre = {self.__nombre}, Apellido = {self.__apellido}, E-mail = {self.__email}, Contraseña = {self.__contrasenia}, Legajo = {self.__legajo}, Año Inscripcion de la Carrera = {self.__anio_inscripcion_carrera}"
    
    def matricular_en_curso(curso):
        pass        


# !_____________________        
        
        
class Profesor(Usuario): 
    def __init__ (self, nombre, apellido, email, contrasenia, titulo, anio_egreso):
        Usuario.__init__(self, nombre, apellido, email, contrasenia)
        self.__titulo: titulo
        self.__anio_egreso: anio_egreso
    
    def __str__ (self):
        return f"Usuario: Nombre = {self.__nombre}, Apellido = {self.__apellido}, E-mail = {self.__email}, Contraseña = {self.__contrasenia}, Titulo = {self.__titulo}, Año Egreso = {self.__anio_egreso}"
        
    
    def dictar_curso (curos):
        pass
        

# !_____________________        


class Cusro (Estudiante, Profesor):
    def __init__(self, nombre, contrasenia_matriculacion):
        self.__nombre: nombre
        self.__contrasenia_matriculacion: contrasenia_matriculacion
    
    def __str__(self):
        return f"Curso: Nombre = {self.__nombre}, Contraseña de Matriculacion = {self.__contrasenia_matriculacion}"    
    
    def __generar_contrasenia__ ():
        passw = 0
        return passw
# !_____________________        
    
def Buscar_alumno():
    return str
    pass

def Buscar_existencia():
    return boolean

def agregar_a_lista(lista_de, ob):
    lista_de.append(ob)