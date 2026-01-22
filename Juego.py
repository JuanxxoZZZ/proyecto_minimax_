#Lo que hice aca fue darle una posicion al gato y al raton a la vez 
fila_gato = 0
col_gato = 0

fila_raton = 5
col_raton = 5

#esto seria basicamente una lista de los obstaculos que hay en el mapa 
lista_de_obstaculos = [(2, 2), (3, 3), (2, 3), (5, 3)]

'''Hacer un ciclo while en donde calcule la posicion del gato y del raton para saber si el gato 
atrapo al raton, mostrar el tablero, a los personajes, darles movimientos 
y que funcione los obstaculos'''
while fila_gato != fila_raton or col_gato != col_raton:

       #Hacer un tablero sencillo con solo puntitos
    tablero = [['.', '.', '.', '.', '.', '.'] for _ in range(6)]

    #Lo que simplemente hace esto es ubicar el emoji en el tablero y le asignamos la fila y la columna para ver en todo momento  
    tablero[fila_gato][col_gato] = "G"
    tablero[fila_raton][col_raton] = "R"

    #Esto lo que hace es, como nosotros le dimos una lista de obstaculos con filas y columnas
    #lo que hace es poner visualmente los obstaculos 
    for (fila, col) in lista_de_obstaculos:
        tablero[fila][col] = '🟫'

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

    '''Que la fila nueva sea mayor o igual a 0 Y menor que 6 (porque tu tablero tiene 6 filas: 0, 1, 2, 3, 4, 5)
       Que la columna nueva sea mayor o igual a 0 Y menor que 6'''
    if fila_nueva >= 5:
    elif:
        col_nueva >= 5
        
        #Lo que tendria que hacer este if, seria calcular basicamente si la posicion del gato
        #este dentro del tablero para poder asi moverse chill de cojones 
