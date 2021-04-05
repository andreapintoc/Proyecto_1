import random
abc = 'abcdefghijklmnopqrstuvwxyz'

def desplazamiento2():
    print('''
    ENCUENTRA EL MENSAJE ENCRIPTADO
    ABECEDARIO : ABCDEFGHIJKLMNÑOPQRSTUVWXYZ
    ABECEDARIO ENCRIPTADO: YZABCDEFGHIJKLMNOPQRSTUVWX 
    ''')
    texto=('Si te graduas pisas el saman').upper()
    clave=3
    abc= ('abcdefghijklmnopqrstuvwxyz').upper()
    longitud=len(texto);
    for i in range (0,longitud):
      for pos in range (0,26):
        if texto[i]==abc[pos]:
          pos_abc=pos-(int(clave))
          if pos_abc >-1:
             print(abc[pos_abc],end='')
          if pos_abc <0 :
             print(abc[pos_abc%26],end='')
      else:
        print(end='')
    print('\n')
    respuesta =(str(input('Indique la frase cifrada: ')))
    if respuesta != 'si te graduas pisas el saman':
        print('Incorrecto, pierdes una vida')
        vidas = vidas - 1
    else:
        print('Haz encontrado el mensaje secreto')
        premio_gavetero = 'mensaje'
        mochila.append(premio_gavetero)

def desplazamiento4():
    print('''
    ENCUENTRA EL MENSAJE ENCRIPTADO
    ABECEDARIO : ABCDEFGHIJKLMNÑOPQRSTUVWXYZ
    ABECEDARIO ENCRIPTADO: WXYZABCDEFGHIJKLMNOPQRSTUV
    ''')
    texto='Si te graduas pisas el saman'.upper()
    clave=4
    abc= ('abcdefghijklmnopqrstuvwxyz').upper()
    longitud=len(texto);
    for i in range (0,longitud):
      for pos in range (0,26):
        if texto[i]==abc[pos]:
          pos_abc=pos-(int(clave))
          if pos_abc >-1:
             print(abc[pos_abc],end='')
          if pos_abc <0 :
             print(abc[pos_abc%26],end='')
      else:
        print(end=' ')
    print('\n')
    respuesta =(str(input('Indique la frase cifrada: ')))
    if respuesta != 'si te graduas pisas el saman':
        print('Incorrecto, pierdes una vida')
        vidas = vidas - 1
        print(f'te quedan {vidas} vidas')
    else:
        print('Haz encontrado el mensaje secreto')
        premio_gavetero = 'mensaje'
        mochila.append(premio_gavetero)

def desplazamiento5():
    print('''
    ENCUENTRA EL MENSAJE ENCRIPTADO
    ABECEDARIO : ABCDEFGHIJKLMNÑOPQRSTUVWXYZ
    ABECEDARIO ENCRIPTADO: VWXYZABCDEFGHIJKLMNOPQRSTU
    ''')
    texto=('Si te graduas pisas el saman').upper()
    clave=5
    abc= ('abcdefghijklmnopqrstuvwxyz').upper()
    longitud=len(texto);
    for i in range (0,longitud):
      for pos in range (0,26):
        if texto[i]==abc[pos]:
          pos_abc=pos-(int(clave))
          if pos_abc >-1:
             print(abc[pos_abc],end='')
          if pos_abc <0 :
             print(abc[pos_abc%26],end='')
      else:
        print(end=' ' )
    print('\n')
    respuesta =(str(input('Indique la frase cifrada: ')))
    if respuesta != 'si te graduas pisas el saman':
        print('Incorrecto, pierdes una vida')
        vidas = vidas - 1
        print(f'te quedan {vidas} vidas')
    else:
        print('Haz encontrado el mensaje secreto')
        premio_gavetero = 'mensaje'
        mochila.append(premio_gavetero)

def criptograma():
    print('''
      ¡Estas en eel mueble de gavetas!
      Para obtener el mensaje,
      debes decifrar el mensaje encriptado
      PRESIONA > PARA CONTINUAR
      ''')
    si = input()
    while si != '>':
        print('''
        ¡Estas en eel mueble de gavetas!
        Para obtener el mensaje,
        debes decifrar el mensaje encriptado
        PRESIONA > PARA CONTINUAR
        ''')
        si = input()
    print('La utilidad de este programa consiste en cifrar o descifrar el texto que introduzca mediante el método César')
    lista = [1,2,3]
    elegirr = []
    elegir = random.sample(lista,1)
    elegirr.append(elegir)
    print(elegirr)
    if elegirr == 1:
         desplazamiento2()
    elif elegirr == 2:
         desplazamiento4()
    else:
         desplazamiento5()
