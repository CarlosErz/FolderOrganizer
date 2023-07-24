import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import customtkinter
import os
import shutil
import json
from PIL import Image

FOLDERS = {
    '.txt': 'Textos',
    '.doc': 'DocumentosWord',
    '.xlsx': 'ArchivosExcel',
    '.pdf': 'PDF',
    '.jpg': 'Imagenes',
    '.png': 'Imagenes',
    '.jpeg': 'Imagenes',
    '.gif': 'Imagenes',
    '.bmp': 'Imagenes',
    '.ico': 'Imagenes',
    '.svg': 'Imagenes',
    '.psd': 'Photoshop',
    '.tif': 'Imagenes',
    '.tiff': 'Imagenes',
    '.raw': 'Imagenes',
    '.cr2': 'Imagenes',
    '.nef': 'Imagenes',
    '.pef': 'Imagenes',
    '.eps': 'Imagenes',
    '.mp3': 'Musica',
    '.wav': 'Musica',
    '.wma': 'Musica',
    '.mid': 'Musica',
    '.midi': 'Musica',
    '.ogg': 'Musica',
    '.aac': 'Musica',
    '.ac3': 'Musica',
    '.flac': 'Musica',
    '.aym': 'Musica',
    '.mp4': 'Videos',
    '.avi': 'Videos',
    '.mkv': 'Videos',
    '.mov': 'Videos',
    '.mpg': 'Videos',
    '.mpeg': 'Videos',
    '.m4v': 'Videos',
    '.h264': 'Videos',
    '.wmv': 'Videos',
    '.rmvb': 'Videos',
    '.vob': 'Videos',
    '.3gp': 'Videos',
    '.3g2': 'Videos',
    '.asf': 'Videos',
    '.flv': 'Videos',
    '.swf': 'Videos',
    '.rm': 'Videos',
    '.f4v': 'Videos',
    '.m4p': 'Videos',
    '.m4b': 'Videos',
    '.m4r': 'Videos',
    '.mpg': 'Videos',
    '.mp2': 'Videos',
    '.exe': 'Programas',
    '.msi': 'Programas',
    '.bat': 'Programas',
    '.com': 'Programas',
    '.bin': 'Programas',
    '.jar': 'Programas',
    '.py': 'Programas',
    '.pyc': 'Programas',
    '.pyw': 'Programas',
    '.pyo': 'Programas',
    '.pyd': 'Programas',
    '.pyz': 'Programas',
    '.pyzw': 'Programas',
    '.ttf': 'Fuentes',
    '.otf': 'Fuentes',
    '.zip': 'Comprimidos',
    '.rar': 'Comprimidos',
    '.7z': 'Comprimidos',
    '.tar': 'Comprimidos',
    '.gz': 'Comprimidos',
    '.bz2': 'Comprimidos',
    '.xz': 'Comprimidos',
    '.iso': 'Comprimidos',
    '.dmg': 'Comprimidos',
    '.vcd': 'Comprimidos',
    '.wim': 'Comprimidos',
    '.swm': 'Comprimidos',
    '.e01': 'Comprimidos',
    '.esd': 'Comprimidos',
    '.001': 'Comprimidos',
    '.002': 'Comprimidos',
    '.003': 'Comprimidos',
    '.ai': 'Illustrator',
    '.indd': 'InDesign',
    '.dwg': 'AutoCAD',
    '.dxf': 'AutoCAD',
    '.docx': 'DocumentosWord',
    '.ppt': 'PowerPoint',
    '.pptx': 'PowerPoint',
    '.pps': 'PowerPoint',
    '.ppsx': 'PowerPoint',
    '.odp': 'PowerPoint',
    '.key': 'Keynote',
    '.gslides': 'GoogleSlides',
    '.csv': 'ArchivosExcel',
    '.xls': 'ArchivosExcel',
    '.xlsx': 'ArchivosExcel',
    '.numbers': 'Numbers',
    '.xlsm': 'ArchivosExcel',
    '.ods': 'ArchivosExcel',
    '.xlr': 'ArchivosExcel',
    '.accdb': 'Access',
    '.accde': 'Access',
    '.accdr': 'Access',
    '.pub': 'Publisher',
    '.vsd': 'Visio',
    '.vsdx': 'Visio',
    '.odg': 'Draw',
    '.odf': 'Draw',
    '.txt': 'Textos',
    '.rtf': 'Textos',
    '.odt': 'Textos',
    '.tex': 'Textos',
    '.wpd': 'Textos',
    '.wps': 'Textos',
    '.msg': 'Outlook',
    '.eml': 'Outlook',
    '.pst': 'Outlook',
    '.vcf': 'Outlook',
    '.ics': 'Outlook',
    '.db': 'BaseDatos',
    '.sql': 'BaseDatos',
    '.dbf': 'BaseDatos',
    '.mdb': 'BaseDatos',
    '.mdf': 'BaseDatos',
    '.iso': 'Disco',
    '.toast': 'Disco',
    '.vcd': 'Disco',
    '.dmg': 'Disco',
    '.img': 'Disco',
    '.bin': 'Disco',
    '.cue': 'Disco',
    '.mds': 'Disco',
    '.mdx': 'Disco',
    '.nrg': 'Disco',
    '.pdi': 'Disco',
    '.vmdk': 'Disco',
    '.vhd': 'Disco',
    '.vdi': 'Disco',
    '.tmp': 'Temporales',
    '.bak': 'Temporales',
    '.log': 'Temporales',
    '.old': 'Temporales',
    '.cab': 'Temporales',
    '.ics': 'Temporales',
    '.msi': 'Temporales',
    '.tmp': 'Temporales',
    '.part': 'Temporales',
    '.asd': 'Temporales',
    '.crdownload': 'Temporales',
    '.iso': 'ISO',
    '.torrent': 'Torrents',
    '.url': 'Enlaces',
    '.lnk': 'Enlaces',
    '.html': 'HTML',
    '.htm': 'HTML',
    '.css': 'CSS',
    '.js': 'JavaScript',
    '.php': 'PHP',
    '.asp': 'ASP',
    '.aspx': 'ASP',
    '.jsp': 'JSP',
    '.xml': 'XML',
    '.json': 'JSON',
    '.c': 'C',
    '.cpp': 'C++',
    '.cs': 'C#',
    '.java': 'Java',
    '.class': 'Java',
    '.vb': 'VisualBasic',
    '.vbs': 'VisualBasic',
    '.f': 'Fortran',
    '.f90': 'Fortran',
    '.f95': 'Fortran',
    '.f03': 'Fortran',
    '.f08': 'Fortran',
    '.f77': 'Fortran',
    '.f2k': 'Fortran',
    '.f23': 'Fortran',
    '.fpp': 'Fortran',
    '.fpp': 'Fortran',
    '.fpp': 'Fortran',
    '.fpp': 'Fortran',
    '.fpp': 'Fortran',
    '.fpp': 'Fortran',
    '.fpp': 'Fortran',
    '.fpp': 'Fortran',
    '.fpp': 'Fortran',
    '.fpp': 'Fortran',
    '.fpp': 'Fortran',
    '.go': 'Go',
    '.lua': 'Lua',
    '.pl': 'Perl',
    '.py': 'Python',
    '.rb': 'Ruby',
    '.sh': 'Shell',
    '.bat': 'Batch',
    '.cmd': 'Batch',
    '.ps1': 'PowerShell',
    '.psm1': 'PowerShell',
    '.psd1': 'PowerShell',
    '.ps1xml': 'PowerShell',
    '.psc1': 'PowerShell',
    '.pssc': 'PowerShell',
    '.msh': 'PowerShell',
    '.msh1': 'PowerShell',
    '.msh2': 'PowerShell',
    '.mshxml': 'PowerShell',
    '.msh1xml': 'PowerShell',
    '.msh2xml': 'PowerShell',
    '.scf': 'PowerShell',
    '.wsf': 'PowerShell',
    '.cpl': 'PowerShell',
    '.msc': 'PowerShell',
    '.jar': 'Java',
    '.war': 'Java',
    '.ear': 'Java',
    '.java': 'Java',
    '.class': 'Java',
    '.apk': 'EjecutableAndroid',
    '.ipa': 'EjecutableiOS',
    '.kmz': 'GoogleEarth',
    '.kml': 'GoogleEarth',
    '.xap': 'WindowsPhone',
    '.xap': 'WindowsPhone',
    '.xap': 'WindowsPhone',
}
# Lista para mantener el historial de acciones realizadas
history = []
folder_names = list(FOLDERS.values())


def show_folders_and_extensions():
    #crear una nueva ventama para mostrar las carpetas y extensiones
    extensions_window = customtkinter.CTkToplevel(app)
    extensions_window.title("Folders and Extensions")

    # crear un diccionario con las carpetas y sus extensiones
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


def filter_folders(folders):
    # Crea un nuevo diccionario con nombres de carpeta únicos
    unique_folders = {}
    for ext, folder_name in folders.items():
        unique_folders[folder_name] = ext
    return unique_folders


def getDataConfigJson(nameFile):
    with open(nameFile) as fileJson:
        dataFile = fileJson.read()
    return json.loads(dataFile)


def checkAddress(address):
    return address if address[-1] == "\\" else address + "\\"


def open_config_file():
    folder_path = filedialog.askdirectory(
        title="Seleccionar carpeta de archivos")
    if folder_path:
        folder_address = checkAddress(folder_path)
        perform_classification(folder_address)


def getContentFolder(srcFolder):
    if os.path.isdir(srcFolder):
        return os.listdir(srcFolder)
    raise ValueError("La carpeta no existe.")


def cleanArrayFiles(files, folder_address):
    return [
        f for f in files if os.path.isfile(os.path.join(folder_address, f))
        and f.lower() != 'desktop.ini'
    ]


def getExtension(filesName):
    return os.path.splitext(filesName)[1]


def getFolder(extension):
    return FOLDERS.get(extension, 'Otros')


def getFilesAndFolders(files, folder_address):
    return {
        os.path.join(folder_address, fileName):
        os.path.join(folder_address, getFolder(getExtension(fileName)))
        for fileName in files
    }


def cleanDictionaryFiles(files):
    newFiles = {}
    for file, folder in files.items():
        if folder != "":
            newFiles[file] = folder
    return newFiles


def createFolder(name):
    if not os.path.isdir(name):
        os.mkdir(name)


def show_message(title, message, message_type="info"):
    if message_type == "info":
        messagebox.showinfo(title, message)
    elif message_type == "warning":
        messagebox.showwarning(title, message)
    elif message_type == "error":
        messagebox.showerror(title, message)


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
        show_message(
            "Error",
            f"Error al mover el archivo '{os.path.basename(fileName)}': {str(e)}",
            message_type="error")


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


def createFoldersAndMoveFiles(filesAndFolders):
    for file, folder in filesAndFolders.items():
        os.makedirs(folder, exist_ok=True)
        moveFile(file, folder)


def center_window(app, width, height):
    # Obtener el tamaño de la pantalla del usuario
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    # Calcular las coordenadas (x, y) para centrar la ventana
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Establecer el tamaño y la posición de la ventana
    app.geometry(f"{width}x{height}+{x}+{y}")


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

        #funcion de ocultar texto por 3 segundos
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
        open_button.config(state=tk.NORMAL)
        loading_label.place(relx=0.5, rely=0.4, anchor='center')
        #ocultar label de texto despues de 3 segundos
        app.after(3000, hide_loading_label)


def show_folders():
    show_folders_and_extensions()


def edit_folders():

    def save_changes():
        selected_folder = combo_folder.get()
        new_name = entry_name.get()

        if selected_folder not in FOLDERS:
            show_message(
                "Error",
                f"La carpeta '{selected_folder}' no existe en el diccionario.",
                message_type="error")
            return

        FOLDERS[new_name] = FOLDERS.pop(selected_folder)
        combo_folder.set(new_name)

        edit_window.destroy()

    filtered_folders = filter_folders(FOLDERS)
    edit_window = customtkinter.CTkToplevel(app)
    edit_window.title("Editar Carpetas")
    customtkinter.set_appearance_mode("Dark")
    float_value = 1.0
    edit_window.config(width=window_width, height=window_height)

    customtkinter.set_default_color_theme("green")
    customtkinter.set_widget_scaling(
        float_value)  # widget dimensions and text size
    customtkinter.set_window_scaling(float_value)

    label_folder = customtkinter.CTkLabel(edit_window, text="Carpeta:")
    label_folder.pack(pady=10)

    combo_folder = customtkinter.CTkComboBox(edit_window,
                                             values=list(
                                                 filtered_folders.keys()),
                                             state="readonly",
                                             font=("Arial", 11, "bold"))

    combo_folder.pack(pady=5)

    label_name = customtkinter.CTkLabel(edit_window, text="Nuevo Nombre:")
    label_name.pack(pady=5)

    entry_name = customtkinter.CTkEntry(edit_window)
    entry_name.pack(pady=5)

    button_save = customtkinter.CTkButton(edit_window,
                                          text="Guardar Cambios",
                                          command=save_changes,
                                          font=(
                                              "Arial",
                                              16,
                                              "bold",
                                          ))
    button_save.pack(pady=10)


app = customtkinter.CTk()
app.title("Clasificador de archivos")
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
# Establecer el tamaño de la ventana
window_width = 600
window_height = 400
carpeta_principal = os.path.dirname(__file__)
img = os.path.join(carpeta_principal, "img")

# Cambiar el color de fondo de toda la ventana, incluida la franja de título
app.config(width=window_width, height=window_height)
app.option_add('*Dialog.msg.font', 'Helvetica 12')

option_folder_img = customtkinter.CTkImage(
    dark_image=Image.open(os.path.join(img, "option_folder.png")),
    size=(30, 30),
)
extensions = customtkinter.CTkImage(
    dark_image=Image.open(os.path.join(img, "extensiones.png")),
    size=(25, 25),
)

agg = tk.PhotoImage(
    #dark_image=Image.open(os.path.join(img, "agg.png")),
    file=os.path.join(img, "agg.png"),

    # size=(50, 50),
)
agg = agg.subsample(4, 4)

# Centrar la ventana en la pantalla
center_window(app, window_width, window_height)

style = ttk.Style()


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


# Crear el botón utilizando ttk.Button
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

#option_folder = customtkinter.CTkButton(
# app,
#text="Editar carpetas",
#Efont=('Arial', 10, 'bold'),
#text_color='#FFFFFF',
# bg_color='#2C2C2C',
#corner_radius=10,
#padx=30,
#pady=10,
#bd=1,
#image=option_folder_img,
#command=edit_folders)

showfolder = customtkinter.CTkButton(app,
                                     text="Carpetas y extensiones",
                                     font=('Arial', 10, 'bold'),
                                     text_color='#FFFFFF',
                                     bg_color='#2C2C2C',
                                     corner_radius=10,
                                     image=extensions,
                                     command=show_folders)

# Configurar el evento para cambiar el color de fondo al hacer hover
open_button.bind('<Enter>', on_enter)
open_button.bind('<Leave>', on_leave)
undo_button.bind('<Enter>', undo_enter)
undo_button.bind('<Leave>', undo_leave)
# Cambiar el cursor a "pointer" (mano) al hacer hover
open_button.config(cursor='hand2')
undo_button.config(cursor='hand2')
# Colocar el botón en la ventana
#option_folder.place(
#   relx=0.2,
#  rely=0.8,
# anchor='center',
#)
showfolder.place(
    relx=0.2,
    rely=0.8,
    anchor='center',
)
#open_button.pack(side='top', anchor='center', pady=10)
open_button.place(relx=0.5, rely=0.2, anchor='center')
undo_button.place(relx=0.5, rely=0.5, anchor='center')

app.mainloop()
