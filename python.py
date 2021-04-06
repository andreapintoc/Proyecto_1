

def python1(mochila):
    pregunta1 = eval(input('Tengo el siguiente string: frase  = \"tengo en mi cuenta 50,00 $\". Escribe en una línea de código como extraer de este string los 50 en formato entero'))
    print(pregunta1)
    if pregunta1 == '50.00':
        print('Respuesta correcta')
        premio_compu1 = 'carnet'
        mochila['premio'].append(premio_compu1)
    else:
        print('Respuesta Incorrecta')
        print('pista: "utiliza replace", "utiliza split", "utiliza int"')
        mochila['vidas'] -= 1/2
    print(f'Tines un total de {mochila["vidas"]} vidas')

def python2(mochila):
    pregunta2 = eval(input("Invierte este string con python en un línea  para poder leerlo frase = \"oidutse ne al ortem aireinegni ed sametsis\""))
    print(pregunta2)
    if pregunta1 == 'estudio en a metro ingenieria en sistemas':
        print('Respuesta correcta')
        mochila['premio'].append(premio_compu1)
    else:
        print('Respuesta Incorrecta')
        print('pista: "utiliza slices"')
        mochila['vidas'] -= 1/2
        
    print(f'Tines un total de {mochila["vidas"]} vidas')








def python(mochila):
    print('''
    ¡te encuentas en la computadora 1!
    Resuelve las siguientes preguntas python

    PRESIONA > PARA EMPEZAR
    ''')
    si = input()
    while si != '>':
        print('''
        ¡te encuentas en la computadora 1!
        Resuelve las siguientes preguntas python

        PRESIONA > PARA EMPEZAR
        ''')
        si = input()

    elegir = random.randint(1,3)

    if elegir == 1:
        python1(mochila)
    else: 
        python2(mochila)
