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
            validacion, indice = ob.buscar_usuario(
                ob.alumnos_registrados, mail)
            if (validacion):
                print("\n\t\t--Accedio al Sistema.--\n")
                op_alumn = input(
                    "1. Matricularse a un curso\n2. Ver curso\n3. Volver al menú principal\n\t")
                if (op_alumn.isdigit()):
                    op_alumn = int(op_alumn)
                    if op_alumn == 1:
                        ob.mostrar_listas(ob.lista_cursos)
                        op_alumn = input("Seleciona una opcion: ")
                        if (op_alumn.isdigit()):
                            op_alumn = int(op_alumn)
                            if op_alumn <= len(ob.lista_cursos) and op_alumn >= 1:
                                i_lista_curso = op_alumn - 1
                                pass_curso = input("Digite la contraseña: ")
                                ob.alumnos_registrados[indice].Matricular_en_curso(
                                    ob.lista_cursos[i_lista_curso], pass_curso)
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
        elif (op == 2):
            print("\n\t\t--Ingresar Profesor--\n\n")
            mail = input("Ingrese su E-mail: ")
            contrasenia = input("Ingrese su contraseña: ")
            validacion, indice = ob.buscar_usuario(
                ob.profesores_registrados, mail)
            if (validacion):
                prof = indice
                print("\n\t\t--Accedio al Sistema.--\n")
                op_prof = input(
                    "1. Matricularse a un curso\n2. Ver curso\n3. Volver al menú principal\n\t")
                if (op_prof.isdigit()):
                    op_prof = int(op_prof)
                    if op_prof == 1:
                        op_prof = input(
                            "1 Programación I\n2 Programación II\n3 Laboratorio II\n4 InglesI\n5 InglesII...")
                        if (op_prof.isdigit()):
                            op_prof = int(op_prof)
                            if op_prof == 1:
                                pass
                            elif op_prof == 2:
                                pass
                            elif op_prof == 3:
                                pass
                            elif op_prof == 4:
                                pass
                            elif op_prof == 5:
                                pass
                            else:
                                print("Opcion no valida..")
                        else:
                            print("Debe ingresar un numero entero..")
                    elif op_prof == 2:
                        ob.mostrar_cursos(
                            ob.alumnos_registrados[prof].mis_cursos)
                    elif op_prof == 3:
                        "Vuelve al menu principal"
                    else:
                        print("Opcion no valida")
                else:
                    print("Debe ser un numero entero")
            else:
                print("Error de ingreso.")

        #!------Op Tres, lsito-----

        elif (op == 3):
            print("\n\t\t--Ver Curso--")
            ob.mostrar_cursos(ob.lista_cursos)

        elif (op == 4):
            print("\n\t\t--Salir--")

        else:
            print("\n\tOpcion no valida.")
    else:
        print("Debe ser un numero entero.")
