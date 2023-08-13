import os
import json
import shutil
from ConfigFolder import FOLDERS
from tkinter import messagebox
import tkinter as tk
import customtkinter
from app_config import *

history = []
folder_names = list(FOLDERS.values())
app = ctk


def read_json_file(file_path):
    with open(file_path) as file_json:
        data = file_json.read()
    return json.loads(data)

#obtener la ruta de la carpeta principal
def getFolder(extension):
    return FOLDERS.get(extension, 'Otros')

#oberner la extensión del archivo
def getExtension(filesName):
    return os.path.splitext(filesName)[1]

#limpar el array de archivos
def cleanArrayFiles(files, folder_address):
    return [
        f for f in files if os.path.isfile(os.path.join(folder_address, f))
        and f.lower() != 'desktop.ini'
    ]

#filtrar las carpetas
def filter_folders(folders):
    # Crea un nuevo diccionario con nombres de carpeta únicos
    unique_folders = {}
    for ext, folder_name in folders.items():
        unique_folders[folder_name] = ext
    return unique_folders

#obtener el contenido de la carpeta
def getContentFolder(srcFolder):
    if os.path.isdir(srcFolder):
        return os.listdir(srcFolder)
    raise ValueError("La carpeta no existe.")

#obtener los archivos y carpetas
def getFilesAndFolders(files, folder_address):
    return {
        os.path.join(folder_address, fileName):
        os.path.join(folder_address, getFolder(getExtension(fileName)))
        for fileName in files
    }

#limpiar los archivos del diccionario
def cleanDictionaryFiles(files):
    newFiles = {}
    for file, folder in files.items():
        if folder != "":
            newFiles[file] = folder
    return newFiles

#mover los archivos
def moveFile(fileName, folderName):
    try:
        if os.path.isdir(folderName):
            # Comprobar si el archivo ya existe en la carpeta destino
            destination_path = os.path.join(folderName,
                                            os.path.basename(fileName))
            if os.path.exists(destination_path):
                show_message(
                    "Advertencia",
                    f"El archivo '{os.path.basename(fileName)}' ya existe en la carpeta destino. No se realizará ninguna acción con ese archivo.",
                    message_type="warning")
                return
            history.append((fileName, destination_path))
            shutil.move(fileName, destination_path)

    except Exception as e:
        show_message("Error", f"Error al mover el archivo: {str(e)}", message_type="error")

#crear las carpetas y mover los archivos
def createFoldersAndMoveFiles(filesAndFolders):
    for file, folder in filesAndFolders.items():
        os.makedirs(folder, exist_ok=True)
        moveFile(file, folder)

#crear una carpeta
def createFolder(name):
    if not os.path.isdir(name):
        os.mkdir(name)

#funcion para los mensajes en windows 
def show_message(title, message, message_type="info"):
    if message_type == "info":
        messagebox.showinfo(title, message)
    elif message_type == "warning":
        messagebox.showwarning(title, message)
    elif message_type == "error":
        messagebox.showerror(title, message)

#funcion para realizar la clasificación de archivos
def perform_classification(folder_address):
    if not folder_address:
        return

    # Contenido de la carpeta en un array
    files = getContentFolder(folder_address)

    # Solo guardo los archivos. Elimino las carpetas del array
    files = cleanArrayFiles(files, folder_address)

    if len(files) > 0:
        # Obtengo los archivos con sus carpetas correspondientes y filtrados
        filesAndFolders = cleanDictionaryFiles(
            getFilesAndFolders(files, folder_address))

        # Mostrar animación de carga mientras se mueven los archivos
        loading_label = tk.Label(
            app,
            text="Moviendo archivos...",
            font=("Helvetica", 12),
            bg='#262626',
            fg='#FFFFFF',
            bd=0,
        )
        loading_label.pack(pady=10)
        progress_bar = customtkinter.CTkProgressBar(app, mode='indeterminate')
        progress_bar.pack(padx=20, pady=10)
        progress_bar.place(relx=0.5, rely=0.9, anchor='center')
        progress_bar.start()

        # Creo las carpetas y muevo los archivos
        createFoldersAndMoveFiles(filesAndFolders)

        # Función para ocultar el texto después de 3 segundos
        def hide_loading_label():
            loading_label.pack_forget()
            loading_label.destroy()

        # Detener animación de carga
        progress_bar.stop()
        progress_bar.pack_forget()
        progress_bar.destroy()
        messagebox.showinfo("Clasificación completa",
                            "Clasificación de archivos completada con éxito.")
        loading_label.config(
            text=
            "Clasificación de archivos completada. Cierre el programa o agregue otra carpeta.",
            foreground='#FFFFFF',
            bg='#262626',
            font=("Arial", 11, "bold"),
            bd=0)

        loading_label.place(relx=0.5, rely=0.4, anchor='center')
        # Ocultar etiqueta de texto después de 3 segundos
        app.after(3000, hide_loading_label)


# Función para deshacer la última acción de movimiento de archivos
def undo_last_action():
    global history
    if len(history) > 0:
        try:
            for src, dest in history:
                shutil.move(dest, src)
            history.clear()
            if len(history) == 0:
                show_message("Deshacer",
                             "Se han deshecho todas las acciones.",
                             message_type="info")
        except Exception as e:
            show_message("Error",
                         f"Error al deshacer las acciones: {str(e)}",
                         message_type="error")
    else:
        show_message("Deshacer",
                     "No hay acciones para deshacer.",
                     message_type="info")

#muestra las carpetas y extensiones
def show_folders_and_extensions(app, FOLDERS):
    # Crear una nueva ventana para mostrar las carpetas y extensiones
    extensions_window = customtkinter.CTkToplevel(app)
    extensions_window.title("Folders and Extensions")

    # Crear un diccionario con las carpetas y sus extensiones
    folders_with_extensions = {}

    for extension, folder in FOLDERS.items():
        if folder in folders_with_extensions:
            folders_with_extensions[folder].append(extension)
        else:
            folders_with_extensions[folder] = [extension]

    # Mostrar las carpetas y sus extensiones en el Listbox
    extensions_listbox = tk.Listbox(extensions_window,
                                    selectmode=tk.SINGLE,
                                    selectbackground='#5F43D3',
                                    selectforeground='#FFFFFF',
                                    font=("Arial", 11, "bold"),
                                    bg='#262626',
                                    fg='#FFFFFF',
                                    bd=0,
                                    width=50,
                                    height=20)
    extensions_listbox.pack()

    for folder, extensions in folders_with_extensions.items():
        extensions_listbox.insert(tk.END, f"{folder}: {', '.join(extensions)}")