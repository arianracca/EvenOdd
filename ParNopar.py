def checkParImpar(num1):
    x = int(num1) #Casting into integer
    x%=2 #Checking if it's odd or even
    if x == 0:
        print("El número es par!")
    else:
        print("El número es impar!")

open = True
while open == True:
    num1 = input("Hola! \nElige un número entero para iniciar. (0: Salir)\n")
    if num1 != "0":
        if num1.isdigit(): #Checking if it's an integer
            checkParImpar(num1)
        else:
            print("Debes ingresar un número entero.\nInténtalo nuevamente.")
            break
    else:
        print("Hasta la próxima!")
        open = False
        








