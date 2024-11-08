import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def load_image(image_path):
    image = cv2.imread(image_path)
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

def plot_image(image):
    plt.imshow(image)
    plt.axis('off')
    plt.show()

def plot_color(color):
    plt.figure(figsize=(2, 2))
    plt.axis('off')
    plt.imshow([[color]])
    plt.show()

image_path = 'imagens\\mayday_parade.jpg'  # Substitua pelo caminho da sua imagem
image = load_image(image_path)
plot_image(image)

dominant_color = get_dominant_color(image, k=3)
print(f'A cor predominante é: {dominant_color}')

plot_color(dominant_color)
