from flask_app import app
from src.views.app import user

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)