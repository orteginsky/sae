from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import os

DATABASE_URL = "mssql+pyodbc://sa:Ainigriv.5@148.204.107.44:1433/SII_DII?driver=ODBC+Driver+17+for+SQL+Server"
#DATABASE_URL = "mssql+pyodbc://miriam:contrasena@148.204.107.35:1433/SII_DII?driver=ODBC+Driver+17+for+SQL+Server"
#DATABASE_URL = "mssql+pyodbc://ortega:7w0zXODLCRb3DR9@localhost/SIE?driver=ODBC+Driver+17+for+SQL+Server"
#DATABASE_URL = "mssql+pyodbc://@localhost/SIE?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"
#DATABASE_URL = "postgresql://admin:PT1BYVNDttdnpwfVzU9c@localhost:5432/sie"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

if __name__ == "__main__":
    db = SessionLocal()
    try:
        result=db.execute(text("SELECT 1"))
        print("La conexión fue exitosa",result.scalar())
    except Exception as e:
        print(f"error en main de db_config:{e}")