#juego logica booleana
import random
a, b = False, True
def booleano1():
   out = (a and b and not a) or (not b) or (b and a) or (a and not a and not b) 
   print('''
   ¿Cuál es el valor de out de la siguiente lógica?
   out = (a and b and not a) or (not b) or (b and a) or (a and not a and not b)
   ''')
   respuesta1 = input('Escriba la respuesta (False (F) o True (T))').upper() #respuesta: False
   if respuesta1.upper() == 'F':
       print('Respuesta correcta, haz ganado el libro de Física')
       premio_puerta = 'libro de fisica'
       mochila.append(premio_puerta)
   else:
       vidas -= 1/2
       print('Incorrecto pierdes media vida, llevas {vidas} vidas')

def booleano2():
    out = (a and b and a) or (b) or (b or a) or (a and not a and not b)
    print('''
    ¿Cuál es el valor de out de la siguiente lógica?
    out = (a and b and a) or (b) or (b or a) or (a and not a and not b)
    ''')
    respuesta2= input('Escriba la respuesta (False (F) o True (T))').upper() #respuesta: Tre
    if respuesta2.upper() == 'T':
       print('Respuesta correcta, haz ganado el libro de Física')
       premio_puerta = 'libro de fisica'
       mochila.append(premio_puerta)
    else:
       vidas -= 1/2
       print(f'Incorrecto pierdes media vida, llevas {vidas} vidas')

def booleana():
    print('''
    ¡Estas en la puerta!
    Para conseguir el libro de fisica, debes contestar las
    siguientes preguntas
    PRESIONA > PARA CONTINUAR
    ''')
    si = input()
    while si != '>':
       print('''
       ¡Estas en la puerta!
       Para conseguir el libro de fisica, debes contestar las
       siguientes preguntas
       PRESIONA > PARA CONTINUAR
       ''')
       si = input()
    lista = [1,2]
    elegirr = []
    elegir = random.sample(lista,1)
    elegir = str(elegir)
    elegirr.append(elegir)
    elegirr= str(elegirr)
    print(elegirr)
    if elegirr == 1:
        booleano1()
    else:
        booleano2()

