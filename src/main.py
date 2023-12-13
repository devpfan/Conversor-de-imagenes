import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk


class EditorFotos:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor v0.1b")

        self.root.iconbitmap(os.path.join(os.path.dirname(__file__), "tijera.ico"))






if __name__=="__main__":
    root = tk.Tk()
    editor = EditorFotos(root)
    root.mainloop()
