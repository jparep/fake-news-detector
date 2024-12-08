import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Fetch the port from environment variables, default to 5000 if not provided
    port = int(os.getenv("PORT", 5000))
    debug = app.config["DEBUG"]
    app.run(host="0.0.0.0", port=port, debug=debug)
