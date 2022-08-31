import random
open_game = True
player_lives = 3
machine_lives = 3

def reset():
    print("Deseas jugar 'Cho Han'?\n1.Sí - \nNo (Presiona cualquier tecla para salir)")
    reset = input()
    if reset == "1":
        global player_lives, machine_lives
        player_lives = 3
        machine_lives = 3
    else:
        print("Hasta la próxima!")
        exit()

def checkParImpar(numero): #Function checks if Total number is Even or Odd
    x = int(numero)
    x%=2 #Checking if it's odd or even
    if x == 0:
        par = 2
        print("El número es par!")
    else:
        par = 1
        print("El número es impar!")
    return par

def checkApuesta(player_choice, par): #Function checks who won the bid
    global machine_lives, player_lives
    if int(player_choice) == int(par):
        machine_lives -= 1
    else:
        player_lives -= 1

print("""Bienvenido al juego 'Cho Han' digital simplificado.
Para esta adaptación tú elegirás un número que te guste jugar
y tu adversario (la PC) elegirá otro número al azar entre 1 y 100.
Tú sólo sabrás tu elección hasta que elijas si Apuestas por que el
resultado de la suma de ambos números será Par o Impar.
Cada jugador puede equivocarse 3 veces antes de perder.""")

while open_game == True:
    reset()
    print("Tus oportunidades: "+str(player_lives))
    print("Las del adversario: "+str(machine_lives))

    if (player_lives > 0) and (machine_lives > 0):
        num1 = input("Elige un número entero para jugar.")#Player choose the number is playing
        if num1.isdigit(): #Checking if it's an integer
            player_choice = input("Apuesta! 1.Impar - 2.Par\n") #Player choose Even or Odd
            if player_choice == "1" or player_choice == "2":
                machine_num = random.randint(1,100) #Machine randomize the number is playing
                print("Tu adversario había elegido: " + str(machine_num))
                num1 = int(machine_num) + int(num1) #Total number on play is calculated
                checkParImpar(num1) #Function checks if Total number is Even or Odd
                checkApuesta(player_choice) #Function checks who won the bid
            else:
                print("Debes ingresar una apuesta válida.\nInténtalo nuevamente.")
        else:
            print("Debes ingresar un número entero.\nInténtalo nuevamente.")
    elif player_lives == 0:
        print("Perdiste... lo siento.")
        reset()
    elif machine_lives == 0:
        print("GANASTE!! Felicitaciones.")
        reset()
    else:
        reset()