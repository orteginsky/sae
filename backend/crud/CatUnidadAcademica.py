from backend.database.models.CatUnidadAcademica import CatUnidadAcademica
from backend.schemas.UnidadAcademica import UnidadAcademicaCreate

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from typing import Optional, Sequence, Tuple

############################__________________FUNCIONES CREATE____________________________############################
def create_unidad(db: Session, dict_unidad: UnidadAcademicaCreate) -> CatUnidadAcademica:
    new_unidad = CatUnidadAcademica(**dict_unidad.model_dump())
    db.add(new_unidad)
    try:
        db.commit()
        db.refresh(new_unidad)
    except IntegrityError:
        db.rollback()
        raise ValueError("Error en CRUD Unidad")
    return new_unidad


############################__________________FUNCIONES READ____________________________############################
def read_unit_by_initials(db: Session, sigla: str) -> Optional[CatUnidadAcademica]:
    try:
        stmt = select(CatUnidadAcademica).where(CatUnidadAcademica.Sigla == sigla)
        return db.execute(stmt).scalars().first()
    except Exception as e:
        raise ValueError(f"error en read_unit_by_initials crud: {e}")

def read_all_unidades(db: Session) -> Sequence[Tuple[int, str]]:
    stmt = select(CatUnidadAcademica.Id_Unidad_Academica, CatUnidadAcademica.Sigla).order_by(CatUnidadAcademica.Sigla)
    result = db.execute(stmt).tuples().all()
    return result
