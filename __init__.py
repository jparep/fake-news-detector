import os
from flask import Flask
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def create_app():
    # Initialize the Flask application
    app = Flask(__name__)
    
    # Use the environment variable "SECRET_KEY" or a fallback value for local development
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "fallback-secret-key")  # Fixed typo in "fallback-secret-key"
    
    # Import and register the blueprint for application routes
    from .routes import main
    app.register_blueprint(main)
    
    return app
