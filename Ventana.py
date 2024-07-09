import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import time

# Tableros
sudoku_facil = [
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

sudoku_medio = [
    [0,3,0,0,0,0,5,4,0],
    [9,2,4,6,0,0,0,0,1],
    [7,8,0,2,1,4,9,0,3],
    [0,4,3,0,0,0,0,0,9],
    [0,0,0,0,0,0,4,2,8],
    [0,6,9,0,4,0,0,0,0],
    [1,7,2,0,3,0,0,0,0],
    [0,5,0,9,6,0,2,0,4],
    [0,0,6,0,0,8,3,0,0]
]

sudoku_dificil = [
    [6,0,0,0,0,0,0,0,5],
    [0,3,0,5,2,0,0,0,0],
    [0,0,0,0,4,6,9,0,0],
    [0,7,2,0,0,5,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,6,0,0,0,2,0],
    [0,0,0,0,0,0,0,0,0],
    [0,4,3,0,0,0,2,0,0],
    [0,0,0,0,0,0,0,8,0]
]


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


# Panel de dificultades
class SudokuLevel:
    def __init__(self, panel_main):
        self.panel_main = panel_main

        self.panel_main.deiconify()
        self.panel_main.title("Selector de dificultad")

        self.fondo_imagen = ImageTk.PhotoImage(Image.open("./resources/Fondo niveles.jpg"))

        self.fondo = tk.Label(self.panel_main, image=self.fondo_imagen)
        self.indicaciones = tk.Label(self.panel_main, text="SELECCIONA EL NIVEL DE DIFICULTAD", font=("Arial", 14), bg="#007ffc", fg="white")

        self.facil = tk.Button(self.panel_main, text="FACIL", font=("Bell", 16), bg="#6495ED", fg="white", command=self.nivel_facil)
        self.medio = tk.Button(self.panel_main, text="MEDIO", font=("Bell", 16), bg="#6495ED", fg="white", command=self.nivel_medio)
        self.dificil = tk.Button(self.panel_main, text="DIFICIL", font=("Bell", 16), bg="#6495ED", fg="white", command=self.nivel_dificil)

        self.fondo.place(x=0, y=0, relwidth=1, relheight=1)
        self.indicaciones.place(x=10, y=25)
        self.facil.place(x=171, y=70)
        self.medio.place(x=168, y=120)
        self.dificil.place(x=165, y=170)

    def crearframejuego(self, dificultad):
        juejuegosudoku = tk.Toplevel()
        juejuegosudoku.title("Sudoku")
        centrar_ventana(juejuegosudoku, 700, 500)
        juejuegosudoku.overrideredirect(True)
        juejuegosudoku.withdraw()
        SudokuGame(juejuegosudoku, dificultad)

    def cerrarframe(self):
        self.panel_main.destroy()

    def nivel_facil(self):
        self.crearframejuego(sudoku_facil)
        self.cerrarframe()

    def nivel_medio(self):
        self.crearframejuego(sudoku_medio)
        self.cerrarframe()

    def nivel_dificil(self):
        self.crearframejuego(sudoku_dificil)
        self.cerrarframe()


# Panel del Juego Sudoku
class SudokuGame:
    def __init__(self, juejuegosudoku, dificultad):
        juejuegosudoku.deiconify()  # Muestra el segundo panel
        root.withdraw()  # Elimina el segundo panel

        self.juejuegosudoku = juejuegosudoku  # widget principal
        self.dificultad = dificultad
        self.juejuegosudoku.title("Juego de Sudoku")  # Titulo
        self.board = self.dificultad  # Genera tablero vacio
        self.solution = [row[:] for row in self.board]  # Copia el tablero vacio

        self.fondo_imagen = ImageTk.PhotoImage(Image.open("./resources/Fondo Juego.jpg"))
        self.fondo = tk.Label(self.juejuegosudoku, image=self.fondo_imagen)
        self.fondo.place(x=0, y=0, relwidth=1, relheight=1)

        resolver_sudoku(self.solution)  # Resuelve el tablero y guarda la solución
        imprimir_Sudoku(self.solution)

        self.cells = {}  # Diccionario para almacenar las celdas
        self.timer_label = tk.Label(self.juejuegosudoku, text="Tiempo: 00:00" , font=("Arial", 16)) # Muestra el tiempo
        self.timer_label.pack()
        self.start_time = time.time()  # Tiempo de inicio del juego
        self.create_ui()  # Crea la interfaz de usuario
        self.update_timer()  # Actualiza el temporizador

        self.verificar_ = tk.Button(self.juejuegosudoku, text="VERIFICAR", font=("Bell", 12), bg="#6495ED", fg="white", command=self.verify_game)
        self.exit_ = tk.Button(self.juejuegosudoku, text="EXIT", font=("Bell", 14), bg="#6495ED", fg="white", command=self.exit_game)

        self.verificar_.place(x=590, y=390)
        self.exit_.place(x=606, y=440)

    def create_ui(self):
        frame = tk.Frame(self.juejuegosudoku)
        frame.pack()
        canvas = tk.Canvas(frame, width=450, height=450)  # para las lineas de separacion
        canvas.pack()
        cell_size = 50  # Tamaño de las lineas predeterminado

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

    def exit_game(self):
        tiempo_actual = self.update_timer()
        if tiempo_actual < 300:
            res = messagebox.askyesno("Salir de la partida", "¿Está seguro de salir de la partida?\nAún le queda tiempo de juego")
            if res:
                self.juejuegosudoku.destroy()
                root.deiconify()
        return

    def verify_game(self):
        for (i,j), cell in self.cells.items():
            if cell["bg"] != "light green":
                self.check_solution("<FocusOut>")
                return
            else:
                self.check_solution("<FocusOut>")
                ans = messagebox.showinfo("Éxito", "Felicidades has completado el Sudoku :D!")
                if ans == "ok":
                    self.juejuegosudoku.destroy()
                    root.deiconify()
                return

    # Tiempo 
    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        if elapsed_time > 300:
            res = messagebox.showerror("Game Over", "Tiempo Cumplido :(")
            if res == "ok":
                self.exit_game()
                return

        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        self.timer_label.config(text=f"Tiempo: {minutes:02}:{seconds:02}" + " Tiempo Limite: 05:00")
        self.juejuegosudoku.after(1000, self.update_timer)  # Actualiza cada segundo
        return elapsed_time

    # Revisa las casillas que esten bien
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


# Panel principal
def centrar_ventana(frame, ancho, altura):
    # Obtén el ancho y alto de la pantalla
    screen_width = frame.winfo_screenwidth()
    screen_height = frame.winfo_screenheight()

    # Calcula la posición x y y para centrar la ventana
    x = (screen_width // 2) - (ancho // 2)
    y = (screen_height // 2) - (altura // 2)

    # Establece la geometría de la ventana
    frame.geometry(f'{ancho}x{altura}+{x}+{y}')

# Instancia panel dificultades
def start_game():
    dificultad_sudoku = tk.Toplevel()
    dificultad_sudoku.title("Sudoku")
    centrar_ventana(dificultad_sudoku, 400, 300)
    dificultad_sudoku.overrideredirect(True)
    dificultad_sudoku.withdraw()

    SudokuLevel(dificultad_sudoku)


# Cerrar Juego
def exit_game():
    ans = messagebox.askyesno("Salir del juego", "¿Está seguro de salir del juego?")
    if ans:
        root.destroy()


root = tk.Tk()
root.title("Sudoku")
centrar_ventana(root, 500, 500)
root.overrideredirect(True)

icon_image = ImageTk.PhotoImage(Image.open("./resources/sudoku.ico"))
background_image = ImageTk.PhotoImage(Image.open("./resources/Fondo.jpeg"))
background_label = tk.Label(root, image=background_image)
root.iconphoto(True, icon_image)

title_label = tk.Label(root, text="SUDOKU", font=("Bell", 30), bg = "#659DCC",fg="white")
start_button = tk.Button(root, text="START GAME", font=("Bell", 14), bg="#6495ED", fg="white", command=start_game)
close_button = tk.Button(root, text="EXIT", font=("Bell", 14), bg="#6495ED", fg="white", command=exit_game)

background_label.place(x=0, y=0, relwidth=1, relheight=1)
title_label.place(x=150, y=80)
start_button.place(x=180, y=440)
close_button.place(x=400, y=440)

root.mainloop()
