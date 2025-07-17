from sqlalchemy.orm import Session
from tosie.database.models.branch import Branch
from sqlalchemy.exc import IntegrityError

def create_branch(db: Session, branch_data: dict) -> Branch:
    new_branch = Branch(**branch_data)
    db.add(new_branch)
    try:
        db.commit()
        db.refresh(new_branch)
    except IntegrityError:
        db.rollback()
        raise ValueError("El registro ya existe o los datos no son válidos.")
    return new_branch
