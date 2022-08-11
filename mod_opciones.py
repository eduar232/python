import os

from library.mod_actividad1 import *
from library.mod_actividad2 import *
from library.mod_actividad3 import *


def opciones():
    op = 1
    while (op != 0):
        print("             ACTIVIDAD 1        ")
        print("")
        print("")
        print("1............Actividad 1.")
        print("1............Actividad 2.")
        print("2............Actividad 3.")
        print("0............Salir.")
        print("")
        try:
            op = int(input("Que opcion elijes: "))
            print("")
        except:
            print('Error dato invalido')

            if (op < 1 or op > 4):
                print("Por favor elija una opcion entre 1 y 4")
        if (op == 1):
            os.system('cls')
            punto1()
            os.system('cls')
        if (op == 2):
            os.system('cls')
            punto2()
            os.system('cls')
        if (op == 3):
            os.system('cls')
            punto3()
            os.system('cls')
        if (op == 0):
            os.system('cls')
