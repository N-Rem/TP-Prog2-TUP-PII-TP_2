##!!! -----menu------

op = input(
    "1. Ingresar cómo alumno\n2. Ingresar cómo profesor\n3. Ver cursos\n4. Salir\n\t")

if (op.isnumeric()):
    op = int(op)
    if (op == 1):
        print("\n\t\t--Ingresar Alumno--")
        if (True):
            print("existe, da accedo al sistema.")
            op_alumn = input("1. Matricularse a un curso\n2. Ver curso\n3. Volver al menú principal\n\t")
            if (op_alumn.isnumeric()):
                op_alumn = int(op_alumn)
                if op_alumn == 1:
                    "Lsita de cursos"
                elif op_alumn == 2:
                    "Lista de cursos alumno matriculado"
                elif op_alumn == 3:
                    "Vuelve al menu principal"
                else:
                    print("Opcion no valida")
            else:
                print("Debe ser un numero entero")
        else:
            print("Error de ingreso.")
    elif (op == 2):
        print("\n\t\t--Ingresar Profesor--")
        if(True): 
            print("existe, da accedo al sistema.")
            op_prof = input("1. Dictar curso\n2. Ver curso\n3. Volver al menú principal\n\t")
            if (op_prof.isnumeric()):
                op_prof = int(op_prof)
                if op_prof == 1:
                    "se crea un curso y se la agrega a una Lsita de cursos"
                elif op_prof == 2:
                    "Lista de cursos Prof posee"
                elif op_prof == 3:
                    "Vuelve al menu principal"
                else:
                    print("Opcion no valida")
            else:
                print("Debe ser un numero entero")
        else:
            print("Error de ingreso.")

    elif (op == 3):
        print("\n\t\t--Ver Curso--")
        "lista de los cursos."

    elif (op == 4):
        print("\n\t\t--Salir--")

    else:
        print("\n\tOpcion no valida.")

else:
    print("Debe ser un numero entero.")
