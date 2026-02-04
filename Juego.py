import random

#Lo que hice aca fue darle una posicion al gato y al raton a la vez, tambien añadir lo que serian los turnos del gato y el "limite"
fila_gato = 0
col_gato = 0

fila_raton = 5
col_raton = 5

turnos_gato = 0 
limite_de_turnos = 20


#esto seria basicamente una lista de los obstaculos que hay en el mapa 
lista_de_obstaculos = [(2, 2), (3, 3), (2, 3), (5, 3)]

def distancia_GyR (fila_gato, col_gato, fila_raton, col_raton):
    return abs(fila_gato - fila_raton) + abs(col_gato - col_raton)


def movimientos_validos(fila, col):
    direcciones_validas = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    movimientos_a_hacer= []
    distancia_encontrada = 0 
    mejor_movimiento = 0 

    for (movi_fila, movi_col) in direcciones_validas:
        nueva_fila = fila + movi_fila
        nueva_col = col + movi_col
        if 0 <= nueva_fila <= 5 and 0 <= nueva_col <= 5:
            if (nueva_fila, nueva_col) not in lista_de_obstaculos:
                movimientos_a_hacer.append((nueva_fila, nueva_col))
                

                '''Hacer un ciclo while en donde calcule la posicion del gato y del raton para saber si el gato 
atrapo al raton, mostrar el tablero, a los personajes, darles movimientos 
y que funcione los obstaculos'''

while fila_gato != fila_raton or col_gato != col_raton:

       #Hacer un tablero sencillo con solo puntitos
    tablero = [['.', '.', '.', '.', '.', '.'] for _ in range(6)]

    #Lo que simplemente hace esto es ubicar el emoji en el tablero y le asignamos la fila y la columna para ver en todo momento  
    tablero[fila_gato][col_gato] = "🐱"
    tablero[fila_raton][col_raton] = "🐭"

    #Esto lo que hace es, como nosotros le dimos una lista de obstaculos con filas y columnas
    #lo que hace es poner visualmente los obstaculos 
    for (fila, col) in lista_de_obstaculos:
        tablero[fila][col] = '◾'

    #esto es simple y llanamente para quitar las comillas del tablero 
    for fila in tablero:
        print(' '.join(fila))

    #con esto le pedimos al usuario que ingrese el movimiento del gato
    tecla = input("Ingrese el movimiento: ").lower()

    fila_nueva = fila_gato
    col_nueva = col_gato

    if tecla == "w":
        fila_nueva -= 1 
    elif tecla == "s":
        fila_nueva += 1 
    elif tecla == "a": 
        col_nueva -= 1
    elif tecla == "d":
        col_nueva += 1 
    else:
        print("El movimiento no es valido")
        continue

        #Lo que tendria que hacer este if, seria calcular basicamente si la posicion del gato
        #este dentro del tablero para poder asi moverse chill de cojones
         
    '''Que la fila nueva sea mayor o igual a 0 Y menor que 5 (porque tu tablero tiene 5 filas: 0, 1, 2, 3, 4, 5)
       Que la columna nueva sea mayor o igual a 0 Y menor que 5'''

    if 0 <= fila_nueva <= 5 and 0 <= col_nueva <= 5:

        #Esto hace que el gato respete los obstaculos y le alerta de paso si puede pasar o no   
     if (fila_nueva, col_nueva) not in lista_de_obstaculos:
        fila_gato = fila_nueva
        col_gato = col_nueva
     else:
        print("Estas chocando un obstaculo")

    #Esto basicamente serian los turnos del gato, y si llega a su limite, el raton gana y le ponemos break para que no siga infinitamente
     turnos_gato = turnos_gato + 1

    if turnos_gato == limite_de_turnos:
        print("El raton gano")
        break
    #Lo que hace este if es, calcular si el gato esta encima del raton y avisa si gana el gato y le ponemos break para que no siga infinitamente
    if (fila_nueva, col_nueva) == (fila_raton, col_raton):
        print("Gano el mishi")
        break
    #esto seria los movimientos que haria el raton 
    direcciones_raton = ("arriba", "abajo", "izquierda", "derecha")

    #aca hacemos que la libreria random decida aleatoriamente en que direccion se va a mover el raton 
    movimientos_raton = random.choice(direcciones_raton)

    fila_nuevarat = fila_raton
    col_nuevarat = col_raton

    if movimientos_raton == "arriba":
        fila_nuevarat -= 1 
    elif movimientos_raton == "abajo":
        fila_nuevarat += 1
    elif movimientos_raton == "izquierda":
        col_nuevarat -= 1 
    elif movimientos_raton == "derecha":
        col_nuevarat += 1 

        """lo quee faltaria seria hacer que el raton se mueva y que respete todo como el gato"""
        """Básicamente lo que tendría que hacer con la librería random seria, crear una variable que en esa variable guarde los movimientos posibles 
         que va a hacer el ratón, luego hacemos que random.choice() elija los movimientos, luego "configuramos" los movimientos de arriba, abajo, etc etc"""    

    if 0 <= fila_nuevarat <= 5 and 0 <= col_nuevarat <= 5:

            if (fila_nuevarat, col_nuevarat) not in lista_de_obstaculos:
                fila_raton = fila_nuevarat
                col_raton = col_nuevarat
