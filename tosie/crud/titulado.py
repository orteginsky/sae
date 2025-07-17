from tosie.database.models.titulado import Titulado

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def create_titulado(db: Session, titulado_data: dict) -> Titulado:
    new_titulado = Titulado(**titulado_data)
    db.add(new_titulado)
    try:
        db.commit()
        db.refresh(new_titulado)
    except IntegrityError as e:
        db.rollback()
        raise ValueError(f"error:{e}")
    return new_titulado