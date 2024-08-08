# Fake News Detector

A Flask-based web API for detecting fake news using a machine learning model. This project utilizes scikit-learn and transformers to classify news articles as fake or real. The application is deployed on Heroku with continuous integration via GitHub.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Environment Variables](#environment-variables)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Fake News Detector is a web API designed to classify news articles as fake or real. The API leverages a pre-trained machine learning model, which is served through a Flask application. This project is ideal for those looking to understand or utilize machine learning for text classification tasks.

## Features

- **Fake News Detection**: Classifies input text as fake or real news.
- **RESTful API**: Easy-to-use API for integration with other services.
- **Continuous Deployment**: Automatically deploys updates to Heroku when changes are pushed to GitHub.
- **Scalable**: Deployed on Heroku with support for scaling and monitoring.

## Installation

### Prerequisites

- Python 3.12+
- Git
- Virtualenv

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/fake-news-detector.git
   cd fake-news-detector


2. **Create a virtual environment:**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install dependencies:**:
    ```bash
    pip install -r requirements.txt

4. **Set up environment variables**:
    Create a .env file in the root directory and set the necessary environment variables as per the Environment Variables section.

5. **Run the application locally**:
    ```bash
    flask run
The API will be accessible at http://127.0.0.1:5000/.

6. **Usage***:
Making Predictions

Once the API is running, you can make predictions by sending a POST request to the /predict endpoint with a JSON payload containing the text you want to classify.

Deployment

The application is deployed on Heroku using the GitHub integration. Every time changes are pushed to the main branch, Heroku automatically builds and deploys the latest version.
Manual Deployment

To manually deploy the application:
    ```bash
    git push heroku main


Continuous Deployment

Continuous deployment is configured through the Heroku dashboard. For more details, refer to the Heroku documentation.
Environment Variables

The application requires the following environment variables:

    FLASK_ENV: The environment in which the Flask app is running (e.g., production, development).
    DEBUG: Whether to run the Flask app in debug mode (True or False).
    SECRET_KEY: A secret key for Flask sessions.

These can be set in an .env file or through the Heroku dashboard for production.

### Project Structure

fake-news-detector/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── Procfile                  # Heroku process file
├── runtime.txt               # Specifies Python version
├── app.json                  # Heroku app setup
├── models/                   # Directory for model files
│   ├── model.joblib
│   └── vectorizer.joblib
├── templates/
│   └── index.html            # HTML template for the web interface (if applicable)
├── .gitignore                # Git ignore rules
└── README.md                 # Project documentation

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request. Ensure that your code follows the PEP 8 guidelines and includes appropriate tests.


# License

This project is licensed under the MIT License. See the LICENSE file for details.