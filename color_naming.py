import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Dicionário de cores estendido
COLOR_NAMES = {
    (240, 248, 255): "alice blue",
    (250, 235, 215): "antique white",
    (0, 255, 255): "aqua",
    (127, 255, 212): "aquamarine",
    (240, 255, 255): "azure",
    (245, 245, 220): "beige",
    (255, 228, 196): "bisque",
    (0, 0, 0): "black",
    (255, 235, 205): "blanched almond",
    (0, 0, 255): "blue",
    (138, 43, 226): "blue violet",
    (165, 42, 42): "brown",
    (222, 184, 135): "burly wood",
    (95, 158, 160): "cadet blue",
    (127, 255, 0): "chartreuse",
    (210, 105, 30): "chocolate",
    (255, 127, 80): "coral",
    (100, 149, 237): "cornflower blue",
    (255, 248, 220): "cornsilk",
    (220, 20, 60): "crimson",
    (0, 255, 255): "cyan",
    (0, 0, 139): "dark blue",
    (0, 139, 139): "dark cyan",
    (184, 134, 11): "dark goldenrod",
    (169, 169, 169): "dark gray",
    (0, 100, 0): "dark green",
    (189, 183, 107): "dark khaki",
    (139, 0, 139): "dark magenta",
    (85, 107, 47): "dark olive green",
    (255, 140, 0): "dark orange",
    (153, 50, 204): "dark orchid",
    (139, 0, 0): "dark red",
    (233, 150, 122): "dark salmon",
    (143, 188, 143): "dark sea green",
    (72, 61, 139): "dark slate blue",
    (47, 79, 79): "dark slate gray",
    (0, 206, 209): "dark turquoise",
    (148, 0, 211): "dark violet",
    (255, 20, 147): "deep pink",
    (0, 191, 255): "deep sky blue",
    (105, 105, 105): "dim gray",
    (30, 144, 255): "dodger blue",
    (178, 34, 34): "firebrick",
    (255, 250, 240): "floral white",
    (34, 139, 34): "forest green",
    (255, 0, 255): "fuchsia",
    (220, 220, 220): "gainsboro",
    (248, 248, 255): "ghost white",
    (255, 215, 0): "gold",
    (218, 165, 32): "goldenrod",
    (128, 128, 128): "gray",
    (0, 128, 0): "green",
    (173, 255, 47): "green yellow",
    (240, 255, 240): "honeydew",
    (255, 105, 180): "hot pink",
    (205, 92, 92): "indian red",
    (75, 0, 130): "indigo",
    (255, 255, 240): "ivory",
    (240, 230, 140): "khaki",
    (230, 230, 250): "lavender",
    (255, 240, 245): "lavender blush",
    (124, 252, 0): "lawn green",
    (255, 250, 205): "lemon chiffon",
    (173, 216, 230): "light blue",
    (240, 128, 128): "light coral",
    (224, 255, 255): "light cyan",
    (250, 250, 210): "light goldenrod yellow",
    (211, 211, 211): "light gray",
    (144, 238, 144): "light green",
    (255, 182, 193): "light pink",
    (255, 160, 122): "light salmon",
    (32, 178, 170): "light sea green",
    (135, 206, 250): "light sky blue",
    (119, 136, 153): "light slate gray",
    (176, 196, 222): "light steel blue",
    (255, 255, 224): "light yellow",
    (0, 255, 0): "lime",
    (50, 205, 50): "lime green",
    (250, 240, 230): "linen",
    (255, 0, 255): "magenta",
    (128, 0, 0): "maroon",
    (102, 205, 170): "medium aquamarine",
    (0, 0, 205): "medium blue",
    (186, 85, 211): "medium orchid",
    (147, 112, 219): "medium purple",
    (60, 179, 113): "medium sea green",
    (123, 104, 238): "medium slate blue",
    (0, 250, 154): "medium spring green",
    (72, 209, 204): "medium turquoise",
    (199, 21, 133): "medium violet red",
    (25, 25, 112): "midnight blue",
    (245, 255, 250): "mint cream",
    (255, 228, 225): "misty rose",
    (255, 228, 181): "moccasin",
    (255, 222, 173): "navajo white",
    (0, 0, 128): "navy",
    (253, 245, 230): "old lace",
    (128, 128, 0): "olive",
    (107, 142, 35): "olive drab",
    (255, 165, 0): "orange",
    (255, 69, 0): "orange red",
    (218, 112, 214): "orchid",
    (238, 232, 170): "pale goldenrod",
    (152, 251, 152): "pale green",
    (175, 238, 238): "pale turquoise",
    (219, 112, 147): "pale violet red",
    (255, 239, 213): "papaya whip",
    (255, 218, 185): "peach puff",
    (205, 133, 63): "peru",
    (255, 192, 203): "pink",
    (221, 160, 221): "plum",
    (176, 224, 230): "powder blue",
    (128, 0, 128): "purple",
    (255, 0, 0): "red",
    (188, 143, 143): "rosy brown",
    (65, 105, 225): "royal blue",
    (139, 69, 19): "saddle brown",
    (250, 128, 114): "salmon",
    (244, 164, 96): "sandy brown",
    (46, 139, 87): "sea green",
    (255, 245, 238): "seashell",
    (160, 82, 45): "sienna",
    (192, 192, 192): "silver",
    (135, 206, 235): "sky blue",
    (106, 90, 205): "slate blue",
    (112, 128, 144): "slate gray",
    (255, 250, 250): "snow",
    (0, 255, 127): "spring green",
    (70, 130, 180): "steel blue",
    (210, 180, 140): "tan",
    (0, 128, 128): "teal",
    (216, 191, 216): "thistle",
    (255, 99, 71): "tomato",
    (64, 224, 208): "turquoise",
    (238, 130, 238): "violet",
    (245, 222, 179): "wheat",
    (255, 255, 255): "white",
    (245, 245, 245): "white smoke",
    (255, 255, 0): "yellow",
    (154, 205, 50): "yellow green"
    
}

def closest_color(requested_color):
    min_colors = {}
    for color, name in COLOR_NAMES.items():
        rd = (color[0] - requested_color[0]) ** 2
        gd = (color[1] - requested_color[1]) ** 2
        bd = (color[2] - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

def get_color_name(rgb_color):
    return closest_color(rgb_color)

def load_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Não foi possível abrir ou encontrar a imagem no caminho: {image_path}")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def get_dominant_color(image, k=3):
    pixels = image.reshape((-1, 3))
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_
    labels = kmeans.labels_
    
    counts = np.bincount(labels)
    dominant_color = colors[np.argmax(counts)]
    
    return dominant_color.astype(int)

def plot_color(color):
    plt.figure(figsize=(2, 2))
    plt.axis('off')
    plt.imshow([[color]])
    plt.show()

def upload_image():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    try:
        image = load_image(file_path)
        plot_image(image)
        dominant_color = get_dominant_color(image)
        color_name = get_color_name(dominant_color)
        result_label.config(text=f'Cor predominante: {color_name} - {dominant_color}')
        result_label.config(bg=f'#{dominant_color[0]:02x}{dominant_color[1]:02x}{dominant_color[2]:02x}')
        plot_color(dominant_color)
    except Exception as e:
        result_label.config(text=f"Erro: {e}", bg="red")

def plot_image(image):
    plt.imshow(image)
    plt.axis('off')
    plt.show()

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
