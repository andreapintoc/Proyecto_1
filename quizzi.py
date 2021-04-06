import random
lista = [1,2,3]
def pregunta1(mochila):
#pregunta uno
    print('''
    ¿En qué fecha es el Aniversario de la Universidad Metropolitana?",
    1. 22 de octubre
    2. 22 de septiembre
    3. 25 de octubre
    4. 25 de septiembre
    ''')
    respuesta_uno = input('''
    - Coloca el numero de la respuesta correcta
    - Coloca 0 (CERO) para una pista
    ''')
    while respuesta_uno != '1' and respuesta_uno != '2' and respuesta_uno != '3' and respuesta_uno != '4' and respuesta_uno != '0':
        print('''
        ¿En qué fecha es el Aniversario de la Universidad Metropolitana?",
        1. 22 de octubre
        2. 22 de septiembre
        3. 25 de octubre
        4. 25 de septiembre
        ''')
        respuesta_uno = input('''
        - Coloca el numero de la respuesta correcta
        - Coloca 0 (CERO) para una pista
        ''')
    if respuesta_uno == '0':
        print('Es en octubre')
        print('''
        ¿En qué fecha es el Aniversario de la Universidad Metropolitana?",
        1. 22 de octubre
        2. 22 de septiembre
        3. 25 de octubre
        4. 25 de septiembre
        ''')
        respuesta_uno = input('''
        - Coloca el numero de la respuesta correcta
        ''')
        if respuesta_uno == '1':
            print('Respuesta correcta, te haz ganado el LIBRO DE MATEMATICA')
        else:
            print('Respuesta incorrecta, pierdes una vida')
            mochila['vidas'] -= 1/2

    elif respuesta_uno == '1':
        print('Respuesta correcta, te haz ganado el LIBRO DE MATEMATICA')

    else:
        print('Respuesta incorrecta, pierdes una vida')
        mochila['vidas'] -= 1/2
        print(f'Te quedan {mochila["vidas"]} vidas')

def pregunta2(mochila):
# pregunta dos
    print('''
     ¿En qué año fue Fundada la Universidad Metropolitana?,
      1. 1979
      2. 1969
      3. 1980
      4. 1970
    ''')
    respuesta_dos = input('''
    - Coloca el numero de la respuesta correcta
    - Coloca 0 (CERO) para una pista
    ''')
    while respuesta_dos != '1' and respuesta_dos != '2' and respuesta_dos != '3' and respuesta_dos != '4' and respuesta_dos != '0':
        print('''
        ¿En qué año fue Fundada la Universidad Metropolitana?,
        1. 1979
        2. 1969
        3. 1980
        4. 1970
        ''')
        respuesta_dos = input('''
        - Coloca el numero de la respuesta correcta
        - Coloca 0 (CERO) para una pista
        ''')
    if respuesta_dos == '0':
        print('Termina en 0 el año"')
        print('''
        ¿En qué año fue Fundada la Universidad Metropolitana?,
        1. 1979
        2. 1969
        3. 1980
        4. 1970
        ''')
        respuesta_dos = input('''
        - Coloca el numero de la respuesta correcta
        ''')
        if respuesta_dos == '4':
            print('Respuesta correcta, te haz ganado el LIBRO DE MATEMATICA')
        else:
            print('Respuesta incorrecta, pierdes una vida')
            mochila['vidas'] -= 1/2

    elif respuesta_dos == '4':
        print('Respuesta correcta, te haz ganado el LIBRO DE MATEMATICA')

    else:
        print('Respuesta incorrecta, pierdes una vida')
        mochila['vidas'] -= 1/2
        print(f'Te quedan {mochila["vidas"]} vidas')

def pregunta3(mochila):
#pregunta tres
    print('''
    ¿Quién fundó la Unimet?
    1. Rafael Matiezo 
    2. Lorenzo Mendoza
    3. Eugenio Mendoza
    4. Luis Miguel Da Gama
    ''')
    respuesta_tres = input('''
    - Coloca el numero de la respuesta correcta
    - Coloca 0 (CERO) para una pista
    ''')
    while respuesta_tres != '1' and respuesta_tres != '2' and respuesta_tres != '3' and respuesta_tres != '4' and respuesta_tres != '0':
        print('''
        ¿Quién fundó la Unimet?
        1. Rafael Matiezo 
        2. Lorenzo Mendoza
        3. Eugenio Mendoza
        4. Luis Miguel Da Gama
        ''')
        respuesta_tres = input('''
        - Coloca el numero de la respuesta correcta
        - Coloca 0 (CERO) para una pista
        ''')
    if respuesta_tres == '0':
        print("Tiene una estatua")
        print('''
        ¿Quién fundó la Unimet?
        1. Rafael Matiezo 
        2. Lorenzo Mendoza
        3. Eugenio Mendoza
        4. Luis Miguel Da Gama
        ''')
        respuesta_tres = input('''
        - Coloca el numero de la respuesta correcta
        ''')
        if respuesta_tres == '3':
            print('Respuesta correcta, te haz ganado el LIBRO DE MATEMATICA')
        else:
            print('Respuesta incorrecta, pierdes una vida')
            mochila['vidas'] -= 1/2
        
    elif respuesta_tres == '3':
        print('Respuesta correcta, te haz ganado el LIBRO DE MATEMATICA')
    
    else:
        print('Respuesta incorrecta, pierdes una vida')
        mochila['vidas'] -= 1/2
        print(f'Te quedan {mochila["vidas"]} vidas')
    
def quizzi(mochila):
    print('''
    ¡te encuentas en el Banco 1
    Contesta estas preguntas en menos de un minutos para conseguir
    el libro de matematicas

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
        pregunta1(mochila)
    elif elegir == 2:
        pregunta2(mochila)
    else: 
        pregunta3(mochila)
