import random
open_game = True
player_life = 3
machine_life = 3
par = 0

def menu(): #Menu for Starting new game, continue a started game or exit.
    print("Deseas jugar 'Cho Han'?\n1.Nueva Partida\n2.Continuar partida\nSalir (Cualquier tecla)")
    reset = input()
    if reset == "1":
        global player_life, machine_life
        player_life = 3
        machine_life = 3
    elif reset == "2":
        pass
    else:
        print("Hasta la próxima!")
        exit()

def checkParImpar(num1): #Function checks if Total number is Even or Odd
    global par
    x = int(num1)
    x%=2 #Checking if it's odd or even
    if x == 0:
        par = 2
        print("El resultado es PAR!")
    else:
        par = 1
        print("El resultado es IMPAR!")
    return par

def checkApuesta(player_choice, par): #Function checks who won the bid
    global machine_life, player_life
    if int(player_choice) == int(par):
        machine_life -= 1
        print("--- GANASTE LA RONDA! ---")
    else:
        player_life -= 1
        print("--- PERDISTE LA RONDA ---")

print("""Bienvenido al juego 'Cho Han' digital simplificado.
Para esta adaptación tú elegirás un número que te guste jugar
y tu adversario (la PC) elegirá otro número al azar entre 1 y 100.
Tú sólo sabrás tu elección hasta que elijas si Apuestas por que el
resultado de la suma de ambos números será Par o Impar.
Cada jugador puede equivocarse 3 veces antes de perder.""")

while open_game == True:

    if (player_life > 0) and (machine_life > 0): #Check player and machine still alive
        menu()
        print("Tus oportunidades: "+str(player_life))
        print("Las del adversario: "+str(machine_life))
        num0 = input("Elige un número entero para jugar.\n") #Player choose the number is playing

        if num0.isdigit(): #Checking if it's a correct integer number
            player_choice = input("Apuesta! 1.Impar - 2.Par\n") #Player choose Even or Odd

            if player_choice == "1" or player_choice == "2":
                machine_num = random.randint(1,100) #Machine randomize the number is playing
                num1 = int(machine_num) + int(num0) #Total number on play is calculated
                print("ELEGISTE: "+str(num0)+"\nTU ADVERSARIO ELIGIÓ: "+str(machine_num)+
                "\nEL NÚMERO FINAL ES..."+str(num1)+"\n")
                checkParImpar(num1) #Function checks if Total number is Even or Odd
                checkApuesta(player_choice,par) #Function checks who won the bid

            else:
                print("Debes ingresar una apuesta válida.\nInténtalo nuevamente.")

        else:
            print("Debes ingresar un número entero.\nInténtalo nuevamente.")

    elif player_life == 0:
        print("PERDISTE... lo siento.")
        menu()

    elif machine_life == 0:
        print("--------- GANASTE!! ---------\n--|F|E|L|I|C|I|T|A|C|I|O|N|E|S|--.")
        menu()

    else:
        menu()