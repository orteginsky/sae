from backend.database.connection import get_db
from backend.database.models.program import Program
from backend.crud.program import create_program

def register_program(program_data:dict) -> Program:
    db = next(get_db())
    try:
        existing = db.query(Program).filter_by().first()
        if existing:
            raise ValueError("the program is already exist")
        program = create_program(db, program_data)
        return program
    finally:
        db.close()