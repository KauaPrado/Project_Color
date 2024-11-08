import numpy as np
from sklearn.cluster import KMeans

def get_dominant_color(image, k=4):
    pixels = image.reshape((-1, 3))
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_
    labels = kmeans.labels_
    
    counts = np.bincount(labels)
    dominant_color = colors[np.argmax(counts)]
    
    return dominant_color.astype(int)
