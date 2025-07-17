from tosie.database.models.egresado import Egresado

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def create_egresado(db: Session, egresado_data: dict) -> Egresado:
    new_egresado = Egresado(**egresado_data)
    db.add(new_egresado)
    try:
        db.commit()
        db.refresh(new_egresado)
    except IntegrityError as e:
        db.rollback()
        raise ValueError(f"error:{e}")
    return new_egresado