from sqlalchemy.orm import Session
from sie.database.models.user import User
from sqlalchemy.exc import IntegrityError

def create_user(db: Session, user_data: dict) -> User:
    new_user = User(**user_data)
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback()
        raise ValueError("El usuario ya existe o los datos no son válidos.")
    return new_user

def get_user_by_username(db: Session, username: str) -> User | None:
    return db.query(User).filter_by(username=username).first()