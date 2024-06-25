import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk 

#Arreglo sudokupredefinido
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
        if i % 3 == 0:  # Separación cada 3 filas
            print("------------------------")
        for j in range(9):
            if j % 3 == 0:  # Separación cada 3 columnas
                print("| ", end="")
            if j == 8:  # Si es la última columna, imprimir valor seguido de la separación
                print(Sudoku[i][j], "|")
            else:
                print(str(Sudoku[i][j]) + " ", end="")
    print("------------------------")

def valido(Sudoku, n, i, j):
    fila = Sudoku[i]
    columna = [f[j] for f in Sudoku]
    bloque = [Sudoku[a][b] for a in range(9) for b in range(9) if (a // 3 == i // 3) and (b // 3 == j // 3)]
    return n not in fila and n not in columna and n not in bloque

def resolver_sudoku(Sudoku):
    for i in range(9):
        for j in range(9):
            if Sudoku[i][j] == 0:
                for n in range(1, 10):
                    if valido(Sudoku, n, i, j):
                        Sudoku[i][j] = n
                        if resolver_sudoku(Sudoku):
                            return True
                        else:
                            Sudoku[i][j] = 0
                return False
    return True

#Panel donde se mostrara el Sudoku
def Segundo_paneljuego():
    global Sudoku
    juejuegosudoku.deiconify() #Muestra el segundo panel
    root.withdraw()#elimina el segundo panel

    # Resolver Sudoku
    if resolver_sudoku(Sudoku):
        imprimir_Sudoku(Sudoku)
    else:
        print("No se encontró solución")

    # recorrer el arreglo del sudoku
    for i in range(9):
        for j in range(9):
            if Sudoku[i][j] == 0:
                label = tk.Label(juejuegosudoku, text=" ", width=4, height=2, font=('bell', 10), bg="#659DCC")
            else:
                label = tk.Label(juejuegosudoku, text=str(Sudoku[i][j]), width=4, height=2, font=('bell', 10))
            label.grid(row=i, column=j, padx=1, pady=1)

#Panel principal

root = tk.Tk()
root.title("Sudoku")
root.geometry("500x500")

background_image = ImageTk.PhotoImage(Image.open("./resources/Fondo.jpeg"))

background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  
# Establecer la imagen de fondo en toda la ventana


title_label = tk.Label(root, text="SUDOKU", font=("Bell", 30), bg = "#659DCC",fg="white")
title_label.place(x=150, y=80)


start_button = tk.Button(root, text="START GAME", font=("Bell", 14), bg="#6495ED", fg="white", command=Segundo_paneljuego)
start_button.place(x=180, y=440)


#Llamado al segundo panel, aca lo crea al panel 
juejuegosudoku = tk.Toplevel()
juejuegosudoku.title("Sudoku")
juejuegosudoku.geometry("500x500")
juejuegosudoku.withdraw()

root.mainloop()