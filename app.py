from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model and vectorizer
model = joblib.load('./models/model.joblib')
vectorizer = joblib.load('./models/vectorizer.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
