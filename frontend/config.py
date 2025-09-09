# config.py
# Configuración de la aplicación Flask y LoginManager

import os
from flask import Flask
from flask_login import LoginManager
from registro import registro_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'clave_insegura')
    app.register_blueprint(registro_bp)
    return app

def create_login_manager(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Debe apuntar al endpoint del blueprint
    return login_manager
