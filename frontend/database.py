# database.py
"""
Módulo para la configuración y conexión a la base de datos SQL Server usando SQLAlchemy y pyodbc.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import urllib


# Importar configuración centralizada
from .config import DB_SERVER, DB_NAME, DB_USER, DB_PASSWORD

# Construcción de la cadena de conexión para SQL Server con pyodbc
params = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={DB_SERVER};DATABASE={DB_NAME};UID={DB_USER};PWD={DB_PASSWORD}"
)
SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"


# Creación del engine y la sesión con autocommit habilitado
engine = create_engine(SQLALCHEMY_DATABASE_URL, isolation_level="AUTOCOMMIT")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos ORM
Base = declarative_base()

def get_db():
    """
    Generador de sesiones de base de datos para inyección de dependencias en FastAPI.
    Uso: incluir como dependencia en los endpoints.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
