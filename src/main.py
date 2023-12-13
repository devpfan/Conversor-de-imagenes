import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk


class EditorFotos:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor v0.1b")

        self.root.iconbitmap(os.path.join(os.path.dirname(__file__), "tijera.ico"))

        self.imagen_original = None
        self.imagen_procesada = None
        self.img_tk = None  # esta variable de instancia almacena la imagen tkinter
        self.factor_zoom = 1.0  # el zoom inicial

        self.configurar_interfaz()

    def configurar_interfaz(self):
        # configurar estilo
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#ccc")

        # Configurar fondo
        frame_superior = tk.Frame(self.root, bg="#333")  # Cambiar el color de fondo
        frame_superior.pack(fill=tk.X)

        # Configurar barra superior
        label_titulo = tk.Label(frame_superior, text="Reducir el tamaño", font=("Arial", 14), fg="white",
                                bg="#333")  # Cambiar fuente, tamaño y color
        label_titulo.grid(row=0, column=0, padx=10)

        # Configurar botones
        boton_cargar = ttk.Button(frame_superior, text="Cargar Imagen", command=self.cargar_imagen)
        boton_cargar.grid(row=0, column=1, padx=10)

        boton_redimensionar = ttk.Button(frame_superior, text="Cambiar Tamaño", command=self.redimensionar_imagen)
        boton_redimensionar.grid(row=0, column=2, padx=10)

        boton_guardar = ttk.Button(frame_superior, text="Guardar", command=self.guardar_imagen)
        boton_guardar.grid(row=0, column=3, padx=10)

        # Botón para abrir la ventana "Acerca de"
        boton_acerca_de = ttk.Button(frame_superior, text="Acerca de", command=self.mostrar_acerca_de)
        boton_acerca_de.grid(row=0, column=4, padx=10)

        # Crear un lienzo (Canvas) para mostrar la imagen
        self.canvas = tk.Canvas(self.root, background="white", highlightthickness=0)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        # eventos del mouse para hacer el zoom out
        self.canvas.bind("<MouseWheel>", self.zoom)
        self.canvas.bind("<Control-MouseWheel>", self.zoom)

    def cargar_imagen(self):
        ruta_archivo = filedialog.askopenfilename()

        self.imagen_original = Image.open(ruta_archivo)
        self.imagen_procesada = self.imagen_original.copy() # para mantener la imagen original sin cambios

        self.mostrar_imagen()

    def redimensionar_imagen(self):
        if self.imagen_original is not None:
            confirmacion = tk.messagebox.askyesno("Confirmar","Desea cambiar el tamaño de la imagen")
            if confirmacion:
                nueva_ancho = 300
                relacion_aspecto = self.imagen_original.width / self.imagen_original.height
                nueva_altura = int(nueva_ancho / relacion_aspecto)

                self.imagen_procesada = self.imagen_original.resize((nueva_ancho, nueva_altura), Image.LANCZOS)

                # reestablece el zoom al predeterminado despues de cambiar el tamaño
                self.factor_zoom = 1.0

                self.mostrar_imagen()


if __name__ == "__main__":
    root = tk.Tk()
    editor = EditorFotos(root)
    root.mainloop()
