import os
from flask import Flask
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def create_app():
    """
    Factory function to create and configure the Flask application.
    """

    # Initialize the Flask application
    app = Flask(__name__)

    # Set the secret key from environment variables or fallback for local development
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "fallback-secret-key")

    # Best Practice: Validate critical environment variables
    if app.config["SECRET_KEY"] == "fallback-secret-key":
        app.logger.warning("Using fallback secret key. Set SECRET_KEY in .env for production.")

    # Additional configuration can be loaded from environment variables
    app.config["MODEL_PATH"] = os.getenv("MODEL_PATH")
    app.config["VECTORIZER_PATH"] = os.getenv("VECTORIZER_PATH")

    # Best Practice: Validate required environment variables
    required_vars = ["MODEL_PATH", "VECTORIZER_PATH"]
    for var in required_vars:
        if not app.config.get(var):
            raise RuntimeError(f"Environment variable {var} is missing. Check your .env file.")

    # Import and register the blueprint for application routes
    from .routes import main
    app.register_blueprint(main)

    # Return the Flask app instance
    return app
