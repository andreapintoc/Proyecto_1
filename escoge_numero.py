import random

def escoge_numero():
    intentos = 0
    num_max = 15
    num_min = 1

    print('¡Estas en la papelera, y te ha tocado el juego de ESCOGE UN NUMERO!')
    numero = random.randint(num_min, num_max)
    print('Debes decirme en que numero estoy pensando entre ' + str(num_min) + ' y ' + str(num_max))

    while intentos < 3:
        adivina =input('Adivina el numero:')
        adivina = int(adivina)
        intentos += 1

        if adivina  < numero:
            print('Tu numero es muy bajo')
        elif adivina > numero:
            print('Tu numero es muy alto')
        elif adivina == numero:
            break
    if adivina == numero:

        print('Buen trabajo, ¡Adivinaste!, haz optenido el TITULO UNIVERSITARIO ')
    elif adivina != numero:
        numero = int(numero)
        print('No es correcto, perdiste un cuarto de vida, intentalo de nuevo, es numero era ' + str(numero))
        #return 
    #if intento > numero_vida:
    #    print('LO SIENTO, TE QUEDASTE SIN VIDAS')
     #   break   
