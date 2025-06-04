import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
import sys
from PIL import Image, ImageTk

class AutoPaintWindow:
    def __init__(self, callback_on_file_drop=None):
        self.root = TkinterDnD.Tk()
        self.root.title("AutoPaint - Selecione sua planilha")
        self.root.geometry("600x300")
        self.root.resizable(False, False)

        # Corrigir caminho do ícone (funciona com PyInstaller também)
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(__file__)

        icon_path = os.path.join(base_path, 'assets', 'icon.ico')
        drop_icon_path = os.path.join(base_path, 'assets', 'drop_icon.png')

        try:
            self.root.iconbitmap(icon_path)
        except Exception as e:
            print(f"Erro ao definir ícone: {e}")

        self.callback_on_file_drop = callback_on_file_drop

        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(expand=True, fill="both")

        # Imagem e botão
        try:
            img = Image.open(drop_icon_path)
            img = img.resize((120, 120), Image.Resampling.LANCZOS)
            self.tk_img = ImageTk.PhotoImage(img)

            # Um único label com imagem, click e drop
            self.image_label = ttk.Label(self.frame, image=self.tk_img, cursor="hand2")
            self.image_label.pack(pady=10)
            self.image_label.bind("<Button-1>", self.open_file_picker)

            # Área de drop
            self.image_label.drop_target_register(DND_FILES)
            self.image_label.dnd_bind('<<Drop>>', self.on_file_drop)
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")

        # Texto abaixo da imagem
        self.label = ttk.Label(
            self.frame,
            text="Arraste um arquivo .xlsx aqui ou clique na imagem para selecionar",
            font=("Arial", 12)
        )
        self.label.pack()

        # Também permitir drop no label de texto
        self.label.drop_target_register(DND_FILES)
        self.label.dnd_bind('<<Drop>>', self.on_file_drop)

    def open_file_picker(self, event=None):
        filepath = filedialog.askopenfilename(
            filetypes=[("Planilhas do Excel", "*.xlsx")]
        )
        if filepath:
            self.process_file(filepath)

    def on_file_drop(self, event):
        filepath = event.data.strip('{}')
        self.process_file(filepath)

    def process_file(self, filepath):
        if not filepath.lower().endswith('.xlsx'):
            messagebox.showerror("Erro", "Por favor, insira um arquivo Excel (.xlsx).")
            return

        self.label.config(text=f"Arquivo recebido:\n{os.path.basename(filepath)}")

        if self.callback_on_file_drop:
            self.callback_on_file_drop(filepath)

    def run(self):
        self.root.mainloop()
