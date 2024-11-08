import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from image_processing import load_image
from color_analysis import get_dominant_color
from color_naming import get_color_name

def upload_image():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    try:
        image = load_image(file_path)
        dominant_color = get_dominant_color(image)
        color_name = get_color_name(dominant_color)
        result_label.config(text=f'Cor predominante: {color_name} - {dominant_color}')
        result_label.config(bg=f'#{dominant_color[0]:02x}{dominant_color[1]:02x}{dominant_color[2]:02x}')
    except Exception as e:
        result_label.config(text=f"Erro: {e}", bg="red")

def create_ui():
    root = tk.Tk()
    root.title("Detecção de Cor Predominante")

    upload_button = ttk.Button(root, text="Carregar Imagem", command=upload_image)
    upload_button.pack(pady=20)

    global result_label
    result_label = tk.Label(root, text="Resultado", width=50, height=10)
    result_label.pack(pady=20)

    root.mainloop()

create_ui()
