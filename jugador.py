import json
from util import leer_data, escribir_data


class Jugador:

    def __init__(self, nombre=None, edad=None, usuario=None, clave=None, avatar=None, record=0, partidas=0):
        self.nombre = nombre
        self.edad = edad
        self.usuario = usuario
        self.clave = clave
        self.avatar = avatar
        self.record = record
        self.partidas = partidas

    

    def registro(self): #Se piden los siguientes datos al usuario para registrarlo
        nombre = input('Introduzca nombre del jugador: ') #Su nombre
        while not nombre.isalpha():
            nombre = input('Nombre incorrecto, introduzca su nombre:')
        edad = input('Introduzca su edad:')
        while not edad.isnumeric() and edad <= 0 :
            edad = input('Edad incorrecta, introduzca edad del jugador: ') #Su edad
        usuario = input('Indroduzca un nombre de usuario:')
        while not usuario.isalpha():
            usuario = input('Introduzca un nombre de usuario correcto: ') #Su usuario, debe ser distinto a los que ya existen
        usuarios = obtener_usuarios()
        usuario_verificado = False
        while not usuario_verificado:
            encontrado = False
            for u in usuarios:
                if u['usuario'] == usuario:
                    encontrado = True
                    print('Usuario existente')
                    usuario = input('Indroduzca un nombre de usuario: ')
            if not encontrado:
                usuario_verificado = True

        clave = input('Ingrese su contraseña: ') #Su clave, debe contener al menos 8 caracteres, no debe tener espacios en blanco y deben ser solo numeros
        while len(clave) < 8:
            clave = input('La contrasena debe tener al menos 8 caracteres, Introduzca una contraseña valida: ')
        while clave.count(" ")> 0:
            clave = input('La contrasena no puede contener espacios en blanco, Introduzca contraseña valida: ')
        while not clave.isnumeric():
            clave = input('La contrasena no puede contener letras, Introduzca una contraseña valida: ')
        #Su avatar
        avatar = input('''
        Seleccione el avatar de su preferencia:      
        1.Scharifker
        2.Eugenio Mendoza
        3.Pelusa
        4.Gandhi 
        5.Pepe
        ''')
        while not avatar.isnumeric():
            avatar = input('''
            Ingrese el numero del avatar de su preferencia:
            1.Scharifker
            2.Eugenio Mendoza
            3.Pelusa
            4.Gandhi 
            5.Pepe
            ''')
        while avatar != '1' and avatar != '2' and avatar != '3' and avatar != '4' and avatar != '5':
               avatar = input('''
               Avatar invalido. Introduzca el avatar de su preferencia:
               1.Scharifker
               2.Eugenio Mendoza
               3.Pelusa
               4.Gandhi 
               5.Pepe
               ''')
        record = 0
        partidas = 0

        print('JUGADOR REGISTRADO')  
        self.nombre = nombre
        self.edad = edad
        self.usuario = usuario
        self.clave = clave
        self.avatar= avatar
        self.record = record 
        self.partidas = partidas

        usuario = json.dumps(self.__dict__) #hacer diccionario
        usuario = json.loads(usuario)
        data = leer_data()
        data['usuarios'].append(usuario)
        escribir_data(data)
        
        registrado_menu = input('¿Desea registrar otro usuario? S (si) N (no)').upper()
        if registrado_menu.upper() == 'S':
            registro()
        
    def guardar_partidas(self): #Cantidad de partidas que ha jugado
        data = leer_data()
        for u in data['usuarios']:
            if u['usuario'] == self.usuario:
                u['partidas'] += 1
                break 
        escribir_data(data)

    def guardar_record(self, record): #funcion para huardar el record mas alto del jugador
        data = leer_data()
        for u in data['usuarios']:
            if u['usuario'] == self.usuario and u['record'] > record:
                u['record'] = record
                break 
        escribir_data(data)
            
def mejores_records():
    records = []
    datos = obtener_usuarios()
    for u in datos:
        records.append(u['record'])
    return records
                 

def obtener_usuarios(): #obtener los usuarios
    datos = leer_data()
    return datos['usuarios']


def obtener_jugador(usuario, usuarios=None): #obtener todos los datos del jugador
    if not usuarios:
        usuarios = obtener_usuarios()
    for jugador in usuarios:
        if jugador['usuario'] == usuario:
            return Jugador(jugador['nombre'], jugador['edad'], jugador['usuario'], jugador['clave'], jugador['avatar'], jugador['record'])

def tiene_vidas(vidas): #para saber si tines vidas y continuar o salir de juego
    if vidas <= 0:
        print('Te quedaste sin vidas')
        return False 
    return True 
