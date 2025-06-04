from auto_paint.AutoPaintWindow import AutoPaintWindow
from auto_paint.AutoPaint import AutoPaint
from tkinter import messagebox

def handle_file_drop(filepath, janela):
    try:
        painter = AutoPaint(filepath)
        novo_arquivo = painter.processar()
        messagebox.showinfo("Sucesso", f"Arquivo salvo como:\n{novo_arquivo}")
        janela.root.destroy()  # Fecha a janela após o clique em OK
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar arquivo:\n{e}")

if __name__ == "__main__":
    # Inicializa a janela
    janela = AutoPaintWindow(callback_on_file_drop=lambda fp: handle_file_drop(fp, janela))
    janela.run()