

def python1():
    pregunta1 = eval(input('Tengo el siguiente string: frase  = \"tengo en mi cuenta 50,00 $\". Escribe en una línea de código como extraer de este string los 50 en formato entero'))
    print(pregunta1)
    if pregunta1 == '50.00':
        print('Respuesta correcta')
        premio_compu1 = 'carnet'
        mochila.append(premio_compu1)
    else:
        print('Respuesta Incorrecta')
        print('pista: "utiliza replace", "utiliza split", "utiliza int"')
        return pregunta1

def python2():
    pregunta2 = eval(input("Invierte este string con python en un línea  para poder leerlo frase = \"oidutse ne al ortem aireinegni ed sametsis\""))
    print(pregunta2)
    if pregunta1 == 'estudio en a metro ingenieria en sistemas':
        print('Respuesta correcta')
        mochila.append(premio_compu1)
    else:
        print('Respuesta Incorrecta')
        print('utiliza slices')
        return pregunta2



#hola = '355.157'
#user_input = eval(input(f'Escribe el codigo en python para cambiar el punto . por , en la siguiente numero: \n (la variable del numero se llama hola) {hola} =>'))
#print(user_input)






def python():
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

    elegir = random.sample(lista,1)

    if elegir == 1:
        python1()
    else: 
        python2()
