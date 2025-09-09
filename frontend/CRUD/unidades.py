from db import SessionLocal
from models import CatUnidadAcademica

def obtener_unidades():
    session = SessionLocal()
    try:
        return session.query(CatUnidadAcademica).all()
    finally:
        session.close()

def crear_unidad(nombre):
    session = SessionLocal()
    try:
        nueva = CatUnidadAcademica(Nombre=nombre)
        session.add(nueva)
        session.commit()
        return nueva
    finally:
        session.close()

def actualizar_unidad(id_unidad, nombre):
    session = SessionLocal()
    try:
        unidad = session.query(CatUnidadAcademica).filter_by(Id_Unidad_Academica=id_unidad).first()
        if unidad:
            unidad.Nombre = nombre
            session.commit()
            return unidad
        return None
    finally:
        session.close()

def eliminar_unidad(id_unidad):
    session = SessionLocal()
    try:
        unidad = session.query(CatUnidadAcademica).filter_by(Id_Unidad_Academica=id_unidad).first()
        if unidad:
            session.delete(unidad)
            session.commit()
            return True
        return False
    finally:
        session.close()
