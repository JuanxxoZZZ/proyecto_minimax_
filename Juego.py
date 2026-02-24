#Lo que hice aca fue darle una posicion al gato y al raton a la vez, tambien añadir lo que serian los turno del gato y el "limite"
fila_gato = 0
col_gato = 0

fila_raton = 5
col_raton = 5

turnos_gato = 0 
limite_de_turnos = 25

#esto seria basicamente una lista de los obstaculos que hay en el mapa 
lista_de_obstaculos = [(1, 1), (3, 3), (1, 2), (3, 4), (2, 1)]

"""Esto basciamente seria a lo que llamamos Distancia manhhattan, es calcular las dos posiciones de los jugadores
para luego calcular el mejor camino"""
def distancia_manhattan (fila_gato, col_gato, fila_raton, col_raton):
    return abs(fila_gato - fila_raton) + abs(col_gato - col_raton)

"""Esto seria una funcion para el raton, que lo que haria es ver si el raton primeramente no sobrepasa los obstaculos 
y que respete los obstaculos sino le devuelve en la misma posicion en la que estaba"""
def movimientos_validos(fila, col):
    direcciones_validas = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    movimientos_a_hacer = []

    for (movi_fila, movi_col) in direcciones_validas:
        nueva_fila = fila + movi_fila
        nueva_col = col + movi_col

        #movimientos validos del raton  
        if 0 <= nueva_fila <= 5 and 0 <= nueva_col <= 5:
            
            if (nueva_fila, nueva_col) not in lista_de_obstaculos:
                movimientos_a_hacer.append((nueva_fila, nueva_col))
                
    return movimientos_a_hacer
 
def minimax(fila_catmini, col_catmini, fila_ratmini, col_ratmini, turno, profundidad):
    #caso base, ya no genera futuros movimientos 
    if profundidad == 0:
        return distancia_manhattan (fila_catmini, col_catmini, fila_ratmini, col_ratmini)
    
    #el raton es max (porque busca maximizar la distancia)
    if turno == "raton":
        mejor_valor = -999
        movimientos_raton = movimientos_validos(fila_ratmini, col_ratmini)
        #este for lo que hace es 
        for (nueva_fila, nueva_col) in movimientos_raton:
            valor = minimax(fila_catmini, col_catmini, nueva_fila, nueva_col, "gato", profundidad - 1)
            if valor > mejor_valor:
                mejor_valor = valor 
        return mejor_valor
    #eL gato es min (Busca minimar la distancia)
    elif turno == "gato":
        mejor_valor = 999
        movimiento_mishi = movimientos_validos(fila_catmini, col_catmini)
        for (nueva_fila, nueva_col) in movimiento_mishi:
            valor = minimax (nueva_fila, nueva_col, fila_ratmini, col_ratmini, "raton", profundidad - 1)
            if valor < mejor_valor:
                mejor_valor = valor
        return mejor_valor
    
'''Hacer un ciclo while en donde calcule la posicion del gato y del raton para saber si el gato 
    atrapo al raton, mostrar el tablero, a los personajes, darles movimientos 
    y que funcione los obstaculos'''

while fila_gato != fila_raton or col_gato != col_raton:

       #Es un tablero sencillo con una lista dentro de otra lista
    tablero = [['.', '.', '.', '.', '.', '.'] for _ in range(6)]

    #Lo que simplemente hace esto es ubicar el emoji en el tablero y le asignamos la fila y la columna para ver en todo momento  
    tablero[fila_gato][col_gato] = "G"
    tablero[fila_raton][col_raton] = "R"

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

    raton_movimientos = movimientos_validos(fila_raton, col_raton)

    mejor_movimiento = None
    mejor_distancia = -999
    #lo que haria basicamente este for seria  

    for (nueva_fila, nueva_col) in raton_movimientos:
        valor = minimax(fila_gato, col_gato, nueva_fila, nueva_col, "gato", 3)
        if valor > mejor_distancia:
            mejor_distancia = valor
            mejor_movimiento = [nueva_fila, nueva_col]
    
    if mejor_movimiento:
        fila_raton = mejor_movimiento[0]
        col_raton = mejor_movimiento[1]

           #Esto basicamente serian los turno del gato, y si llega a su limite, el raton gana y le ponemos break para que no siga infinitamente
    turnos_gato = turnos_gato + 1
   
    #Lo que hace este aif es, calcular si el gato esta encima del raton y avisa si gana el gato y le ponemos break para que no siga infinitamente
    if (fila_gato, col_gato) == (fila_raton, col_raton):
        print("Gano el mishi")
        break
    
    if turnos_gato == limite_de_turnos:
        print("El raton gano")
        break
"""lo quee faltaria seria hacer que el raton se mueva y que respete todo como el gato"""
"""Básicamente lo que tendría que hacer con la librería random seria, crear una variable que en esa variable guarde los movimientos posibles 
 que va a hacer el ratón, luego hacemos que random.choice() elija los movimientos, luego "configuramos" los movimientos de arriba, abajo, etc etc"""
