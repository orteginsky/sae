from tosie.database.connection import get_db
from tosie.database.models.modality import Modality
from tosie.crud.modality import create_modality

def register_modality(modality_data: dict) -> Modality:
    db = next(get_db())
    try:
        existing = db.query(Modality).filter_by().first()
        if existing:
            raise ValueError("ya existe dicha información")
        modality = create_modality(db=db, modality_data=modality_data)
        return modality
    finally:
        db.close()