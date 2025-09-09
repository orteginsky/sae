# auth_user.py
# Clase User para integración con Flask-Login

from flask_login import UserMixin
from db import SessionLocal
from models import CatAltaUsuario

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

    @staticmethod
    def get(user_id):
        session = SessionLocal()
        try:
            usuario = session.query(CatAltaUsuario).filter_by(Id_Usuario=user_id).first()
            if usuario:
                return User(usuario.Id_Usuario, usuario.Usuario)
        finally:
            session.close()
        return None
