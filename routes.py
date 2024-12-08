from flask import Flask, request, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the pre-trained model and vectorizer
model_path = os.getenv('MODEL_PATH', './models/model.joblib')
vectorizer_path = os.getenv('VECTORIZER_PATH', './models/vectorizer.joblib')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        text = request.form['text']
        if not text.strip():
            raise ValueError("No input text provided.")
        
        # Vectorize the input text
        vectorized_text = vectorizer.transform([text])

        # Make prediction
        prediction = model.predict(vectorized_text)
        prediction_proba = model.predict_proba(vectorized_text)

        # Map prediction to label
        label_map = {1: 'Fake News', 0: 'Real News'}
        prediction_label = label_map[prediction[0]]

        prediction_result = {
            'label': prediction_label,
            'probability': prediction_proba[0].tolist()
        }

        return render_template('index.html', prediction=prediction_result)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
