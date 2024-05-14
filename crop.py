from PIL import Image
import numpy as np

def crop_image(image_path, left, upper, right, lower):
    # Resmi aç
    image = Image.open(image_path)
    
    # Resmi numpy dizisine dönüştür
    image_array = np.array(image)
    
    # Belirtilen bölgeyi kırpmak
    cropped_image_array = image_array[upper:lower, left:right]
    
    # Kırpılmış resmi numpy dizisinden PIL görüntüsüne dönüştür
    cropped_image = Image.fromarray(cropped_image_array)
    
    # Kırpılmış resmi döndür
    return cropped_image

