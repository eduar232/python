
import os


def punto2():
    op = 1

    while (op != 0):
        print("             ACTIVIDAD 2       ")
        print("")
        print("")
        print("Dita 3 numeros para ordenarlos de mayor a menor")
        print("1............Describir edad")
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
                edad = 0
                edad = int(input("Digita tu edad: "))
                os.system('cls')
                if (edad == 1):
                    print(f"Felicidades, tienes  {edad} año")
                else:
                    print(f"Felicidades, tienes  {edad} años")
                print('')
            except:
                print('Error dato invalido')
        if (op == 0):
            os.system('cls')
