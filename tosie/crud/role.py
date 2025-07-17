from sqlalchemy.orm import Session
from tosie.database.models.role import Role
from sqlalchemy.exc import IntegrityError

def create_role(db: Session, role_data: dict) -> Role:
    new_role = Role(**role_data)
    db.add(new_role)
    try:
        db.commit()
        db.refresh(new_role)
    except IntegrityError as e:
        db.rollback()
        raise ValueError(f"El registro ya existe o los datos no son válidos. el erro de integridad es el siguiente: {e.orig}")
    return new_role
