import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk 

def start_game():
    print("El juego ha comenzado")


root = tk.Tk()
root.title("Sudoku")
root.geometry("3000x2000")


background_image = ImageTk.PhotoImage(Image.open("./resources/Principal.jpeg"))

background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Establecer la imagen de fondo en toda la ventana


title_label = tk.Label(root, text="SUDOKU", font=("Arial", 40), bg="#FFFFFF")
title_label.place(x=720, y=220)


start_button = tk.Button(root, text="START GAME", font=("Arial", 14), bg="#6495ED", fg="white", command=start_game)
start_button.place(x=720, y=650)

root.mainloop()