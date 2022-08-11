
import os
import math


def punto3():
    op = 1

    while (op != 0):
        print("             ACTIVIDAD 3        ")
        print("")
        print("")
        print("Dita 3 numeros para ordenarlos de mayor a menor")
        print("1............Factorial")
        print("2............Serie Taylor")
        print("3............Serie SENO y COSENO")
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
                num = 0
                while (num <= 0):
                    num = int(
                        input("Digita un numero para obtener su factorial: "))
                    if (num <= 0):
                        print('Debe digitar un numero mayor a 0.')
                facto = num
                respu = num
                os.system('cls')
                while (num > 0):
                    if (num > 1):
                        facto = facto * (num-1)
                    num = num - 1
                print('El factorial de ', respu, ' es: ', facto)
            except:
                print('Error dato invalido')
        if (op == 2):
            try:
                num = int(
                    input("Digita un numero para obtener la solucion de la serie: "))
                dato = 0
                os.system('cls')
                for i in range(0, num + 1):
                    dato += (math.pow(5, i) / math.factorial(i))
                print('Respuesta de la serie: ', dato)
            except:
                print('Error dato invalido')
        if (op == 3
                ):
            try:
                n = int(input("Digita el valor de n: "))
                x = int(input("Digita el valor de x: "))

                sen = math.pow(-1, n) * (math.pow(x, 2*n+1) /
                                         math.factorial(2*n+1))
                cos = math.pow(-1, n) * (math.pow(x, 2*n) /
                                         math.factorial(2*n))

                print('SENO: ', sen)
                print('SENO: ', cos)
            except:
                print('Error dato invalido')
        if (op == 0):
            os.system('cls')
