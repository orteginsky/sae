
# app.py
# Punto de entrada principal. Arranca la app Flask, registra blueprints y expone get_db_connection.

import pyodbc
import os
from config import create_app, create_login_manager
from routes.auth import bp as auth_bp
from auth_user import User

app = create_app()
login_manager = create_login_manager(app)
app.register_blueprint(auth_bp)

# Registrar el user_loader después de crear login_manager
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

def get_db_connection():
    """Devuelve una conexión a la base de datos SQL Server."""
    conn_str = (
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={os.environ.get('DB_SERVER', '148.204.107.22')};"
        f"DATABASE={os.environ.get('DB_NAME', 'Base_pruebas')};"
        f"UID={os.environ.get('DB_USER', 'sa')};"
        f"PWD={os.environ.get('DB_PASSWORD', 'emmanuel280900')};"
        f"TrustServerCertificate=yes;"
    )
    conn = pyodbc.connect(conn_str)
    return conn

if __name__ == '__main__':
    app.run(debug=True)