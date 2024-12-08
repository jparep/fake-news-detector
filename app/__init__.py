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

    # Set the secret key from environment variables
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    if not app.config["SECRET_KEY"]:
        raise RuntimeError("SECRET_KEY is missing! Add it to your .env file or environment variables.")

    # Load model and vectorizer paths from environment variables
    app.config["MODEL_PATH"] = os.getenv("MODEL_PATH")
    app.config["VECTORIZER_PATH"] = os.getenv("VECTORIZER_PATH")

    # Validate required environment variables
    required_vars = ["MODEL_PATH", "VECTORIZER_PATH"]
    missing_vars = [var for var in required_vars if not app.config.get(var)]
    if missing_vars:
        app.logger.error(f"Missing required environment variables: {', '.join(missing_vars)}")
        raise RuntimeError("Application configuration is incomplete. Check your .env file.")

    # Import and register the blueprint for application routes
    from .routes import main
    app.register_blueprint(main)

    # Return the Flask app instance
    return app
