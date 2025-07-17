from database.models.basica import Basica

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def create_basica(db: Session, basica_data: dict)->Basica:
    new_basica = Basica(**basica_data)
    db.add(new_basica)
    try:
        db.commit
        db.refresh(new_basica)
    except IntegrityError as e:
        db.rollback()
        raise ValueError(f"la información ingresada es incorrecta ocurrio un error: {e}")
    return new_basica