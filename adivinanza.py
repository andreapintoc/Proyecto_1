
import random
lista = [1,2,3]


def adivinanza1():
   pistas1 = ['Lo usas cuando se va la luz', 'Lo puedes prender con un encendedor', 'Es de cera']
   pistas2 = ["lo usas cuando hay luz", "gracias a estar encendido puedes leer", "se coloca en las lámparas"]
   pistas3 = ["fruta", "POTASIO", "parecido al plátano"]
   print('''
   ¡Estas en la computadora 2!
   Contesta estas adivinanzas para conseguir la llave
   ¿Estas listo?
   PRESIONA > PARA CONTINUAR
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
   print('Soy alta cuando soy joven y baja cuando soy vieja. ¿Qué soy yo? : ')
   pregunta_uno = input('''
   -Escriba la respuesta 
   -Coloque 0 (cero) para una pista
   ''')
   
   if pregunta_uno == '0':
       for i in range(1):
           print(random.choice(pistas1))
       pregunta_uno= input('''
       Soy alta cuando soy joven y baja cuando soy vieja. ¿Qué soy yo? : 
       -Escriba la respuesta 
       -Coloque 0 (cero) para una pista
       ''') 
   elif pregunta_uno != "una vela" or pregunta_uno != "vela" or pregunta_uno != "Vela" or pregunta_uno != "la Vela" or pregunta_uno or pregunta_uno !="La Vela" :  
       print('Respuesta incorrecta, pierdes una vida')
       vidas = vidas - 1/2
       print(' Te quedan ' + str(vidas) + ' vidas')
    
   
   else:
       print('¡Buen trabajo!, Respuesta correcta, te has ganado la LLAVE')
       premio_compu2 = 'llave'
       mochila.append(premio_compu2)
       
#    if pregunta_uno == '0':
#        print('Lo puedes prender con un encendedor')
#        pregunta_uno= input('''
#        Soy alta cuando soy joven y baja cuando soy vieja. ¿Qué soy yo? : 
#        -Escriba la respuesta 
#        -Coloque 0 (cero) para una pista
#        ''')
#    elif pregunta_uno == "una vela" or pregunta_uno == "vela" or pregunta_uno == "Vela" or pregunta_uno == "la Vela" or pregunta_uno == "La Vela" :  
#       print('¡Buen trabajo!, Respuesta correcta, te has ganado la LLAVE')
#       if pregunta_uno == '0':
#            print('Es de cera')
#            pregunta_uno= input('''
#            Soy alta cuando soy joven y baja cuando soy vieja. ¿Qué soy yo? : 
#            -Escriba la respuesta 
#            -0 PISTAS
#            ''')
#       elif pregunta_uno == "una vela" or pregunta_uno == "vela" or pregunta_uno == "Vela" or pregunta_uno == "la Vela" or pregunta_uno == "La Vela" :  
#            print('¡Buen trabajo!, Respuesta correcta, te has ganado la LLAVE')
#
#      
# 
#else:
#    print('Respuesta incorrecta, pierdes una vida')
#    vidas = vidas - 1
#    print(' Te quedan ' + str(vidas) + ' vidas')
 


def adivinanza2():
    pistas1 = ['Lo usas cuando se va la luz', 'Lo puedes prender con un encendedor', 'Es de cera']
    pistas2 = ["lo usas cuando hay luz", "gracias a estar encendido puedes leer", "se coloca en las lámparas"]
    pistas3 = ["fruta", "POTASIO", "parecido al plátano"]
    print('''
    ¡Estas en la computadora 2!
    Contesta estas adivinanzas para conseguir la llave
    ¿Estas listo?
    PRESIONA > PARA CONTINUAR
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
    pregunta_dos = input('''
        Es pequeño como una pera, pero alumbra la casa entera. ¿Qué soy yo?:
        -Escriba la respuesta 
        -Coloque 0 (cero) para una pista
       ''') 
    if pregunta_dos == '0':
       for i in range(1):
           print(random.choice(pistas2))
       pregunta_dos= input('''
       Es pequeño como una pera, pero alumbra la casa entera. ¿Qué soy yo? : 
       -Escriba la respuesta 
       -Coloque 0 (cero) para una pista
       ''') 
    elif pregunta_dos != "un bombillo" and pregunta_dos != "bombillo" and pregunta_dos != "El Bombillo" and pregunta_dos != "el bombillo" and pregunta_dos != "Bombillo":
       print('Respuesta incorrecta, pierdes una vida')
       vidas = vidas - 1/2
       print(' Te quedan ' + str(vidas) + ' vidas')
    
    else:
       print('¡Buen trabajo!, Respuesta correcta, te has ganado la LLAVE')
       premio_compu2 = 'llave'
       mochila.append(premio_compu2)


def adivinanza3():
    pistas1 = ['Lo usas cuando se va la luz', 'Lo puedes prender con un encendedor', 'Es de cera']
    pistas2 = ["lo usas cuando hay luz", "gracias a estar encendido puedes leer", "se coloca en las lámparas"]
    pistas3 = ["fruta", "POTASIO", "parecido al plátano"]
    print('''
    ¡Estas en la computadora 2!
    Contesta estas adivinanzas para conseguir la llave
    ¿Estas listo?
    PRESIONA > PARA CONTINUAR
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
    pregunta_tres = input('''
    Oro parece y plata no es, y no lo adivinas de aquí a un mes ¿Qué soy yo?: : 
    -Escriba la respuesta 
    -Coloque 0 (cero) para una pista
    ''') 
    if pregunta_tres == '0':
        for i in range(1):
            print(random.choice(pistas3))
        pregunta_tres= input('''
        Oro parece y plata no es, y no lo adivinas de aquí a un mes ¿Qué soy yo?: : 
        -Escriba la respuesta 
        -Coloque 0 (cero) para una pista
        ''') 
    elif pregunta_tres != "un cambur" and pregunta_tres != "cambur" and pregunta_tres != "El Cambur" and pregunta_tres!= "Cambur" and pregunta_tres != "cámbur" and pregunta_tres != "Cámbur":
       print('Respuesta incorrecta, pierdes una vida')
       vidas = vidas - 1/2
       print(' Te quedan ' + str(vidas) + ' vidas')
    
    else:
       print('¡Buen trabajo!, Respuesta correcta, te has ganado la LLAVE')
       premio_compu2 = 'llave'
       mochila.append(premio_compu2)


def adivinanzas():
   
   
   elegir = random.sample(lista,1)

   if elegir == 1:
       adivinanza1()
   elif elegir == 2:
       adivinanza3()
   else: 
       adivinanza2()

