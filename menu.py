import objetos as ob
##!!! -----menu profesor------
def menu_profesor():
    op_prof = 0
    while(op_prof!=3):
        op_prof = input("\n\t\t--Accedio al Sistema.--\n1. Dictar curso \n2. Ver mis cursos \n3. Volver al menú principal\n\t")
        if (op_prof.isdigit()):
            op_prof = int(op_prof)
            if op_prof == 1: #!!!---- con el indice se busca el objeto y se llama al metodo .Dictar_curso()
                ob.profesores_registrados[indice].Dictar_curso()#!!!---- CREA UN CUSRO.

            elif op_prof == 2:
                ob.mostrar_mis_cursos(ob.profesores_registrados,indice)#!!!--- Muestra los cursos del Profesor, 
                op_prof = input("Seleciones un curso.\n")
                if op_prof.isdigit():
                    op_prof = int(op_prof)
                    if (op_prof >= 1 or op_prof <= len(ob.profesores_registrados[indice].mis_cursos)):
                        #!!!---ListaProfesores[indice] nos da el objeto Prof, .mis_cursos[indice] nos da el objeto Curso que se eligio--
                        print(ob.profesores_registrados[indice].mis_cursos[op_prof-1]) #!!!----imprime en nombre del curso y la contraseña
                        print(f"\n     \tCantidad de archivos:{len(ob.profesores_registrados[indice].mis_cursos[op_prof-1].archivos)}")
                        
                        ingresa_archivo = input("¿Desea ingresar un archivo? S/N")
                        while(ingresa_archivo!="s"and ingresa_archivo!="S"and ingresa_archivo!="n" and ingresa_archivo!="N" ):
                            ingresa_archivo = input("Desea ingresar un archivo) SI/NO")
                        
                        if(ingresa_archivo=="s" or ingresa_archivo=="S"):
                            archivo_nombre = input ("Ingresar el nombre del archivo:")
                            archivo_formato = input ("Ingresar formato archivo:")
                            ob.profesores_registrados[indice].mis_cursos[op_prof-1].Ingresar_archivo( archivo_nombre,archivo_formato)
                    else:
                        print("Ingrese una opcion valida.. \n")
                else: 
                    print("Debe ser un numero entero.. \n")
            elif op_prof == 3:
                print("Vuelve al menu principal\n")
            else:
                print("Opcion no valida\n")
        else:
            print("Debe ser un numero entero\n")
#!!! -----menu alumno------
def menu_alumno():
    op_alumn=0 
    while(op_alumn!=3):
        op_alumn = input("\n\t\t--Accedio al Sistema.--\n1. Matricularse a un curso\n2. Ver curso\n3. Volver al menú principal\n\t")
        if (op_alumn.isdigit()):#!!!-----si es digito entra sino vuelve al menu principal.
            op_alumn = int(op_alumn)#!!!----se combierte el op en entero.
            if op_alumn == 1:
                ob.mostrar_listas(ob.lista_cursos)#!!!-----funcion que impime la lista que se desea
                op_alumn = input("Seleciona una opcion: ")
                if (op_alumn.isdigit()):
                    op_alumn = int(op_alumn)
                    if op_alumn <= len(ob.lista_cursos) and op_alumn >= 1:#!!!-----Se comprueba si se eligio bien, op_alumn(opcion elegida) <= largo de la lista
                        indice_curso = op_alumn - 1 #!!!---- op_alumn-1 ahora es el numero de indice de la lista que se desea
                        pass_curso = input("Digite la contraseña: ") #!!!---- Se pide la contraseña de maticulacion
                        ob.alumnos_registrados[indice].Matricular_en_curso(ob.lista_cursos[indice_curso], pass_curso)#!!!---se busca en la lista el alumno.Metodo(matricular_en_curso)
                    else:
                        print("Opcion no valida..")
                else:
                    print("Debe ingresar un numero entero..")
            elif op_alumn == 2:
                print("----\nDESMATRICULARSE-----")
                ob.mostrar_mis_cursos(ob.alumnos_registrados, indice)#!!!-----muestra mis cursos.
                op_alumn = input("Seleciona una opcion: ")
                if (op_alumn.isdigit()):
                    op_alumn = int(op_alumn)
                    if op_alumn <= len(ob.alumnos_registrados[indice].mis_cursos) and op_alumn >= 1: #!!!-----Se comprueba si se eligio bien
                        indice_curso = op_alumn - 1 #!!!----indice de la lista mis_cusos
                        confirm = input("¿Desea Desmatricularse del curso? s/n ") #!!!---- Se pide Confirmacion
                        ob.alumnos_registrados[indice].Desmatricular(ob.alumnos_registrados[indice].mis_cursos[indice_curso], confirm)#!!!---se busca en la lista el alumno.Metodo(matricular_en_curso)
                    else:
                        print("Opcion no valida..")
                else:
                    print("Debe ingresar un numero entero..")
            elif op_alumn == 3: 
                ob.mostrar_mis_cursos(ob.alumnos_registrados, indice)#!!!-----muestra mis cursos.
                op_alumn = input("Seleciona una opcion: ")
                if (op_alumn.isdigit()):
                    op_alumn = int(op_alumn)
                    if op_alumn <= len(ob.alumnos_registrados[indice].mis_cursos) and op_alumn >= 1:
                        indice_curso = op_alumn - 1
                        ob.alumnos_registrados[indice].Mostrar_archivos(indice_curso)
                    else:
                        print("Opcion no valida..")
                else:
                    print("Debe ingresar un numero entero..")
                    
            elif op_alumn == 4:
                print("Vuelve al menu principal")
            else:
                print("Opcion no valida")
        else:
            print("Debe ser un numero entero")

##!!! -----menu------
op = 0
while (op != 4):
    op = input(
        "1. Ingresar cómo alumno\n2. Ingresar cómo profesor\n3. Ver cursos\n4. Salir\n\t")
    if (op.isdigit()):
        op = int(op)
        if (op == 1):###!!!------opcion 1
            print("\n\t\t--Ingresar Alumno--\n\n")
            mail = input("Ingrese su E-mail: ")##!!!-----input para ingresar como alumno                 
            if ob.existencia_alumno(mail,ob.alumnos_registrados):
                contrasenia = input("Ingrese su contraseña: ")
                validacion, indice = ob.buscar_usuario(ob.alumnos_registrados, mail , contrasenia)##!!!-----Se usa la funcion buscar usuario (retorna un boleano y un indice)
                if (validacion):#!!!------si es true accede
                    menu_alumno()#!!!------  
                else:
                    print("Error de ingreso.")
            else:
                print("debe darse de alta en alumnado.....\n")
        #!----------------Profesores-----------------------!!!---Es muy similar a ingresar Alumno
        elif (op == 2):
            print("\n\t\t--Ingresar Profesor--\n\n")
            mail = input("Ingrese su E-mail: ")
            if ob.existencia_alumno(mail,ob.profesores_registrados):
                contrasenia = input("Ingrese su contraseña: ")
                validacion, indice = ob.buscar_usuario(ob.profesores_registrados, mail, contrasenia)#!!!----Esta fun nos da el Indice
                if (validacion):
                    menu_profesor()
                else:
                    print("Error de ingreso.\n")
            else:
                print("debe darse de alta en profesorado.....\n")
        #!------Op Tres-----
        elif (op == 3):
            print("\n\t\t--Ver Curso--")
            ob.mostrar_cursos(ob.lista_cursos) #!!!---Muestra todos los cursos de la forma que lo pide el cuadernillo

        elif (op == 4):
            print("\n\t\t--Salir--")

        else:
            print("\n\tOpcion no valida.\n")
    else:
        print("Debe ser un numero entero.\n")
