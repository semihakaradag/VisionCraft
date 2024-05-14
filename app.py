import numpy as np
from flask import Flask, render_template, request, send_file
import cv2
import os
from graydonusum import custom_gray_conversion
from rotate import custom_rotate
from zoom_in_out import zoom_in_out
from crop import crop_image



app = Flask(__name__)

# Ana sayfa
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Kullanıcıdan resmi al
        uploaded_image = request.files['image']
        image_path = os.path.join('static', 'uploaded_image.jpg')
        uploaded_image.save(image_path)
       
        # Seçilen işlem
        selected_operation = request.form['operation']

        # Resmi işle
        image = cv2.imread(image_path)
        if selected_operation == 'gray':
            processed_image = custom_gray_conversion(image)
        elif selected_operation == 'binary':
            _, processed_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
        elif selected_operation == 'rotate':
            angle = 45  # İsteğe bağlı olarak dönüş açısını buradan ayarlayabilirsiniz
            processed_image = custom_rotate(image, angle)
        elif selected_operation == 'crop':
           # Kırpma işlemi için gerekli parametreleri alın
            start_x = int(request.form['start_x'])
            end_x = int(request.form['end_x'])
            start_y = int(request.form['start_y'])
            end_y = int(request.form['end_y'])
            image = cv2.imread(image_path)
            cropped_image = crop_image(image, start_x, start_y, end_x, end_y)
        
            # Kırpılmış resmi kaydet
            cropped_image_path = os.path.join('static', 'cropped_image.png')
            cropped_image.save(cropped_image_path)
        
            return render_template('index.html', image_path=image_path, cropped_image_path=cropped_image_path)
        elif selected_operation == 'zoom':
            zoom_factor = 2  # Görüntüyü %50 daha büyük göster
            processed_image = zoom_in_out(image, zoom_factor)
        elif selected_operation == 'color_space':
            processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        elif selected_operation == 'histogram_stretch':
            processed_image = cv2.equalizeHist(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
        elif selected_operation == 'arithmetic':
            processed_image = cv2.addWeighted(image, 0.7, cv2.imread(image_path), 0.3, 0)
        elif selected_operation == 'brightness':
            processed_image = cv2.convertScaleAbs(image, alpha=1.5, beta=50)
        elif selected_operation == 'convolution':
            kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
            processed_image = cv2.filter2D(image, -1, kernel)
        elif selected_operation == 'thresholding':
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, processed_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        elif selected_operation == 'edge_detection':
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            processed_image = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
        elif selected_operation == 'noise':
            processed_image = image.copy()
            rows, cols, _ = processed_image.shape
            for _ in range(500):
                x = np.random.randint(0, rows)
                y = np.random.randint(0, cols)
                processed_image[x, y] = 255
        elif selected_operation == 'blurring':
            processed_image = cv2.GaussianBlur(image, (5, 5), 0)
        elif selected_operation == 'dilation':
            kernel = np.ones((5, 5), np.uint8)
            processed_image = cv2.dilate(image, kernel, iterations=1)
        elif selected_operation == 'erosion':
            kernel = np.ones((5, 5), np.uint8)
            processed_image = cv2.erode(image, kernel, iterations=1)
        elif selected_operation == 'opening':
            kernel = np.ones((5, 5), np.uint8)
            processed_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
        elif selected_operation == 'closing':
            kernel = np.ones((5, 5), np.uint8)
            processed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        else:
            processed_image = image  # İşlem yapılmadan orijinal resmi göster

        # İşlenmiş resmi kaydet
        processed_image_path = os.path.join('static', 'processed_image.jpg')
        cv2.imwrite(processed_image_path, processed_image)

        return render_template('index.html', image_path=image_path, processed_image_path=processed_image_path)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)