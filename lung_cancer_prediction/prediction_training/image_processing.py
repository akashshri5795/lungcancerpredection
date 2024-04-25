# image_processing.py
import cv2  
# installed library || pip install opencv-python
import os
from skimage.feature import greycomatrix, greycoprops 
 # installed library || pip install scikit-image

def preprocess_images(image_dir):
    for filename in os.listdir(image_dir):
        img_path = os.path.join(image_dir, filename)
        img = cv2.imread(img_path)
        img = cv2.resize(img, (100, 100))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(img_path, img)

def extract_features(image):
    glcm = greycomatrix(image, distances=[5], angles=[0], levels=256, symmetric=True, normed=True)
    contrast = greycoprops(glcm, 'contrast')
    return contrast[0, 0]
