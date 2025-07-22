from sie.database.connection import get_db
from sie.database.models.sex import Sex
from sie.crud.sex import create_sex

def register_sex(sex_data:dict) -> Sex:
    db = next(get_db())
    try:
        existing = db.query(Sex).filter_by().first()
        if existing:
            raise ValueError("no mi shavo, ya existe ese sexo")
        sex = create_sex(db,sex_data)
        return sex
    finally:
        db.close()

