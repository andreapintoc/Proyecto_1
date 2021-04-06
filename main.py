from memoria import * #juego
from final import * #juego final
from logica import * #juego
from criptograma import * #juego
from ahorcado import * #juego
from adivinanza import * #juego
from jugador import * #clase jugador, registro, obtener jugador , entre otras
from palabras import * #juego
from quizzi import * #juego
from python import * #juego
from booleana import * #juego
from juegos import Lugar #clase paa definir el lugar desde el api
from sopa import * #juego
import imagenes #imagenes de los cuartos
import instrucciones #instrucciones de juego
import escoge_numero #juego
import time #para el tiempo
import os 
import json #json


mochila = {
    'premios':[],
    'vidas': 0 }


def empezar_juego(): #Iniciar sesion y elegir nivel de dificultad

    usuario =input('Intruzca su usuario: ')
    jugadores = obtener_usuarios()
    usuarios = [u['usuario'] for u in jugadores]
    usuario_valido = False
    jugador = None
    while not usuario_valido: #validacion si el usuario existe
        if usuario in usuarios:
            print('Usuario valido')
            jugador = obtener_jugador(usuario, jugadores)
            usuario_valido = True
        else:
            print('Este usuario no existe, presione 1 para registrarse')
            main()
    clave = input('Intruzca la clave: ')
    clave_valida = False
    while not clave_valida: #validacion de la clave con el del usuario
        if jugador.clave == clave:
            print('Clave correcta')
            clave_valida = True
        else:
            print('Clave Incorrecta')
            respuesta =input('''
            PRESIONE:
            1. Para ir al menu
            2.Para ingresar la clave nuevamente
            ''')
            if respuesta == 1:
                main()
            else:
                clave = input('Intruzca la clave: ')
    jugador.guardar_partidas()

    if jugador.avatar == 1:
        jugador.avatar = 'Scharifker'
    elif jugador.avatar == 2:
        jugador.avatar = 'Eugenio Mendoza'
    elif jugador.avatar == 3:
        jugador.avatar = 'Pelusa'
    elif jugador.avatar == 4:
        jugador.avatar = 'Gandhi'
    else:
        jugador.avatar = 'Pepe'
                
    print('Ingrese nivel de dificultad a jugar: ')
    nivel = input('''
    1.Fácil: 5 vidas y 5 pistas. 45 minutos
    2.Medio: 3 vidas y 3 pistas. 35 minutos
    3.Difícil: 1 vida y 2 pistas. 25 minutos
    ''')
    while nivel != '1' and nivel != '2' and nivel != '3':
        nivel = input('''
        Ingrese un nivel valido:
        1.Fácil: 5 vidas y 5 pistas. 45 minutos
        2.Medio: 3 vidas y 3 pistas. 35 minutos
        3.Difícil: 1 vida y 2 pistas. 25 minutos
        ''')
    
    if nivel == '1': #cronometro tiempo 45
        tiempo_inicial = time.time()
        fin_juego = tiempo_inicial + (60*45)
        while time.time() < fin_juego:
            nivel_uno(jugador, tiempo_inicial)
        print('Tiempo agotado')
        main()


    elif nivel == '2': #cronometro tiempo 35
        tiempo_inicial = time.time()
        fin_juego = tiempo_inicial + (60*35)
        while time.time() < fin_juego:
            nivel_dos(jugador, tiempo_inicial)
        print('Tiempo agotado')
        main()

       
    else: #cronometro tiempo 25 minutos
        tiempo_inicial = time.time()
        fin_juego = tiempo_inicial + (60*25)
        while time.time() < fin_juego:
            nivel_tres(jugador, tiempo_inicial)
        print('Tiempo agotado')  
        main()

def nivel_uno(jugador, tiempo_inicial): #Inicio del juego mas facil
    mochila['vidas'] = 5
    #primera narrativa
    print('''
      Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), 
     lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto
     de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. 
     Necesitamos que nos ayudes a recuperar el disco, para eso tienes 45 minutos, antes 
        de que el servidor se caiga y no se pueda hacer más nada.                 
    ''')
    print(imagenes.plano)
    empezar = input('¿Aceptas el reto? (PRESIONA ">" PARA CONTINUAR)')
    while empezar.upper() != '>':
        empezar = input('¿Aceptas el reto? (PRESIONA ">" PARA CONTINUAR)' )
    print(f'¡EMPECEMOS¡')

    #segunda narrativa
    print(imagenes.biblioteca) #plano de la biblioteca
    print(f'''
    Bienvenido {jugador.avatar}, gracias por tu disposición a ayudarnos a resolver este inconveniente, 
     te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué
                                acciones puedes realizar. 
           Recuerda que el tiempo corre más rápido que un trimestre en este reto.
    ''')
    print(imagenes.plano)
    dirigirse = input('''
    ¿A donde quieres dirigirte?:
    1. Si desea quedarse en la Biblioteca, PRESIONE 1
    2. Si desea ir al Rectorado, PRESIONE 2
    3. Si desea ir a la Puerta, PRESIONE 3
    ''').upper()

    while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3':
        dirigirse = input('''
    ¿A donde quieres dirigirte?:
    1. Si desea quedarse en la Biblioteca, PRESIONE 1
    2. Si desea ir al Rectorado, PRESIONE 2
    3. Si desea ir a la Puerta, PRESIONE 3
    ''').upper()
     
    if dirigirse == '1':
        biblioteca(mochila) #ir a la biblioteca
    elif dirigirse == '2':
        rectorado(mochila) #ir a plaza rectorado
    else:
        puerta(mochila) #ir a la puerta    

def nivel_dos(jugador, tiempo_inicial): #Inicio del juego medio
    mochila['vidas'] = 3
    #if vidas <= 3:
    #    print('Te quedaste sin vidas')
    # primera narrativa
    print('''
      Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), 
     lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto
     de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. 
     Necesitamos que nos ayudes a recuperar el disco, para eso tienes 35 minutos, antes 
        de que el servidor se caiga y no se pueda hacer más nada.                 
    ''')
    print(imagenes.plano)
    empezar = input('¿Aceptas el reto? (PRESIONA ">" PARA CONTINUAR)')
    while empezar.upper() != '>':
        empezar = input('¿Aceptas el reto? (PRESIONA ">" PARA CONTINUAR)' )
    print(f'¡EMPECEMOS¡')
    print(imagenes.biblioteca) #plano de la biblioteca
    #segunda narrativa
    print(f'''
    Bienvenido {jugador.avatar}, gracias por tu disposición a ayudarnos a resolver este inconveniente, 
     te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué
                                acciones puedes realizar. 
           Recuerda que el tiempo corre más rápido que un trimestre en este reto.
    ''')
    print(imagenes.plano)
    dirigirse = input('''
    ¿A donde quieres dirigirte?:
    1. Si desea quedarse en la Biblioteca, PRESIONE 1
    2. Si desea ir al Rectorado, PRESIONE 2
    3. Si desea ir al Puerta, PRESIONE 3
    ''').upper()
    while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3':
        dirigirse = input('''
    ¿A donde quieres dirigirte?:
    1. Si desea quedarse en la Biblioteca, PRESIONE 1
    2. Si desea ir al Rectorado, PRESIONE 2
    3. Si desea ir al Puerta, PRESIONE 3
    ''').upper()
    if dirigirse == '1':
        biblioteca(mochila) #ir a la biblioteca
    elif dirigirse == '2':
        rectorado(mochila) #ir a plaza rectorado
    else:
        puerta(mochila) #ir a la puerta    
 

def nivel_tres(jugador, tiempo_inicial): #Inicio del juego dificil
    mochila['vidas'] = 1
    #primera narrativa
    print('''
      Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), 
     lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto
     de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. 
     Necesitamos que nos ayudes a recuperar el disco, para eso tienes 25 minutos, antes 
        de que el servidor se caiga y no se pueda hacer más nada.                 
    ''')
    print(imagenes.plano)
    empezar = input('¿Aceptas el reto? (PRESIONA ">" PARA CONTINUAR)')
    while empezar.upper() != '>':
        empezar = input('¿Aceptas el reto? (PRESIONA ">" PARA CONTINUAR)' )
    print(f'¡EMPECEMOS¡')


    print(imagenes.biblioteca) #plano de la biblioteca
    #segunda narrativa
    print(f'''
    Bienvenido {jugador.avatar}, gracias por tu disposición a ayudarnos a resolver este inconveniente, 
     te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué
                                acciones puedes realizar. 
           Recuerda que el tiempo corre más rápido que un trimestre en este reto.
    ''')
    print(imagenes.plano)
    dirigirse = input('''
    ¿A donde quieres dirigirte?:
    1. Si desea quedarse en la Biblioteca, PRESIONE 1
    2. Si desea ir al Rectorado, PRESIONE 2
    3. Si desea ir al Puerta, PRESIONE 3
    ''').upper()

    while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3':
        dirigirse = input('''
    ¿A donde quieres dirigirte?:
    1. Si desea quedarse en la Biblioteca, PRESIONE 1
    2. Si desea ir al Rectorado, PRESIONE 2
    3. Si desea ir al Puerta, PRESIONE 3
    ''').upper()
     
    if dirigirse == '1':
        biblioteca(mochila) #ir a la biblioteca
    elif dirigirse == '2':
        rectorado(mochila) #ir a plaza rectorado
    else:
        puerta(mochila) #ir a la puerta  

def biblioteca(mochila):
    print(imagenes.biblioteca)
    print('¡Estas en la biblioteca!')
    biblioteca_lugar = Lugar('Biblioteca') #definir lugar
    biblioteca_lugar.cargar_objetos() #definir objetos
    movimientos = biblioteca_lugar.obtener_movimientos() #definir el menu para que el usuario se mueva al sillon, estante o gavetas
    dirigirse = input(movimientos).upper()
    while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3' and dirigirse.upper() != '4':
        dirigirse = input(movimientos).upper()
    if dirigirse == '1':
        requerimiento_estante = False
        ahorcado() #ir al estante
        biblioteca(mochila)

    elif dirigirse == '2':
        requerimiento_sillon = 'libro de matematicas'
        if requerimiento_sillon not in mochila['premios']:
            print('Debes saber derivar')
            biblioteca(mochila)
        pass #ir al sillon
        biblioteca(mochila)

    elif dirigirse == '3':
        mensaje_estante = biblioteca_lugar.objetos[2].juego.mensaje_requerimiento
        requerimiento_gavetero = 'llave'
        if requerimiento_gavetero not in mochila['premios']:
            print(mensaje_estante)
            biblioteca(mochila)
        criptograma(mochila) #ir al gavetero
        biblioteca(mochila)
        if tiene_vidas(mochila['vidas']):
            biblioteca(mochila)
        else:
            print('perdiste')

    else:
        print(imagenes.plano)
        dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir a la Puerta, PRESIONE 3
        ''').upper()

        while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3':
            dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir a la Puerta, PRESIONE 3
        ''').upper()
        if dirigirse == '1':
            biblioteca(mochila) #ir a la biblioteca
        elif dirigirse == '2':
            rectorado(mochila) #ir a plaza rectorado
        else:
            puerta(mochila) #ir a la puerta 

def rectorado(mochila):
    print(imagenes.saman)
    print('¡Estas en Plaza Rectorado!')
    p_rectorado = Lugar('Plaza Rectorado') #definir lugar
    p_rectorado.cargar_objetos() #definir objetos
    movimientos = p_rectorado.obtener_movimientos() #definir menu para dirigirse al saman, o a los bancos
    dirigirse = input(movimientos).upper()
    while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3' and dirigirse.upper() != '4':
        dirigirse = input(movimientos).upper()
    if dirigirse == '1':
        requerimiento_saman = 'titulo universitario', 'mensaje' #mensaje que indica que necesita eso para entrar
        if requerimiento_saman not in mochila['premios']:
            print('pierdes una vida por pisar el samán 🥵')
            vidas =- 1
            rectorado(mochila)
        logica(mochila) #ir al saman
        rectorado(mochila)

    elif dirigirse == '2':
        requerimiento_banco1 = False
        quizzi(mochila) #ir al banco 1
        rectorado(mochila)

    elif dirigirse == '3':
        requerimiento_banco2 = False
        memoria(mocila) #ir al banco 2
        rectorado(mochila)
    else:
        print(imagenes.plano)
        dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir a la Puerta, PRESIONE 3
        ''').upper()

        while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3':
            dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir a la Puerta, PRESIONE 3
        ''').upper()
        if dirigirse == '1':
            biblioteca(mochila) #ir a la biblioteca
        elif dirigirse == '2':
            rectorado(mochila) #ir a plaza rectorado
        else:
            puerta(mochila) #ir a la puerta 

def puerta(mochila):
    print(imagenes.puerta)
    print('¡Estas en la puerta!')
    pasillo = Lugar('Pasillo Laboratorios ') #definir el lugar
    pasillo.cargar_objetos() #definir objetos
    movimientos = pasillo.obtener_movimientos() #Crear menu para dirigirse a la puerta o al plano
    dirigirse = input(movimientos).upper() 
    while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3' :
            dirigirse = input(movimientos).upper()
    if dirigirse == '1':
        requerimiento_puerta = 'martillo'
        if requerimiento_puerta not in mochila['premios']:
            print('Está cerrado con candado!!!!!')
            puerta(mochila)
        booleana() #ir a la puerta
        puerta(mochila)
    else:
        print(imagenes.plano)
        dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir al laboratorio, PRESIONE 3
        4. Si desea ir al Cuarto de servidores, PRESIONE 4
        ''').upper()

        while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3' and dirigirse.upper() != '4':
            dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir al laboratorio, PRESIONE 3
        4. Si desea ir al Cuarto de servidores, PRESIONE 4
        ''').upper()
        if dirigirse == '1':
            biblioteca(mochila) #ir a la biblioteca
        elif dirigirse == '2':
            rectorado(mochila) #ir a plaza rectorado
        elif dirigirse == '3':
            puerta(mochila) #ir a la puerta 
        else:
            cuarto_servidores(mochila) #ir al cuarto de servidores

def cuarto_servidores(mochila):
    print(imagenes.cuarto_servidores)
    print('¡Estas en el Cuarto de servidores!')
    cuarto_de_sevidores = Lugar('Cuarto de Servidores ') #definir el lugar
    cuarto_de_sevidores.cargar_objetos() #definir objetoa
    movimientos = cuarto_de_sevidores.obtener_movimientos() #crear el menu para dirigirse al rack, puerta o papelera
    dirigirse = input(movimientos).upper()
    while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3' and dirigirse.upper() != '4':
        dirigirse = input(movimientos).upper()
    if dirigirse == '1':
        requerimiento_puertalab = 'carnet'
        if requerimiento_puertalab not in mochila['premios']:
            print('Necesitas tener un carnet de trabajador para poder pasar')
            cuarto_servidores(mochila)
        juegoquizzi(mochila) #ir a la puerta 
        ganador(mochila)
    elif dirigirse == '2':
        requerimiento_rack = False
        palabra_mezclada(mochila) #ir al rack
        cuarto_servidores(mochila)
    elif dirigirse == '3':
        requerimiento_papelera = False
        escoge_numero(mochila) #ir a la papelera
        cuarto_servidores(mochila)
    else:
        print(imagenes.plano)
        dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir al laboratorio, PRESIONE 3
        4. Si desea ir al Cuarto de servidores, PRESIONE 4
        ''').upper()

        while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3' and dirigirse.upper() != '4':
            dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir al laboratorio, PRESIONE 3
        4. Si desea ir al Cuarto de servidores, PRESIONE 4
        ''').upper()
        if dirigirse == '1':
            biblioteca(mochila) #ir a la biblioteca
        elif dirigirse == '2':
            rectorado(mochila) #ir a plaza rectorado
        elif dirigirse == '3':
            laboratorio(mochila) #ir a la puerta 
        else:
            cuarto_servidores(mochila) #ir al cuarto de servidores

def laboratorio(mochila):
    print(imagenes.laboratorio)
    print('¡Estas en el laboratorio!')
    laboratorio_sl = Lugar('Laboratorio SL001') 
    laboratorio_sl.cargar_objetos() #definicion de objetos
    movimientos = laboratorio_sl.obtener_movimientos() #crear menu, para dirigirse a las computadoras o a la pizzara
    dirigirse = input(movimientos).upper() 
    while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3' and dirigirse.upper() != '4':
        dirigirse = input(movimientos).upper()
    if dirigirse == '1':
        requerimiento_pizarra = False
        matriz(mochila) #ir a la pizarra
        laboratorio(mochila)
    elif dirigirse == '2':
        requerimiento_compu1 = 'cable HDMI'
        if requerimiento_compu1 is not mochila['premios']:
            print('Mi pantalla no funciona')
            laboratorio(mochila)
        else:
            python(mochila) #ir a computadora 1
            laboratorio(mochila)

    elif dirigirse == '3':
        requerimiento_compu2 = 'contraseña'
        if requerimiento_compu2 not in mochila['premios']:
            print('necesita contraseña para ingresar')
            laboratorio(mochila)
        adivinanzas(mochila) #ir a la computadora 2
        laboratorio(mochila)
    else:
        print(imagenes.plano)
        dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir al laboratorio, PRESIONE 3
        4. Si desea ir al Cuarto de servidores, PRESIONE 4
        ''').upper()

        while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3' and dirigirse.upper() != '4':
            dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir al laboratorio, PRESIONE 3
        4. Si desea ir al Cuarto de servidores, PRESIONE 4
        ''').upper()
        if dirigirse == '1':
            biblioteca(mochila) #ir a la biblioteca
        elif dirigirse == '2':
            rectorado(mochila) #ir a plaza rectorado
        elif dirigirse == '3':
            laboratorio(mochila) #ir a la puerta 
        else:
            cuarto_servidores(mochila) #ir al cuarto de servidores


def ganador(mochila, tiempo_inicial):
    tiempo = (time.time() - tiempo_inicial/60)
    jugador.guardar_record(tiempo)
    print(f'''
           ¡Felicidades! Has logrado evitar una catástrofe en la Unimet,
                muchas gracias por tu apoyo, sin ti no lo hubiesemos
                        logrado, lo hiciste en un tiempo 
                           de {tiempo} minutos
    ''')
def estadisticas():
    #jugador = obtener_jugador()
    print('''
                ESTADISTICAS DE JUEGO ESCAPAMET
    ''')
    menu1 = True 
    while menu1:
        print('''
        1. Los mejores records
        2. Cuartos mas visitados por los jugadores
        3. Jugadores que mas juegan ESCAPAMET
        ''')
        opcion1 = int(input('Seleccione una opcion 1, 2, 3 o 4: '))
        if opcion1 == 1:
            records=mejores_records()
            records.sort()
            print(records)
            
          
        elif opcion1 == 2:
            print('''
            Los cuartos mas visitados de ESCAPAMET son la biblioteca,
                                y Plaza rectorado
            ''')
 
        elif opcion1 == 3:
            print('''
            Los jugadores que mas juegan ESCAPAMET son:
            ''')
            print(usuarios['usuario', 'partidas'])
            
        else:
            print('Seleccione una opccion correcta') 
    

def main():
    print('BIENVENDO A ESCAPAMET')
    menu = True 
    while menu:
        print('''
        1. Registrar usuario
        2. Empezar el juego
        3. Ver instrucciones de juego
        4. Estadisticas de juego
        ''')
        opcion = int(input('Seleccione una opcion 1, 2, 3 o 4: '))
        if opcion == 1:
           # registro() 
            jugador = Jugador() #clase jugador
            jugador.registro() #registrar jugador
            print(jugador.nombre)
            menu = False
          
        elif opcion == 2:
            empezar_juego() #funcion que inicia el juego
 
        elif opcion == 3:
            print(instrucciones.manual)
            ir_menu = input('PRESIONE (>) PARA JUGAR') 

        elif opcion == 4:
            estadisticas()
            #ganador(mochila, tiempo_inicial)
            

        else:
            print('Seleccione una opccion correcta') 
  
main()  