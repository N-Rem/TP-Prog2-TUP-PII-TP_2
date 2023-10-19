##!!! -----menu------
import objetos as ob
op = 0
while (op != 4):
    op = input(
        "1. Ingresar cómo alumno\n2. Ingresar cómo profesor\n3. Ver cursos\n4. Salir\n\t")
    if (op.isdigit()):
        op = int(op)
        if (op == 1):###!!!------opcion 1
            print("\n\t\t--Ingresar Alumno--\n\n")
            mail = input("Ingrese su E-mail: ")##!!!-----input para ingresar como alumno
            contrasenia = input("Ingrese su contraseña: ")
            validacion, indice = ob.buscar_usuario(ob.alumnos_registrados, mail)##!!!-----Se usa la funcion buscar usuario (retorna un boleano y un indice)
            if (validacion):#!!!------si es true accede
                op_alumn = input("\n\t\t--Accedio al Sistema.--\n1. Matricularse a un curso\n2. Ver curso\n3. Volver al menú principal\n\t")
                if (op_alumn.isdigit()):#!!!-----si es digito entra sino vuelve al menu principal.
                    op_alumn = int(op_alumn)#!!!----se combierte el op en entero.
                    if op_alumn == 1:
                        ob.mostrar_listas(ob.lista_cursos)#!!!-----funcion que impime la lista que se desea
                        op_alumn = input("Seleciona una opcion: ")
                        if (op_alumn.isdigit()):
                            op_alumn = int(op_alumn)
                            if op_alumn <= len(ob.lista_cursos) and op_alumn >= 1:#!!!-----Se comprueba si se eligio bien, op_alumn(opcion elegida) <= largo de la lista
                                indice_curso = op_alumn - 1 #!!!---- op_alumn-1 ahora es el numero de indice de la lista que se desea, en este caso aumnos_registrados[]..
                                pass_curso = input("Digite la contraseña: ") #!!!---- Se pide la contraseña de maticulacion
                                ob.alumnos_registrados[indice].Matricular_en_curso(ob.lista_cursos[indice_curso], pass_curso)#!!!---se busca en la lista el alumno.Metodo(matricular_en_curso)
                            else:
                                print("Opcion no valida..")
                        else:
                            print("Debe ingresar un numero entero..")
                    elif op_alumn == 2: 
                        ob.mostrar_mis_cursos(ob.alumnos_registrados, indice)#!!!-----2 opcion; solo muestra la lsita de cursos del alumno.
                    elif op_alumn == 3:
                        print("Vuelve al menu principal")
                    else:
                        print("Opcion no valida")
                else:
                    print("Debe ser un numero entero")
            else:
                print("Error de ingreso.")
        #!----------------Profesores-----------------------!!!---Es muy similar a ingresar Alumno
        elif (op == 2):
            print("\n\t\t--Ingresar Profesor--\n\n")
            mail = input("Ingrese su E-mail: ")
            contrasenia = input("Ingrese su contraseña: ")
            validacion, indice = ob.buscar_usuario(ob.profesores_registrados, mail)#!!!----Esta fun nos da el Indice
            if (validacion):
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
                            if (op_prof >= 1 or op_prof <= len(ob.profesores_registrados[indice].get_mis_cursos())):
                                #!!!---ListaProfesores[indice] nos da el objeto Prof, .get_mis_cursos()[indice] nos da el objeto Curso que se eligio--
                                print(ob.profesores_registrados[indice].get_mis_cursos()[op_prof-1]) #!!!----imprime en nombre del curso y la contraseña
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
            else:
                print("Error de ingreso.\n")

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
