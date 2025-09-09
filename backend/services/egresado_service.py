from backend.database.connection import get_db
from backend.database.models.egresado import Egresado
from backend.crud.egresado import create_egresado

def register_egresado(egresado_dict: dict) -> Egresado:
    db = next(get_db())
    try:
        existing = db.query(Egresado).filter_by().first()
        if existing:
            raise ValueError("ocurrio un error en egresado_service.py")
        egresado = create_egresado(egresado_dict)
        return egresado
    finally:
        db.close()