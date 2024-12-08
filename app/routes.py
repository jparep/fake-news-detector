from flask import Blueprint, render_template, request, current_app

# Define a blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    """
    Render the home page with the input form.
    """
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    """
    Handle prediction requests and return results on the result page.
    """
    try:
        # Get input text from the form
        text = request.form.get('text', '').strip()
        if not text:
            raise ValueError("No input text provided. Please enter some text.")

        # Access model and vectorizer from app configuration
        model = current_app.config['MODEL']
        vectorizer = current_app.config['VECTORIZER']

        # Log input (only in debug mode, avoid logging sensitive input in production)
        if current_app.config["DEBUG"]:
            current_app.logger.debug(f"Input text: {text}")

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
            'probability': f"{max(prediction_proba[0]) * 100:.2f}%"  # Use max probability for clarity
        }

        # Log prediction result in debug mode
        if current_app.config["DEBUG"]:
            current_app.logger.debug(f"Prediction result: {prediction_result}")

        # Render result.html with prediction results
        return render_template('result.html', prediction=prediction_result)
    except Exception as e:
        # Log error and return to the home page with an error message
        current_app.logger.error(f"Prediction error: {e}")
        return render_template('index.html', error="An error occurred while processing your request. Please try again.")
