from flask import Blueprint, render_template, request, current_app

# Define a blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    """
    Render the home page.
    """
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    """
    Handle prediction requests and return results.
    """
    try:
        # Get input text from the form
        text = request.form.get('text', '').strip()
        if not text:
            raise ValueError("No input text provided.")

        # Access model and vectorizer from app configuration
        model = current_app.config['MODEL']
        vectorizer = current_app.config['VECTORIZER']

        # Vectorize the input text
        vectorized_text = vectorizer.transform([text])

        # Make prediction
        prediction = model.predict(vectorized_text)
        prediction_proba = model.predict_proba(vectorized_text)

        # Map prediction to label
        label_map = {1: 'Fake News', 0: 'Real News'}
        prediction_label = label_map[prediction[0]]

        # Prepare result
        prediction_result = {
            'label': prediction_label,
            'probability': prediction_proba[0].tolist()
        }

        # Render template with prediction results
        return render_template('index.html', prediction=prediction_result)
    except Exception as e:
        # Log error and return error message
        current_app.logger.error(f"Prediction error: {e}")
        return render_template('index.html', error=str(e))
