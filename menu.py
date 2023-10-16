##!!! -----menu------
import objetos as ob
op = 0
while (op != 4):
    op = input(
        "1. Ingresar cómo alumno\n2. Ingresar cómo profesor\n3. Ver cursos\n4. Salir\n\t")
    if (op.isdigit()):
        op = int(op)
        if (op == 1):
            print("\n\t\t--Ingresar Alumno--\n\n")
            mail = input("Ingrese su E-mail: ")
            contrasenia = input("Ingrese su contraseña: ")
            validacion, indice = ob.buscar_usuario(ob.alumnos_registrados, mail)
            if (validacion):
                op_alumn = input("\n\t\t--Accedio al Sistema.--\n1. Matricularse a un curso\n2. Ver curso\n3. Volver al menú principal\n\t")
                if (op_alumn.isdigit()):
                    op_alumn = int(op_alumn)
                    if op_alumn == 1:
                        ob.mostrar_listas(ob.lista_cursos)
                        op_alumn = input("Seleciona una opcion: ")
                        if (op_alumn.isdigit()):
                            op_alumn = int(op_alumn)
                            if op_alumn <= len(ob.lista_cursos) and op_alumn >= 1:
                                indice_curso = op_alumn - 1
                                pass_curso = input("Digite la contraseña: ")
                                ob.alumnos_registrados[indice].Matricular_en_curso(ob.lista_cursos[indice_curso], pass_curso)
                            else:
                                print("Opcion no valida..")
                        else:
                            print("Debe ingresar un numero entero..")
                    elif op_alumn == 2:
                        ob.mostrar_mis_cursos(ob.alumnos_registrados, indice)
                    elif op_alumn == 3:
                        print("Vuelve al menu principal")
                    else:
                        print("Opcion no valida")
                else:
                    print("Debe ser un numero entero")
            else:
                print("Error de ingreso.")
        #!----------------Profesores-----------------------
        elif (op == 2):
            print("\n\t\t--Ingresar Profesor--\n\n")
            mail = input("Ingrese su E-mail: ")
            contrasenia = input("Ingrese su contraseña: ")
            validacion, indice = ob.buscar_usuario(ob.profesores_registrados, mail)
            if (validacion):
                op_prof = input("\n\t\t--Accedio al Sistema.--\n1. Dictar curso \n2. Ver mis cursos \n3. Volver al menú principal\n\t")
                if (op_prof.isdigit()):
                    op_prof = int(op_prof)
                    if op_prof == 1:
                        ob.profesores_registrados[indice].Dictar_curso()
                        
                    elif op_prof == 2:
                        ob.mostrar_mis_cursos(ob.profesores_registrados,indice)
                        op_prof = input("Seleciones un curso.\n")
                        if op_prof.isdigit():
                            op_prof = int(op_prof)
                            if (op_prof >= 1 or op_prof <= len(ob.profesores_registrados[indice].get_mis_cursos())):
                                print(ob.profesores_registrados[indice].get_mis_cursos()[op_prof-1])
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
            ob.mostrar_cursos(ob.lista_cursos)

        elif (op == 4):
            print("\n\t\t--Salir--")

        else:
            print("\n\tOpcion no valida.\n")
    else:
        print("Debe ser un numero entero.\n")
