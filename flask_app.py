from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate

from config import config
from src.db_models import db as db_model




def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    
    db_model.init_app(app)
    
    migrate = Migrate(app, db_model)
    
    from src.views.blueprint import blueprint_tiktok
    app.register_blueprint(blueprint_tiktok)
    
    return app, db_model

app, db = create_app()