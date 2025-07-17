from tosie.database.connection import get_db
from tosie.database.models.role import Role
from tosie.crud.role import create_role

def register_role(role_dict: dict) -> Role:
    db = next(get_db())
    try:
        existing = db.query(Role).filter_by().first()
        if existing:
            raise ValueError("role already exist")
        role = create_role(db, role_dict)
        return role
    finally:
        db.close()