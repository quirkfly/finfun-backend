from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from openai import OpenAI
from config import OPENAI_API_KEY

db = SQLAlchemy()

openai_client = OpenAI(api_key=OPENAI_API_KEY)

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    CORS(app)

    from .routes import assistant_bp
    app.register_blueprint(assistant_bp, url_prefix='/api/assistant')

    return app
