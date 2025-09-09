from backend.database.models.rolePrivilege import RolePrivilege

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def create_rolePrivilege(db: Session, rolePrivilege_data: dict) -> RolePrivilege:
    new_rolePrivilege = RolePrivilege(**rolePrivilege_data)
    db.add(new_rolePrivilege)
    try:
        db.commit()
        db.refresh(new_rolePrivilege)
    except IntegrityError as e:
        db.rollback()
        raise ValueError(f"error:{e}")
    return new_rolePrivilege