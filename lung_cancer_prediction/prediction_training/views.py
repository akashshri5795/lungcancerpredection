# views.py

from django.shortcuts import render
from .image_processing import preprocess_images, extract_features
from .model_training import train_model
import joblib

def upload_image(request):
    # Placeholder code for uploading image
    return render(request, 'upload_image.html')

def predict_lung_cancer(request):
    if request.method == 'POST':
        image = request.FILES['image']
        preprocess_images('media/')
        features = extract_features(image)
        classifier = joblib.load('lung_cancer_prediction_model.pkl')
        prediction = classifier.predict([features])    
        return render(request, 'prediction_result.html', {'prediction': prediction})
    else:
        return render(request, 'upload_image.html')
