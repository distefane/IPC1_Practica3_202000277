import sys
from random import randint

a = 10
while a == 10:
    # Menú de inicio
    print()
    print("╔═════MENÚ INICIO═════╗")
    print("║  1. Iniciar Juego   ║")
    print("║      2. Salir       ║")
    print("╚═════════════════════╝")
    print()
    opcion = int(input("Escriba el número de la opción que desea elegir: "))

    if opcion == 1:
        # Ingresar ordenes al entrar aquí
        nombre = input("Ingrese su nombre de usuario: ")
        print("**************************************************")
        print()
        print("Vista previa del tablero")
        print("---------------")

        tablero = [[" ", "X", " ", "0", " ", "X"],
                   [" ", " ", " ", " ", "X", " "],
                   [" ", "X", " ", "0", " ", " "],
                   [" ", " ", "X", " ", " ", " "],
                   ["0", " ", " ", "@", " ", " "]]

        for elemento in tablero:
            print("|", elemento[0], elemento[1],
                  elemento[2], elemento[3], elemento[4], elemento[5], "|")
        print("---------------")
        print()

        # Colocar pac-man de forma aleatoria
        fila = randint(0,4)
        columna = randint(0,5)

        while tablero[fila][columna] != " ":
                        fila = randint(0,4)
                        columna = randint(0,5)
        
        tablero[fila][columna] = "<"
        
        vida = 1
        puntos = 0

        while vida != 0 or puntos != 30:
                print()
                print("*******************************")
                print("Usuario: ", nombre)
                print("Vidas: ", vida)
                print("Puntos: ", puntos)
                print()
                print("---------------")
                for elemento in tablero:
                        print("|", elemento[0], elemento[1],
                        elemento[2], elemento[3], elemento[4], elemento[5], "|")
                print("---------------")
                print()

                print("""Movimientos (escribir la letra y presionar enter): 
        ◔ "a" hacia la izquierda, "d" hacia la derecha, "w" hacia arriba, "s" hacia abajo. 
        ◔ Escriba "F" para finalizar el juego.""")
                movimiento = input()

                if movimiento == "a":
                        columna = columna - 1
                        if columna < 0 or tablero[fila][columna] == "X":
                                columna = columna + 1
                        elif tablero[fila][columna] == " ":
                                tablero[fila][columna + 1] = " "
                                tablero[fila][columna] = "<"
                        elif tablero[fila][columna] == "0":
                                puntos = puntos + 10
                                tablero[fila][columna] = " "
                                tablero[fila][columna + 1] = " "
                                tablero[fila][columna] = "<"
                                if puntos == 30:
                                        print()
                                        print("*******************************")
                                        print("Usuario: ", nombre)
                                        print("Vidas: ", vida)
                                        print("Puntos: ", puntos)
                                        print()
                                        print("---------------")
                                        for elemento in tablero:
                                                print("|", elemento[0], elemento[1],
                                                elemento[2], elemento[3], elemento[4], elemento[5], "|")
                                        print("---------------")
                                        print()

                        elif tablero[fila][columna] == "@":
                                vida = vida - 1
                                tablero[fila][columna] = " "
                                tablero[fila][columna + 1] = " "
                                tablero[fila][columna] = "<"
                                if vida == 0:
                                        print()
                                        print("*******************************")
                                        print("Usuario: ", nombre)
                                        print("Vidas: ", vida)
                                        print("Puntos: ", puntos)
                                        print()
                                        print("---------------")
                                        for elemento in tablero:
                                                print("|", elemento[0], elemento[1],
                                                elemento[2], elemento[3], elemento[4], elemento[5], "|")
                                        print("---------------")
                                        print()

                
                elif movimiento == "d":
                        columna = columna + 1
                        if columna > 5 or tablero[fila][columna] == "X":
                                columna = columna - 1
                        elif tablero[fila][columna] == " ":
                                tablero[fila][columna - 1] = " "
                                tablero[fila][columna] = "<"
                        elif tablero[fila][columna] == "0":
                                puntos = puntos + 10
                                tablero[fila][columna] = " "
                                tablero[fila][columna - 1] = " "
                                tablero[fila][columna] = "<"
                                if puntos == 30:
                                        print()
                                        print("*******************************")
                                        print("Usuario: ", nombre)
                                        print("Vidas: ", vida)
                                        print("Puntos: ", puntos)
                                        print()
                                        print("---------------")
                                        for elemento in tablero:
                                                print("|", elemento[0], elemento[1],
                                                elemento[2], elemento[3], elemento[4], elemento[5], "|")
                                        print("---------------")
                                        print()
                        elif tablero[fila][columna] == "@":
                                vida = vida - 1
                                tablero[fila][columna] = " "
                                tablero[fila][columna - 1] = " "
                                tablero[fila][columna] = "<"
                                if vida == 0:
                                        print()
                                        print("*******************************")
                                        print("Usuario: ", nombre)
                                        print("Vidas: ", vida)
                                        print("Puntos: ", puntos)
                                        print()
                                        print("---------------")
                                        for elemento in tablero:
                                                print("|", elemento[0], elemento[1],
                                                elemento[2], elemento[3], elemento[4], elemento[5], "|")
                                        print("---------------")
                                        print()
                

                elif movimiento == "w":
                        fila = fila - 1
                        if fila < 0 or tablero[fila][columna] == "X":
                                fila = fila + 1
                        elif tablero[fila][columna] == " ":
                                tablero[fila + 1][columna] = " "
                                tablero[fila][columna] = "<"
                        elif tablero[fila][columna] == "0":
                                puntos = puntos + 10
                                tablero[fila][columna] = " "
                                tablero[fila + 1][columna] = " "
                                tablero[fila][columna] = "<"
                                if puntos == 30:
                                        print()
                                        print("*******************************")
                                        print("Usuario: ", nombre)
                                        print("Vidas: ", vida)
                                        print("Puntos: ", puntos)
                                        print()
                                        print("---------------")
                                        for elemento in tablero:
                                                print("|", elemento[0], elemento[1],
                                                elemento[2], elemento[3], elemento[4], elemento[5], "|")
                                        print("---------------")
                                        print()

                        elif tablero[fila][columna] == "@":
                                vida = vida - 1
                                tablero[fila][columna] = " "
                                tablero[fila + 1][columna] = " "
                                tablero[fila][columna] = "<"
                                if vida == 0:
                                        print()
                                        print("*******************************")
                                        print("Usuario: ", nombre)
                                        print("Vidas: ", vida)
                                        print("Puntos: ", puntos)
                                        print()
                                        print("---------------")
                                        for elemento in tablero:
                                                print("|", elemento[0], elemento[1],
                                                elemento[2], elemento[3], elemento[4], elemento[5], "|")
                                        print("---------------")
                                        print()

                elif movimiento == "s":
                        fila = fila + 1
                        if fila > 4 or tablero[fila][columna] == "X":
                                fila = fila - 1
                        elif tablero[fila][columna] == " ":
                                tablero[fila - 1][columna] = " "
                                tablero[fila][columna] = "<"
                        elif tablero[fila][columna] == "0":
                                puntos = puntos + 10
                                tablero[fila][columna] = " "
                                tablero[fila - 1][columna] = " "
                                tablero[fila][columna] = "<"
                                if puntos == 30:
                                        print()
                                        print("*******************************")
                                        print("Usuario: ", nombre)
                                        print("Vidas: ", vida)
                                        print("Puntos: ", puntos)
                                        print()
                                        print("---------------")
                                        for elemento in tablero:
                                                print("|", elemento[0], elemento[1],
                                                elemento[2], elemento[3], elemento[4], elemento[5], "|")
                                        print("---------------")
                                        print()

                        elif tablero[fila][columna] == "@":
                                vida = vida - 1
                                tablero[fila][columna] = " "
                                tablero[fila - 1][columna] = " "
                                tablero[fila][columna] = "<"
                                if vida == 0:
                                        print()
                                        print("*******************************")
                                        print("Usuario: ", nombre)
                                        print("Vidas: ", vida)
                                        print("Puntos: ", puntos)
                                        print()
                                        print("---------------")
                                        for elemento in tablero:
                                                print("|", elemento[0], elemento[1],
                                                elemento[2], elemento[3], elemento[4], elemento[5], "|")
                                        print("---------------")
                                        print()

                elif movimiento == "F":
                        break

    elif opcion == 2:
        sys.exit()
