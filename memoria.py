import random, sys

def memoria(mochila):
    print('''
    ¡Estas en el banco 2!
    Para obtener el martillo,
    debe jugar memoria
    PRESIONA > PARA CONTINUAR
    ''')
    si = input()
    while si != '>':
       print('''
       ¡Estas en en Saman!
       Para obtener el disco duro,
       debes encontrar la logica
       PRESIONA > PARA CONTINUAR
       ''')
       si = input()
    jugar_memoria(mochila)

def jugar_memoria(mochila):

        cartes = ['😀', '🙄', '🤮', '🥰', '😨', '🤓', '😷','🤑']
    
        parejas = len(cartes)
    
        tiradas = 0
    
        # Cargamos la lista
        taulell = []
        for i in range(2):
            taulell.append([])
            for j in range(4):
                taulell[i].append([])
                for k in range(4):
                    taulell[i][j].append('?')
    
        # Duplicamos las cartas
        cartes = cartes*2
    
        # Barajamos las cartas
        random.shuffle(cartes)
    
        # Cargamos la capa 0 (la capa que no se muestra) con las cartas
        k = 0
        for i in range(4):
            for j in range(4):
                taulell[0][i][j] = (cartes[k])
                k = k + 1
    
        # Mostramos la capa 1 y las coordenadas
        def mostrar_tablero(tablero):
            sys.stdout.write(' |')
            for x in range(4):
                sys.stdout.write(' ' + str(x))
            sys.stdout.write('\n')
            print ("============")
            lletra = 'A'
            for i in range(4):
                sys.stdout.write(lletra+'|')
                lletra = chr(ord(lletra) + 1)
                for j in range(4):
                    sys.stdout.write(' ' + taulell[1][i][j])
                sys.stdout.write('\n')
    
        mostrar_tablero(taulell)
        while taulell[1] != taulell[0]:
            fila = input("Fila?")
            fila = ord(fila) - 65
            columna = int(input("Columna?"))
    
            while columna > 4 or columna < 0 or fila > 4 or fila < 0:
                print ("Valor incorrecto")
                fila = input("Fila?")
                fila = ord(fila) - 65
                columna = int(input("Columna?"))
    
            taulell[1][fila][columna] = taulell[0][fila][columna]
            mostrar_tablero(taulell)
    
            resultado_1 = taulell[1][fila][columna]
    
            fila_auxiliar = input("Fila?")
            fila_auxiliar = ord(fila_auxiliar) - 65
            columna_auxiliar = int(input("Columna?"))
    
            while columna_auxiliar > 4 or columna_auxiliar < 0 or fila_auxiliar > 4 or fila_auxiliar < 0:
                print ("Valor incorrecto")
                fila_auxiliar = input("Fila?")
                fila_auxiliar = ord(fila_auxiliar) - 65
                columna_auxiliar = int(input("Columna?"))
    
            taulell[1][fila_auxiliar][columna_auxiliar] = taulell[0][fila_auxiliar][columna_auxiliar]
            mostrar_tablero(taulell)
            resultado_2 = taulell[1][fila_auxiliar][columna_auxiliar]
    
            tiradas += 1
    
            if resultado_1 != resultado_2:
                taulell[1][fila][columna] = "?"
                taulell[1][fila_auxiliar][columna_auxiliar] = "?"
                vidas = vidas - 1/4
            else:
                parejas -= 1
                print ("Correcto, te quedan ", parejas, " parejas")
    
        print ("Has necesitado ", tiradas, " tiradas")
        print(f'Te quedan {vidas} vidas')

    
    

