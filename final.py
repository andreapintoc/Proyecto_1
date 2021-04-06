import random
lista = [1,2,3]
def juego1(mochila):
#pregunta uno
    print('''
    ¿El lenguaje de programacion Python, se caracteriza por usar un lenguaje parecido a..,
    1. Aleman
    2. Español
    3. Ingles
    4. Portugues
    ''')
    respuesta_uno = input('''
    - Coloca el numero de la respuesta correcta
    - Coloca 0 (CERO) para una pista
    ''')
    while respuesta_uno != '1' and respuesta_uno != '2' and respuesta_uno != '3' and respuesta_uno != '4' and respuesta_uno != '0':
        print('''
         ¿El lenguaje de programacion Python, se caracteriza por usar un lenguaje parecido a..,
         1. Aleman
         2. Español
         3. Ingles
         4. Portugues
        ''')
        respuesta_uno = input('''
        - Coloca el numero de la respuesta correcta
        - Coloca 0 (CERO) para una pista
        ''')
    if respuesta_uno == '0':
        print('Uno e los idiomas mas importantes')
        print('''
        ¿El lenguaje de programacion Python, se caracteriza por usar un lenguaje parecido a..,
        1. Aleman
        2. Español
        3. Ingles
        4. Portugues
        ''')
        respuesta_uno = input('''
        - Coloca el numero de la respuesta correcta
        ''')
        if respuesta_uno == '3':
            print('Respuesta correcta, GANASTE')
        else:
            print('Respuesta incorrecta, pierdes una vida')

    elif respuesta_uno == '3':
        print('Respuesta correcta, GANASTE')

    else:
        print('Respuesta incorrecta, pierdes una vida')
        mochila['vidas'] -= 1/2
        print(f'Te quedan {mochila["vidas"]} vidas')

def juego2(mochila):
# pregunta dos
    print('''
     ¿En qué año aparecio Python?,
      1. 1990
      2. 2001
      3. 1980
      4. 1991
    ''')
    respuesta_dos = input('''
    - Coloca el numero de la respuesta correcta
    - Coloca 0 (CERO) para una pista
    ''')
    while respuesta_dos != '1' and respuesta_dos != '2' and respuesta_dos != '3' and respuesta_dos != '4' and respuesta_dos != '0':
        print('''
        ¿En qué año aparecio Python?,
         1. 1990
         2. 2001
         3. 1980
         4. 1991
           ''')
        respuesta_dos = input('''
        - Coloca el numero de la respuesta correcta
        - Coloca 0 (CERO) para una pista
        ''')
    if respuesta_dos == '0':
        print('Termina en 0 el año"')
        print('''
         ¿En qué año aparecio Python?,
          1. 1990
          2. 2001
          3. 1980
          4. 1991
            ''')
        respuesta_dos = input('''
        - Coloca el numero de la respuesta correcta
        ''')
        if respuesta_dos == '4':
            print('Respuesta correcta, HAZ GANADO')
        else:
            print('Respuesta incorrecta, pierdes una vida')

    elif respuesta_dos == '4':
        print('Respuesta correcta, HAZ GANADO')

    else:
        print('Respuesta incorrecta, pierdes una vida')
        mochila['vidas'] -= 1/2
        print(f'Te quedan {mochila["vidas"]} vidas')
    
def juegoquizzi(mochila):
    print('''
    ¡te encuentas en el Banco 1
    Contesta estas preguntas en menos de un minutos para conseguir
    ganar

    PRESIONA > PARA EMPEZAR
    ''')
    si = input()
    while si != '>':
        print('''
        ¡Estas en la computadora 2!
        Debes de conseguir la contraseña, contestando estas adivinanzas
        ¿Estas listo?
        PRESIONA > PARA CONTINUAR
        ''')
        si = input()

    elegir = random.sample(lista,1)

    if elegir == 1:
        juego1(mochila)
    else: 
        juego2(mochila)
