import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

def predict_cancer(image_path):
    # Load the trained model
    model = load_model('lung_cancer_model.h5')

    # Load and preprocess the input image
    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    # Predict the class probabilities for the input image
    predictions = model.predict(img_array)
    if predictions[0] > 0.5:
        return 'Malignant'
    else:
        return 'Benign'
