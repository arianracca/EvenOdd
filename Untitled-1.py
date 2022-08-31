import random

player_lives = int(3)
machine_lives = int(3)
player_choice = 0
apuesta = 0
par = 0
open_game = True

def reset():
    reset = input(print("""Deseas jugar nuevamente?
    1.Si
    Presiona cualquier tecla para salir."""))
    if reset == 1:
        player_lives = 3
        machine_lives = 3
        player_choice = 0
        apuesta = 0
        par = 0
        open_game = True
        return open_game, player_lives, player_choice, machine_lives, apuesta, par
    else:
        open_game = False
        return open_game


def checkParImpar(numero):
    x = int(numero)  # Casting into integer
    x %= 2  # Checking if it's odd or even
    if x == 0:
        par = 2
        print("El número es par!")
    else:
        par = 1
        print("El número es impar!")
    return (par)


def checkApuesta(machine_lives, player_lives, apuesta, par):
    if apuesta == par:
        machine_lives -= 1
        return machine_lives
    else:
        player_lives -= 1
        return player_lives

if player_lives > 0 & machine_lives > 0:
    num1 = input("""Hola!
    Elige un número entero para iniciar.
    (0: Salir)\n""")
    if num1 != "0":
        if num1.isdigit():  # Checking if it's an integer
            machine_num = random.randint(1, 1000)
            print("Tu adversario había elegido: " + machine_num)
            num1 = machine_num + int(num1)
            player_choice = input("""Apuesta!
            1.Impar
            2.Par""")
            if player_choice == 1 | player_choice == 2:
                checkParImpar(num1)
                checkApuesta(machine_lives, player_lives,
                             player_choice, par)
            else:
                print("""Debes ingresar una apuesta válida.
                Inténtalo nuevamente.""")
        else:
            print("""Debes ingresar un número entero.
            Inténtalo nuevamente.""")
    else:
        reset()
elif player_lives <= 0:
    print("Perdiste... lo siento.")
    reset()
elif machine_lives <= 0:
    print("GANASTE!! Felicitaciones.")
    reset()
else:
    reset()
