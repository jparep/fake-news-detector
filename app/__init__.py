import os
from flask import Flask
from dotenv import load_dotenv
import joblib

# Load environment variables from .env
load_dotenv()

def create_app():
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)

    # Set configurations from environment variables
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["MODEL_PATH"] = os.getenv("MODEL_PATH")
    app.config["VECTORIZER_PATH"] = os.getenv("VECTORIZER_PATH")
    app.config["DEBUG"] = os.getenv("DEBUG", "False").lower() == "true"

    # Validate required environment variables
    required_vars = ["SECRET_KEY", "MODEL_PATH", "VECTORIZER_PATH"]
    missing_vars = [var for var in required_vars if not app.config.get(var)]
    if missing_vars:
        raise RuntimeError(f"Missing required environment variables: {', '.join(missing_vars)}")

    # Load model and vectorizer
    app.config["MODEL"] = joblib.load(app.config["MODEL_PATH"])
    app.config["VECTORIZER"] = joblib.load(app.config["VECTORIZER_PATH"])

    # Import and register the blueprint for application routes
    from .routes import main
    app.register_blueprint(main)

    return app
