
import os


def punto1():
    op = 1
    salida = False

    while (op != 0):
        print("             ACTIVIDAD 1        ")
        print("")
        print("")
        print("Dita 3 numeros para ordenarlos de mayor a menor")
        print("1............Comenzar")
        print("0............Salir.")
        print("")
        try:
            op = int(input("Que opcion elijes: "))
            print("")
        except:
            print('Error dato invalido')

            if (op < 1 or op > 4):
                print("Opcion no valida.")
        if (op == 1):
            try:
                n1 = int(input("Primer numero: "))
                n2 = int(input("Primer numero: "))
                n3 = int(input("Primer numero: "))

                listado = []

                listado.append(n1)
                listado.append(n2)
                listado.append(n3)
                listado.sort(reverse=True)
                os.system('cls')
                print("Numero del mayor: ", listado[0])
                print("Numero del medio: ", listado[1])
                print("Numero menor: ",     listado[2])
                print("")
                print("")
            except:
                print('Error dato invalido')
        if (op == 0):
            os.system('cls')
