Sudoku = [
    [0,0,1,0,3,4,0,0,6],
    [0,4,0,0,0,2,5,8,0],
    [0,5,0,1,8,0,0,4,0],
    [1,3,2,0,4,0,0,0,0],
    [0,0,0,0,1,6,0,0,0],
    [7,6,4,8,5,0,0,2,0],
    [0,0,0,3,9,1,0,5,8],
    [9,1,0,7,0,8,4,0,0],
    [6,0,0,4,2,0,0,0,7]
]

def imprimir_Sudoku(Sudoku):
    for i in range(9):
        if i % 3 == 0 : #SEPARACION CADA 3 FILAS
            print("------------------------")
        for j in range(9):
            if j % 3 == 0 : #SEPARACION CADA 3 COLUMNAS
                print("| ", end="")
            if j == 8: #SI LA CELDA ESTA EN LA ULTIMA COLUMNA, IMPRIME VALOR SEGUIDA DE LA SEPARACION
                print(Sudoku[i][j], "|")
            else:
                print(str(Sudoku[i][j]) + " ", end="") #DE LO CONTRARIO IMPRIME VALOR SEGUIDO DE UN ESPACIO

def valido(Sudoku, n, i, j):
    fila = Sudoku[i]
    columna = [f[j] for f in Sudoku]
    bloque = [Sudoku[a][b] for a in range(9) for b in range(9) if (a//3 == i//3) and (b//3 == j//3)] #CONTIENE LOS NUMEROS QUE YA ESTAN AHI
    return n not in fila and n not in columna and n not in bloque

def resolver_sudoku(Sudoku):
    for i in range(9): #RECORRE FILA
        for j in range(9): #RECORRE COLUMNA
            if Sudoku[i][j] == 0: #COMPROBAR QUE LA CASILLA ESTE VACIA = O,1
                for n in range(1, 10): #NUMERO DEL 1 AL 9 PARA PROBAR SI PODEMOS METERLO EN UNA CASILLA
                    if valido(Sudoku, n, i, j): #SI NO SE REPITE EN CADA FILA, COLUMNA Y BLOQUE
                        Sudoku[i][j] = n #ENTONCES EN LA POSICION DE LA CASILLA AHORA SERÁ N
                        if resolver_sudoku(Sudoku): #REPETIR LO MISMO (RECURSIVIDAD) || PUEDE QUE SE SOLUCIONE O NO (IF)
                            return True
                        else:
                            Sudoku[i][j] = 0 #SI NO SE VUELVE VACIA DE NUEVO
                return False #SI ES QUE NO HAY SOLUCION
    return True #ESTA BIEN RESUELTO

if resolver_sudoku(Sudoku):
    imprimir_Sudoku(Sudoku)
else:
    print("No se encontró solución") 
           




                         