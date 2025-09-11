from backend.database.models.CatRoles import CatRoles
from backend.crud.CatRoles import create_rol, read_role_by_name, read_all_names_roles, read_id_by_name, read_all_roles
from backend.schemas.Roles import RolesCreate, RolesResponse

from sqlalchemy.orm import Session

def role_already_exists(db: Session, role_name: str) -> bool:
    role = read_role_by_name(db,role_name)
    validation = role is not None
    return  validation

def register_role(db: Session,role_dict: RolesCreate) -> CatRoles:
    try:
        if role_already_exists(db=db, role_name=role_dict.Nombre):
            raise ValueError("role already exist")
        role = create_rol(db, role_dict)
        return role
    finally:
        db.close()

def get_all_roles(db: Session) -> list[RolesResponse]:
    roles = read_all_roles(db)
    return [RolesResponse.model_validate(r) for r in roles]
