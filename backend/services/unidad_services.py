from backend.database.models.CatUnidadAcademica import CatUnidadAcademica
from backend.database.connection import get_db
from backend.crud.CatUnidadAcademica import create_unidad, read_all_unidades
from backend.schemas.UnidadAcademica import UnidadAcademicaCreate, UnidadAcademicaResponse

from sqlalchemy.orm import Session

def unidad_already_exists(db: Session):
    return 0

def get_all_units(db: Session) -> list[dict]:
    roles = read_all_unidades(db)
    return [r[1] for r in roles]
    #return [{"id": r[0], "nombre": r[1]} for r in roles]
