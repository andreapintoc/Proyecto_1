import random


abc = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
matriz_abc = [None] * (15)

palabra1 = ['p','i','l','a','r']
palabra2 = ['a', 'r','d', 'i', 'l', 'a']
palabra3 = ['s','c','h','a','r','i','f','k','e','r'] 
palabra4 = 'bello'
palabra5 ='marcano'
palabra6 ='dagama'
palabra7='boada'
palabra8='llorante'
palabra9='dagama'

def sopa(mochila):
    for i in range(len(palabra1)):
        matriz_abc[i][0] = palabra1[i];
    
    for i in range(len(palabra2)):
        matriz_abc[i][4+i] = palabra2[i];
    
    for i in range(len(palabra3)):
        matriz_abc[14][5+i] = palabra3[i];
    
    for fila in matriz_abc:
        print(fila)
    pistas = input('Desea una pista S o N: ').upper()
    if pistas.upper() == 's':
        print('''
        "apellido directora de escuela de sistemas",
        "apellido jefe del CeTIC",
        "apellido rector Unimet
        ''')
    respuesta=input('Indique las palabras encontradas:')
    if respuesta == 'ardila' or respuesta == 'pilar' or respuesta == 'scharifker':
        print('Respuesta correcta, te haz ganado una vida extra')
        mochila["vidas"] += 1
        print(f'te quedan {mochila["vidas"]} vidas')
    else:
        print('Respuesta Incorrecta pierdes media vida')
        mochila["vidas"] -= 1/2
        print(f'te quedan {mochila["vidas"]} vidas')


def sopa2(mochila):
    for i in range(len(palabra4)):
        matriz_abc[i][0] = palabra4[i];
    
    for i in range(len(palabra5)):
        matriz_abc[i][2+i] = palabra5[i];
    
    for i in range(len(palabra6)):
        matriz_abc[6][2+i] = palabra6[i];
    
    for fila in matriz_abc:
        print(fila)

    pistas = input('Desea una pista S o N: ').upper()
    if pistas.upper() == 's':
        print('''
         "apellido directora de escuela de sistemas",
         "apellido jefe del CeTIC",
         "apellido rector Unimet
        ''')
    respuesta=input('Indique las palabras encontradas:')
    if respuesta == 'bello' or respuesta == 'marcano' or respuesta == 'dagama':
        print('Respuesta correcta, te haz ganado una vida extra')
        mochila["vidas"] += 1
        print(f'te quedan {mochila["vidas"]} vidas')
    else:
        print('Respuesta Incorrecta pierdes media vida')
        mochila["vidas"] -= 1/2
        print(f'te quedan {mochila["vidas"]} vidas')
    
def sopa3(mochila):
    for i in range(len(palabra7)):
        matriz_abc[i][9] = palabra7[i];
    
    for i in range(len(palabra8)):
        matriz_abc[i][1+i] = palabra8[i];
    
    for i in range(len(palabra9)):
        matriz_abc[12][3+i] = palabra9[i];
    
    for fila in matriz_abc:
        print(fila)
    
    pistas = input('Desea una pista S o N: ').upper()
    if pistas.upper() == 's':
        print('''
        "apellido del coronel de Seguridad de la Unimet",
        "apellido del presidente de la FCE-UNIMET ",
        "apellido de Vicerrectora Académica de la Unimet
        ''')
    respuesta=input('Indique las palabras encontradas:')
    if respuesta == 'lloante' or respuesta == 'boada' or respuesta == 'dagama':
        print('Respuesta correcta, te haz ganado una vida extra')
        mochila["vidas"] += 1
        print(f'te quedan {mochila["vidas"]} vidas')
    else:
        print('Respuesta Incorrecta pierdes media vida')
        mochila["vidas"] -= 1/2
        print(f'te quedan {mochila["vidas"]} vidas')


def matriz(mochila):
    for i in range(0, 15):
        matriz_abc[i] = [None] * 15

    for i in range(15):
        for j in range(15):
            matriz_abc[i][j] = abc[random.randint(0,25)]
    lista = [1,2,3]
    elegirr=[]
    elegir = random.sample(lista,1)
    elegirr.append(elegir)
    print(elegirr)
    if elegirr == 1:
         sopa3(mochila)
    elif elegirr == 2:
         sopa2(mochila)
    else:
         sopa(mochila)



