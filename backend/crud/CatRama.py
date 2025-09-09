from backend.database.models.CatRama import CatRama

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def create_rama(db: Session, dict_rama:dict) -> CatRama:
    new_Rama = CatRama(**dict_rama)
    db.add(new_Rama)
    try:
        db.commit()
        db.refresh(new_Rama)
    except IntegrityError:
        db.rollback()
        raise ValueError("La información introducida es incorrecta o ya existe")
    return new_Rama
