from sie.database.models.aprovechamiento import Aprovechamiento
from sie.crud.aprovechamiento import create_aprovechamiento
from sie.database.connection import get_db

def register_aprovechamiento(aprovechamiento_dict: dict) -> Aprovechamiento:
    db = next(get_db())
    try:
        existing = db.query(Aprovechamiento).filter_by()
        if existing:
            raise ValueError("ocurrio un error")
        aprovechamiento = create_aprovechamiento(db,aprovechamiento_dict)
        return aprovechamiento
    finally:
        db.close()