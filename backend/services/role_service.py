from backend.database.connection import get_db
from backend.database.models.role import Role
from backend.crud.role import create_role

def role_already_exists(db, role_name: str) -> bool:
    return db.query(Role).filter(
        (Role.role_name == role_name)
    ).first() is not None

def register_role(role_dict: dict) -> Role:
    db = next(get_db())
    try:
        if role_already_exists(db=db, role_name=role_dict['role_name']):
            raise ValueError("role already exist")
        role = create_role(db, role_dict)
        return role
    finally:
        db.close()
