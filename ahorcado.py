import random

AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
palabras = 'metromix rectorado piscina'.split()

 
def buscarPalabraAleat(listaPalabras, mochila):
    # Esta funcion retorna una palabra aleatoria.
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    if palabraAleatoria == 'metromix':
        print('Me encuentro en la entrada de la Universidad')
    elif palabraAleatoria == 'rectorado':
        print('Tienes que subir muchos pisos para llegar a mi')
    elif palabraAleatoria == 'piscina':
        print('Me buscan y nunca me encuentran en la Universidad')
    return listaPalabras[palabraAleatoria]
 
def displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta, mochila):
    print(AHORCADO[len(letraIncorrecta)])
    print ("")
    fin = " "
    print ('Letras incorrectas:', fin)
    for letra in letraIncorrecta:
        print (letra, fin)
    print ("")
    espacio = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)): # Remplaza los espacios en blanco por la letra bien escrita
        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
    for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
        print (letra, fin)
    print ("")
 
def elijeLetra(algunaLetra, mochila):
    # Devuelve la letra que el jugador ingreso. Esta función hace que el jugador ingrese una letra y no cualquier otra cosa
    while True:
        print ('Adivina una letra:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print ('Introduce una sola letra.') 
        elif letra in algunaLetra:
            print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Elije una letra.')
        else:
            return letra
 
def continuar(mochila):
    print('Presiona > para continuar')
    presiona = input()
    biblioteca()
 

def ahorcado(mochila):
    print('''
    ¡Estas en la mueble de libros!
    Para conseguir el cable HDMI debes encontrar
    las palabras
    PRESIONA > PARA CONTINUAR
    ''')
    si = input()
    while si != '>':
       print('''
       ¡Estas en el mueble de libros!
       Para conseguir el cable HDMI, debes encontrar las 
       palabras
       PRESIONA > PARA CONTINUAR
       ''')
       si = input()
    print ('A H O R C A D O')
    letraIncorrecta = ""
    letraCorrecta = ""
    palabraSecreta = buscarPalabraAleat(palabras)
    finJuego = False
    while True:
        displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
        # El usuairo elije una letra.
        letra = elijeLetra(letraIncorrecta + letraCorrecta)
        if letra in palabraSecreta:
            letraCorrecta = letraCorrecta + letra
            # Se fija si el jugador ganó
            letrasEncontradas = True
            for i in range(len(palabraSecreta)):
                if palabraSecreta[i] not in letraCorrecta:
                    letrasEncontradas = False
                    break
            if letrasEncontradas:
                print ('¡Muy bien! La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
                premio_estante = 'cable HDMI'
                mochila['premio'].append(premio_estante)
                finJuego = True
        else:
            letraIncorrecta = letraIncorrecta + letra
            mochila["vidas"] -= - 1/4
            # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
            if len(letraIncorrecta) == len(AHORCADO) - 1:
                displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
                print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
                print(f'Te quedan {mochila["vidas"]} vidas')
                finJuego = True
        # Pregunta al jugador si quiere jugar de nuevo
        if finJuego:
            if continuar(mochila):
                letraIncorrecta = ""
                letraCorrecta = ""
                finJuego = False
                palabraSecreta = buscarPalabraAleat(palabras)
            else:
                break

