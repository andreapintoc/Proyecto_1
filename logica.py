import random
def logica1(mochila):
    #β° vale 3 π vale 4 π§‘ vale 15
    print('π§‘+π§‘+π§‘=45 \n π+π+π§‘=23 \n π+β°+β°=10 \n β°+π+πxπ§‘=?')
    respuesta1 = input('cual sera el valor? ')
    if respuesta1 == '67' or respuesta1 == 'sesenta y siete':
        print('Respuesta correcta, haz ganado el DISCO DURO')
    else:
        print('Respuesta incorrecta, pierdes una vida')

def logica2():
    #π vale 5 π§vale 9 π¦vale 4
    print('π§+π§+π§=27 \n π§+π+π=19 \n π+π¦+π¦=13 \n πxπ§-π¦=?')
    respuesta2 = input('cual sera el valor? ')
    if respuesta2 == '25' or respuesta2 == 'veinticinco':
        print('Respuesta correcta, haz ganado el DISCO DURO')
    else:
        print('Respuesta incorrecta, pierdes una vida')

def logica(mochila):
    print('''
    Β‘Estas en en Saman!
    Para obtener el disco duro,
    debes encontrar la logica
    PRESIONA > PARA CONTINUAR
    ''')
    si = input()
    while si != '>':
       print('''
       Β‘Estas en en Saman!
       Para obtener el disco duro,
       debes encontrar la logica
       PRESIONA > PARA CONTINUAR
       ''')
       si = input()
    lista = ['1','2']
    elegirr = []
    elegir = random.sample(lista,1)
    elegir = str(elegir)
    elegirr.append(elegir)
    elegirr= str(elegirr)
    print(elegirr)
    if elegirr == '1':
        logica1(mochila)
    else:
        logica2(mochila)
