import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
import time

#Arreglo sudokupredefinido - Con el uso de una api obtendremos un arreglo con el sudoku a trabajar
response = requests.get("https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value,difficulty}}}")
print(response.status_code)
# print(response.json())
Sudoku = response.json()['newboard']['grids'][0]['value']
dificultad = response.json()['newboard']['grids'][0]['difficulty']


#Sudoku = [
#    [0,0,1,0,3,4,0,0,6],
#    [0,4,0,0,0,2,5,8,0],
#    [0,5,0,1,8,0,0,4,0],
#    [1,3,2,0,4,0,0,0,0],
#    [0,0,0,0,1,6,0,0,0],
#    [7,6,4,8,5,0,0,2,0],
#    [0,0,0,3,9,1,0,5,8],
#    [9,1,0,7,0,8,4,0,0],
#    [6,0,0,4,2,0,0,0,7]
#    ]

# Función para mostrar la solución del Sudoku
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


# Función para resolver el Sudoku
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

class SudokuGame:
    
    def __init__(self, juejuegosudoku):        
        juejuegosudoku.deiconify() #Muestra el segundo panel
        root.withdraw()#elimina el segundo panel

        self.juejuegosudoku = juejuegosudoku # widget principal
        self.juejuegosudoku.title("Juego de Sudoku") # Titulo
        self.board = Sudoku  # Genera tablero vacio
        self.solution = [row[:] for row in self.board]  # Copia el tablero vacio
        resolver_sudoku(self.solution)  # Resuelve el tablero y guarda la solución
        imprimir_Sudoku(self.solution)
        self.cells = {}  # Diccionario para almacenar las celdas
        self.timer_label = tk.Label(self.juejuegosudoku, text="Tiempo: 00:00" , font=("Arial", 16)) # Muestra el tiempo 
        self.timer_label.pack()
        self.start_time = time.time()  # Tiempo de inicio del juego
        self.create_ui()  # Crea la interfaz de usuario
        self.update_timer()  # Actualiza el temporizador

    def create_ui(self):
        frame = tk.Frame(self.juejuegosudoku)
        frame.pack()
        canvas = tk.Canvas(frame, width=450, height=450) #para las lineas de separacion
        canvas.pack()
        cell_size = 50 #Tamaño de las lineas predeterminado

        for i in range(9):
            for j in range(9):
                x1, y1 = j * cell_size, i * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                cell = tk.Entry(frame, width=2, font=("Arial", 18), justify="center")
                cell.place(x=x1 + 5, y=y1 + 5, width=cell_size - 10, height=cell_size - 10)
                cell.insert(0, str(self.board[i][j]) if self.board[i][j] != 0 else "")
                cell.bind("<FocusOut>", self.check_solution)
                self.cells[(i, j)] = cell

                # Validación de entrada
                validate_cmd = (self.juejuegosudoku.register(self.validate_entry), '%P', '%W')
                cell.config(validate="key", validatecommand=validate_cmd)

        # Dibujar líneas de separación
        for i in range(10):
            line_width = 3 if i % 3 == 0 else 1
            canvas.create_line(0, i * cell_size, 450, i * cell_size, width=line_width, fill="sky blue")
            canvas.create_line(i * cell_size, 0, i * cell_size, 450, width=line_width, fill="sky blue")

    # Tiempo 
    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        self.timer_label.config(text=f"Tiempo: {minutes:02}:{seconds:02}" + " Tiempo Limite: 05:00")
        self.juejuegosudoku.after(1000, self.update_timer) # Actualiza cada segundo

    #Revisa las casillas que esten bien 
    def check_solution(self, event):
        for (i, j), cell in self.cells.items():
            value = cell.get()
            if value.isdigit():
                value = int(value)
                if self.solution[i][j] == value:
                    cell.config(bg="light green")
                else:
                    cell.config(bg="light coral")
            else:
                cell.config(bg="white")

    # Hace la validacion de la casilla 
    def validate_entry(self, value, widget_name):
        if value.isdigit() or value == "":
            return True
        else:
            self.show_error(widget_name)
            return False
        
    # Muestra mensaje de error
    def show_error(self, widget_name):
        widget = self.juejuegosudoku.nametowidget(widget_name)
        widget.delete(0, tk.END)
        messagebox.showerror("Entrada inválida", "Por favor, ingrese solo números del 1 al 9.")





# def Segundo_paneljuego():
#     global Sudoku
#     juejuegosudoku.deiconify() #Muestra el segundo panel
#     root.withdraw()#elimina el segundo panel

#     # Resolver Sudoku
#     # if resolver_sudoku(Sudoku):
#     #     imprimir_Sudoku(Sudoku)
#     # else:
#     #     print("No se encontró solución")

#     # recorrer el arreglo del sudoku
#     for i in range(9):
#         for j in range(9):
#             if Sudoku[i][j] == 0:
#                 label = tk.Label(juejuegosudoku, text=" ", width=4, height=2, font=('bell', 10), bg="#659DCC")
#             else:
#                 label = tk.Label(juejuegosudoku, text=str(Sudoku[i][j]), width=4, height=2, font=('bell', 10))
#             label.grid(row=i, column=j, padx=1, pady=1)

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


#Llamado al segundo panel, aca lo crea al panel 
juejuegosudoku = tk.Toplevel()
juejuegosudoku.title("Sudoku")
juejuegosudoku.geometry("700x500")
juejuegosudoku.deiconify()
juejuegosudoku.withdraw()

# Función para iniciar el juego
def start_game():
    SudokuGame(juejuegosudoku)

start_button = tk.Button(root, text="START GAME", font=("Bell", 14), bg="#6495ED", fg="white", command=start_game)
start_button.place(x=180, y=440)

root.mainloop()