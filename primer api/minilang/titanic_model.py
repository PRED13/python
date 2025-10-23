import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import requests
import joblib
import os

class TitanicModel:
    def __init__(self):
        self.model = None
        self.le_sex = LabelEncoder()
        self.model_path = 'titanic_model.joblib'
        self.encoder_path = 'sex_encoder.joblib'
        
    def download_and_prepare_data(self):
        # Usar archivo local para el dataset
        local_path = r"C:\Users\Pred\Desktop\pruebas\archive\train.csv"
        if not os.path.exists(local_path):
            raise Exception(f"No se encontró el archivo de datos: {local_path}")
        df = pd.read_csv(local_path)
        # Preprocesamiento
        self.le_sex.fit(df['Sex'])  # Entrenar el encoder
        df['Sex'] = self.le_sex.transform(df['Sex'])
        # Guardar el encoder
        joblib.dump(self.le_sex, self.encoder_path)
        # Seleccionar características relevantes
        features = ['Pclass', 'Sex', 'Age', 'Fare']
        X = df[features].fillna(df[features].mean())
        y = df['Survived']
        return X, y
    
    def train_model(self):
        # Obtener datos
        X, y = self.download_and_prepare_data()
        
        # Dividir datos
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Crear y entrenar modelo
        self.model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
        self.model.fit(X_train, y_train)
        
        # Calcular accuracy
        accuracy = self.model.score(X_test, y_test)
        print(f"Accuracy del modelo: {accuracy:.2f}")
        
        # Guardar modelo
        joblib.dump(self.model, self.model_path)
        
    def load_model(self):
        if os.path.exists(self.model_path) and os.path.exists(self.encoder_path):
            self.model = joblib.load(self.model_path)
            self.le_sex = joblib.load(self.encoder_path)
        else:
            self.train_model()
    
    def predict_survival(self, pclass, sex, age, fare):
        if self.model is None:
            self.load_model()
            
        # Preparar datos
        try:
            sex_encoded = self.le_sex.transform([sex])[0]
            features = np.array([[pclass, sex_encoded, age, fare]])
            
            # Hacer predicción
            prediction = self.model.predict(features)[0]
            probability = self.model.predict_proba(features)[0][1]
        except ValueError as e:
            # Si el encoder no está entrenado, entrenar el modelo
            self.train_model()
            return self.predict_survival(pclass, sex, age, fare)
        
        return {
            'survived': bool(prediction),
            'probability': float(probability),
            'passenger_info': {
                'class': int(pclass),
                'sex': sex,
                'age': float(age),
                'fare': float(fare)
            }
        }