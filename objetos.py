class Usuario():
    def __init__ (self, nomb, lasname, mail, passw):
        self.__nomb: nomb
        self.__lasname: lasname
        self.__mail: mail
        self.__passw: passw
    def __str__():
        self =" cosas"
    def validar_credenciales(mail, passw): 
        if (mail != str or passw != str):
            return False
        else: return True
# !_____________________        
        
class Estudiante(Usuario): 
    def __init__(self, legajo):
        self.legajo: legajo
# !_____________________        
        
        
class Profesor(Usuario): 
    def __init__(self, nomb, lasname, mail, passw):
        super().__init__(nomb, lasname, mail, passw, titulo, egreso)
# !_____________________        


class Cusro (Estudiante, Profesor):
    def __init__(self, nombr, pass_matriculacion):
        self.nomb: nombr
    def __generar_contrasenia__ ():
        return "Contraseña"
# !_____________________        
    