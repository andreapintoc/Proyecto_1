from util import obtener_inventario
from objetos import Objeto
class Juego:
    def __init__(self, nombre, requerimiento, premio, reglas, preguntas, mensaje_requerimiento=None):
        self.nombre = nombre
        self.requerimiento = requerimiento
        self.premio = premio
        self.reglas = reglas
        self.preguntas= preguntas 
        self.mensaje_requerimiento = mensaje_requerimiento
        

class Pregunta:
    def __init__(self, pregunta=None, respuesta=None):
        self.pregunta = pregunta
        self.respuesta = respuesta


class Pista(Pregunta):
    def __init__(self, pista1, respuesta1=None, respuesta2=None, respuesta3=None, pista2=None, pista3=None, pregunta=None, respuesta=None):
        Pregunta.__init__(self, pregunta, respuesta)
        self.respuesta1 = respuesta1
        self.respuesta2 = respuesta2
        self.respuesta3 = respuesta3
        self.pista1 = pista1
        self.pista2 = pista2
        self.pista3 = pista3

class Acertijo(Pregunta):
    def __init__(self, categoria, palabras, pregunta=None, respuesta=None):
        Pregunta.__init__(self, pregunta, respuesta)
        self.categoria = categoria
        self.palabras = palabras


class Quiz(Pista):
    def __init__(self, pregunta, respuesta1, respuesta2, respuesta3, respuesta4, pista1, pista2=None, pista3=None, respuesta=None):
        Pista.__init__(self, pista1, respuesta1, respuesta2, respuesta3, pista2, pista3, pregunta, respuesta)
        self.respuesta4 = respuesta4



class Lugar:
    def __init__(self, nombre, objetos=None):
        self.nombre = nombre
        self.objetos = objetos
                
    def cargar_objetos(self):
        lugares = obtener_inventario()
        for lugar in lugares:
            if lugar['name'] == self.nombre:
                objetos = []
                for objeto in lugar['objects']:
                    data_juego = objeto['game']
                    preguntas = []
                    for p in data_juego['questions']:
                        pregunta = crear_pregunta(objeto['name'], p)
                        preguntas.append(pregunta)
                    mensaje_requerido = data_juego['message_requirement'] if 'message_requirement' in data_juego else None
                    juego = Juego(data_juego['name'], data_juego['requirement'], data_juego['award'], data_juego['rules'], preguntas, mensaje_requerido)
                    obj = Objeto(objeto['name'], objeto['position'], juego)
                    objetos.append(obj)
                self.objetos = objetos
                break

    def obtener_movimientos(self):
        movimientos = 'PRESIONA:\n'
        for i, o in enumerate(self.objetos):
            movimientos += f'{i+1}. Para ir al {o.nombre} ({o.posicion})\n'
        movimientos += f'{len(self.objetos)+1}. Ir al plano '
        return movimientos


def crear_pregunta(objeto, dict_p):
    pregunta=None
    tipo_pista = ['pizarra', 'computadora 1', 'computadora 2', 'mueble de sentarse', 'mueble de libros', 'Banco 2', 'Papelera']
    if objeto == 'pizarra':
        pregunta = Pista( dict_p['clue_1'], dict_p['answer_1'], dict_p['answer_2'], dict_p['answer_3'], dict_p['clue_2'], dict_p['clue_3'])
    elif objeto == 'computadora 1' or objeto == 'computadora 2' or objeto == 'mueble de libros':
        pregunta = Pista(dict_p['clue_1'], None, None, None, dict_p['clue_2'], dict_p['clue_3'], dict_p['question'], dict_p['answer'])
    elif objeto == 'mueble de sentarse':
        pregunta = Pista(dict_p['clue_1'], None, None, None, None, None, dict_p['answer'])
    elif objeto == 'mueble de gabetas' :
        pregunta = Pregunta(dict_p['question'], dict_p['desplazamiento'])
    elif objeto == 'Saman':
        pregunta = Pregunta(dict_p)
    elif objeto == 'Banco 1':
        pregunta = Quiz(dict_p['question'], dict_p['correct_answer'], dict_p['answer_1'], dict_p['answer_2'],dict_p['answer_3'], dict_p['answer_4'], dict_p['clue_1'])
    elif objeto == 'Banco 2':
        pregunta = Pista(dict_p[clue_1], None, None, None, None, None, dict_p['question'])
    elif objeto == 'puerta':
        pregunta = Pregunta(dict_p['question'], dict_p['answer'])
    elif objeto == 'Rack':
        pregunta = Acertijo(dict_p['category'], dict_p['words'], dict_p['question'])
    elif objeto == 'Papelera':
        pregunta = Pista(dict_p['clue_1'], None, None, None, None, None, dict_p['question'], dict_p['answer'])
    
    return pregunta

            

