
import tkinter as tk
from tkinter import messagebox
import time
import random

class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Sudoku")
        self.board = self.create_board()
        self.solution = [row[:] for row in self.board]
        self.cells = {}
        self.timer_label = tk.Label(self.root, text="Tiempo: 00:00", font=("Arial", 16))
        self.timer_label.pack()
        self.start_time = time.time()
        self.create_ui()
        self.update_timer()

    def create_board(self):
        # Genera un tablero de Sudoku vacío
        return [[0] * 9 for _ in range(9)]

    def create_ui(self):
        frame = tk.Frame(self.root)
        frame.pack()
        for i in range(9):
            for j in range(9):
                cell = tk.Entry(frame, width=4, font=("Arial", 18), justify="center")
                cell.grid(row=i, column=j)
                cell.insert(0, str(self.board[i][j]) if self.board[i][j] != 0 else "")
                cell.bind("<FocusOut>", self.check_solution)
                self.cells[(i, j)] = cell

    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        self.timer_label.config(text=f"Tiempo: {minutes:02}:{seconds:02}")
        self.root.after(1000, self.update_timer)

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

if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()
