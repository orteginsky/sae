from db import SessionLocal
from models import CatRol

def obtener_roles():
    session = SessionLocal()
    try:
        return session.query(CatRol).all()
    finally:
        session.close()

def crear_rol(nombre):
    session = SessionLocal()
    try:
        nuevo = CatRol(Nombre=nombre)
        session.add(nuevo)
        session.commit()
        return nuevo
    finally:
        session.close()

def actualizar_rol(id_rol, nombre):
    session = SessionLocal()
    try:
        rol = session.query(CatRol).filter_by(Id_Rol=id_rol).first()
        if rol:
            rol.Nombre = nombre
            session.commit()
            return rol
        return None
    finally:
        session.close()

def eliminar_rol(id_rol):
    session = SessionLocal()
    try:
        rol = session.query(CatRol).filter_by(Id_Rol=id_rol).first()
        if rol:
            session.delete(rol)
            session.commit()
            return True
        return False
    finally:
        session.close()
