
vidas = []
numero_vidas = 5
lista = [1,2,3]
import random

def palabra1():
    print('Las siguientes palabras son de la categoria COCINA')
    #primeras palabras
    sarten = list('sarten')
    random.shuffle(sarten)
    print (''.join(sarten))
    respuesta_sarten = input('Ordena las letras para formar una palabra con sentido')
    if respuesta_sarten == 'sarten' or respuesta_sarten == 'SARTEN' or respuesta_sarten == 'Sarten':
            print('¡Buen trabajo, respuesta correcta!')
    else:
        print('respuesta incorrecta, haz perdido media vida')
        vidas.append(respuesta_sarten)
    
    paleta = list('paleta')
    random.shuffle(paleta)
    print (''.join(paleta))
    respuesta_paleta = input('Ordena las letras para formar una palabra con sentido')
    if respuesta_paleta == 'paleta' or respuesta_paleta == 'Paleta' or respuesta_paleta == 'PALETA':
        print('¡Buen trabajo, respuesta correcta!')
    else:
        print('respuesta incorrecta, haz perdido media vida')
        vidas.append(respuesta_paleta)
    
    olla = list('olla')
    random.shuffle(olla)
    print (''.join(olla))
    respuesta_olla = input('Ordena las letras para formar una palabra con sentido')
    if respuesta_olla == 'olla' or respuesta_olla == 'OLLA' or respuesta_olla == 'Olla':
        print('¡Buen trabajo, respuesta correcta!')
    else:
        print('respuesta incorrecta, haz perdido media vida')
        vidas.append(respuesta_olla)
    
    vaso = list('vaso')
    random.shuffle(vaso)
    print (''.join(vaso))
    respuesta_vaso = input('Ordena las letras para formar una palabra con sentido')
    if respuesta_vaso == 'vaso' or respuesta_vaso == 'Vaso' or respuesta_vaso == 'VASO':
        print('¡Buen trabajo, respuesta correcta!')
    else:
        print('respuesta incorrecta, haz perdido media vida')
        vidas.append(respuesta_vaso)
    
    hornilla = list('hornilla')
    random.shuffle(hornilla)
    print (''.join(hornilla))
    respuesta_hornilla = input('Ordena las letras para formar una palabra con sentido')
    if respuesta_hornilla == 'hornilla' or respuesta_hornilla == 'HORNILLA' or respuesta_hornilla == 'Hornilla':
        print('¡Buen trabajo, respuesta correcta!')
    else:
        print('respuesta incorrecta, haz perdido media vida')
        vidas.append(respuesta_hornilla)
    numero_vidas= int(numero_vidas)
    vidas1 = len(vidas)
    total = numero_vidas - vidas1
    
    if total < -1:
        print('Usted, ha pedido debido a que tiene ' + str(total) + ' de vidas')
    else:
        print('Buen trabajo, ha ganado la contraseña, tiene un total de ' + str(total) + ' vidas')

#segundas palabras

def palabra2():
    print('Las siguientes palabras son de la categoria BAÑO')
    
    poceta = list('poceta')
    random.shuffle(poceta)
    print (''.join(poceta))
    respuesta_poceta = input('Ordena las letras para formar una palabra con sentido')
    if respuesta_poceta == 'poceta' or respuesta_poceta == 'POCETA' or respuesta_poceta == 'Poceta':
            print('¡Buen trabajo, respuesta correcta!')
    else:
        print('respuesta incorrecta, haz perdido media vida')
        vidas.append(respuesta_poceta)
    
    cepillo = list('cepillo')
    random.shuffle(cepillo)
    print (''.join(cepillo))
    respuesta_cepillo = input('Ordena las letras para formar una palabra con sentido')
    if respuesta_cepillo == 'cepillo' or respuesta_poceta == 'Cepillo' or respuesta_paleta == 'CEPILLO':
        print('¡Buen trabajo, respuesta correcta!')
    else:
        print('respuesta incorrecta, haz perdido media vida')
        vidas.append(respuesta_cepillo)
    
    afeitadora = list('afeitadora')
    random.shuffle(afeitadora)
    print (''.join(afeitadora))
    respuesta_afeitadora = input('Ordena las letras para formar una palabra con sentido')
    if respuesta_afeitadora == 'afeitadora' or respuesta_afeitadora == 'AFEITADORA' or respuesta_afeitadora == 'Afeitadora':
        print('¡Buen trabajo, respuesta correcta!')
    else:
        print('respuesta incorrecta, haz perdido media vida')
        vidas.append(respuesta_afeitadora)
    
    regadera = list('regadera')
    random.shuffle(regadera)
    print (''.join(regadera))
    respuesta_regadera = input('Ordena las letras para formar una palabra con sentido')
    if respuesta_regadera == 'regadera' or respuesta_regadera == 'Regadera' or respuesta_vaso == 'REGADERA':
        print('¡Buen trabajo, respuesta correcta!')
    else:
        print('respuesta incorrecta, haz perdido media vida')
        vidas.append(respuesta_regadera)
    
    grifo = list('grifo')
    random.shuffle(grifo)
    print (''.join(grifo))
    respuesta_grifo = input('Ordena las letras para formar una palabra con sentido')
    if respuesta_grifo == 'grifo' or respuesta_grifo == 'GRIFO' or respuesta_grifo == 'Grifo':
        print('¡Buen trabajo, respuesta correcta!')
    else:
        print('respuesta incorrecta, haz perdido media vida')
        vidas.append(respuesta_grifo)
    
    numero_vidas= int(numero_vidas)
    vidas1 = len(vidas)
    total = numero_vidas - vidas1
    
    if total < -1:
        print('Usted, ha pedido debido a que tiene ' + str(total) + ' de vidas')
    else:
        print('Buen trabajo, ha ganado la contraseña, tiene un total de ' + str(total) + ' vidas')

#tercera palabra
def palabra3():
    print('Las siguientes palabras son de la categoria BAILE')
    
    zumba = list('zumba')
    random.shuffle(zumba)
    print (''.join(zumba))
    respuesta_zumba = input('Ordena las letras para formar una palabra con sentido')
    if respuesta_zumba == 'zumba' or respuesta_zumba == 'ZUMBA' or respuesta_zumba == 'Zumba':
            print('¡Buen trabajo, respuesta correcta!')
    else:
        print('respuesta incorrecta, haz perdido media vida')
        vidas.append(respuesta_zumba)
    
    salsa = list('salsa')
    random.shuffle(salsa)
    print (''.join(salsa))
    respuesta_salsa = input('Ordena las letras para formar una palabra con sentido')
    if respuesta_salsa == 'salsa' or respuesta_salsa == 'Salsa' or respuesta_salsa == 'SALSA':
        print('¡Buen trabajo, respuesta correcta!')
    else:
        print('respuesta incorrecta, haz perdido media vida')
        vidas.append(respuesta_salsa)
    
    flamengo = list('flamengo')
    random.shuffle(flamengo)
    print (''.join(flamengo))
    respuesta_flamengo = input('Ordena las letras para formar una palabra con sentido')
    if respuesta_flamengo == 'flamengo' or respuesta_afeitadora == 'FLAMENGO' or respuesta_afeitadora == 'Flamengo':
        print('¡Buen trabajo, respuesta correcta!')
    else:
        print('respuesta incorrecta, haz perdido media vida')
        vidas.append(respuesta_flamengo)
    
    tango = list('tango')
    random.shuffle(tango)
    print (''.join(tango))
    respuesta_tango = input('Ordena las letras para formar una palabra con sentido')
    if respuesta_tango == 'tango' or respuesta_tango == 'Tango' or respuesta_tango == 'TANGO':
        print('¡Buen trabajo, respuesta correcta!')
    else:
        print('respuesta incorrecta, haz perdido media vida')
        vidas.append(respuesta_tango)
    
    perreo = list('perreo')
    random.shuffle(perreo)
    print (''.join(perreo))
    respuesta_perreo = input('Ordena las letras para formar una palabra con sentido')
    if respuesta_perreo == 'perreo' or respuesta_perreo == 'PERREO' or respuesta_perreo == 'Perreo':
        print('¡Buen trabajo, respuesta correcta!')
    else:
        print('respuesta incorrecta, haz perdido media vida')
        vidas.append(respuesta_perreo)
        
    numero_vidas= int(numero_vidas)
    vidas1 = len(vidas)
    total = numero_vidas - vidas1
    
    if total < -1:
        print('Usted, ha pedido debido a que tiene ' + str(total) + ' de vidas')
    else:
        print('Buen trabajo, ha ganado la contraseña, tiene un total de ' + str(total) + ' vidas')
    





def palabra_mezclada():
    print('''
    ¡Estas en el rack!
    Para conseguir la contraseña debes ordenar las siguientes palabras
    PRESIONA > PARA CONTINUAR
    ''')
    si = input()
    while si != '>':
        print('''
         ¡Estas en el rack!
         Para conseguir la contraseña debes ordenar las siguientes palabras
         PRESIONA > PARA CONTINUAR
        ''')
        si = input()
    
    elegir = random.randint(1,3)
 
    if elegir == 1:
        palabra1()
    elif elegir == 2:
        palabra2()
    elif elegir == 3:
        palabra3()

