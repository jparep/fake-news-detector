import os
from flask import Flask
from dotenv import load_dotenv
import joblib
import logging

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

    # Configure logging
    logging.basicConfig(level=logging.DEBUG if app.config["DEBUG"] else logging.INFO)
    logger = logging.getLogger(__name__)

    # Validate required environment variables
    required_vars = ["SECRET_KEY", "MODEL_PATH", "VECTORIZER_PATH"]
    missing_vars = [var for var in required_vars if not app.config.get(var)]
    if missing_vars:
        raise RuntimeError(f"Missing required environment variables: {', '.join(missing_vars)}")

    # Load model and vectorizer
    try:
        app.config["MODEL"] = joblib.load(app.config["MODEL_PATH"])
        logger.info(f"Model loaded from {app.config['MODEL_PATH']}")
    except Exception as e:
        raise RuntimeError(f"Failed to load model from {app.config['MODEL_PATH']}: {e}")

    try:
        app.config["VECTORIZER"] = joblib.load(app.config["VECTORIZER_PATH"])
        logger.info(f"Vectorizer loaded from {app.config['VECTORIZER_PATH']}")
    except Exception as e:
        raise RuntimeError(f"Failed to load vectorizer from {app.config['VECTORIZER_PATH']}: {e}")

    # Register the blueprint for application routes
    from .routes import main
    app.register_blueprint(main)

    return app
