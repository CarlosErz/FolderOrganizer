import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter
import os
from PIL import Image
from Logic_folders import * 
from app_config import *

# Configuración de la ventana
w = window_width 
h = window_height
carpeta_principal = os.path.dirname(__file__)
img = os.path.join(carpeta_principal, "img")

agg = tk.PhotoImage(
    #dark_image=Image.open(os.path.join(img, "agg.png")),
    file=os.path.join(img, "agg.png"),

    # size=(50, 50),
)
agg = agg.subsample(4, 4)

extensions = customtkinter.CTkImage(
    dark_image=Image.open(os.path.join(img, "extensiones.png")),
    size=(25, 25),
)

# Funciones relacionadas con la interfaz gráfica
def on_enter(event):
    # Cambiar el color de fondo cuando el cursor entra al botón
    open_button.config(background='#2ECC71', foreground='white')

def on_leave(event):
    # Cambiar el color de fondo cuando el cursor sale del botón
    open_button.config(background='#5F43D3', foreground='white')

def undo_leave(event):
    # Cambiar el color de fondo cuando el cursor sale del botón
    undo_button.config(background='#F54242', foreground='white')

def undo_enter(event):
    # Cambiar el color de fondo cuando el cursor sale del botón
    undo_button.config(background='#AE0F0F', foreground='white')

def center_window(app, width, height):
    # Obtener el tamaño de la pantalla del usuario
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    # Calcular las coordenadas (x, y) para centrar la ventana
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Establecer el tamaño y la posición de la ventana
    app.geometry(f"{width}x{height}+{x}+{y}")
def checkAddress(address):
    return address if address[-1] == "\\" else address + "\\"

def open_config_file():
    folder_path = filedialog.askdirectory(
        title="Seleccionar carpeta de archivos")
    if folder_path:
        folder_address = checkAddress(folder_path)
        perform_classification(folder_address)

def show_folders():
    show_folders_and_extensions(app, FOLDERS)
    

# Crear la ventana principal
app = ctk
title = ctk.title("Clasificador de archivos")
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

# Centrar la ventana en la pantalla
center_window(app, window_width, window_height)

# Crear los botones y etiquetas
open_button = tk.Button(app,
                        text="Selecciona una carpeta para organizar",
                        font=('Arial', 12, 'bold'),
                        foreground='#FFFFFF',
                        bg='#5F43D3',
                        padx=30,
                        pady=10,
                        image=agg,
                        compound=tk.LEFT,
                        bd=0,
                        command=open_config_file)

undo_button = tk.Button(app,
                        text="Deshacer toda la acción",
                        font=('Arial', 12, 'bold'),
                        foreground='#FFFFFF',
                        bg='#F54242',
                        padx=40,
                        pady=10,
                        bd=0,
                        command=undo_last_action)

labelfrom = customtkinter.CTkLabel(app,
                                   text="Creado @CarlosErz",
                                   fg_color="transparent")

showfolder = customtkinter.CTkButton(app,
                                     text="Carpetas y extensiones",
                                     font=('Arial', 10, 'bold'),
                                     text_color='#FFFFFF',
                                     bg_color='#2C2C2C',
                                     corner_radius=10,
                                     image=extensions,
                                     command=show_folders)

# Configurar eventos y estilosf
open_button.bind('<Enter>', on_enter)
open_button.bind('<Leave>', on_leave)
undo_button.bind('<Enter>', undo_enter)
undo_button.bind('<Leave>', undo_leave)

open_button.config(cursor='hand2')
undo_button.config(cursor='hand2')

# Colocar elementos en la ventana
showfolder.place(relx=0.2, rely=0.8, anchor='center')
open_button.place(relx=0.5, rely=0.2, anchor='center')
undo_button.place(relx=0.5, rely=0.5, anchor='center')
labelfrom.place(relx=0.5, rely=0.9, anchor='center')


app.mainloop()
