# model_training.py

from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(X_train, y_train, model_file_path='lung_cancer_prediction_model.pkl'):
    classifier = RandomForestClassifier(n_estimators=100) 
    classifier.fit(X_train, y_train)  
    joblib.dump(classifier, model_file_path)  
    return model_file_path
