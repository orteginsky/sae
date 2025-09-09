from db import SessionLocal
from models import CatAltaUsuario
from sqlalchemy import text

def crear_usuario(usuario, contrasena, email, id_unidad, id_rol):
    session = SessionLocal()
    try:
        nuevo = CatAltaUsuario(
            Usuario=usuario,
            Contraseña=contrasena,
            Email=email,
            Id_Unidad_Academica=id_unidad,
            Id_Rol=id_rol
        )
        session.add(nuevo)
        session.commit()
        return nuevo
    finally:
        session.close()

def obtener_usuario_por_usuario_o_email(usuario_o_email):
    session = SessionLocal()
    try:
        return session.query(CatAltaUsuario).filter(
            ((CatAltaUsuario.Usuario == usuario_o_email) | (CatAltaUsuario.Email == usuario_o_email)) & (CatAltaUsuario.Id_Estatus != 3)
        ).first()
    finally:
        session.close()

def actualizar_usuario(id_usuario, **kwargs):
    session = SessionLocal()
    from datetime import datetime
    try:
        usuario = session.query(CatAltaUsuario).filter_by(Id_Usuario=id_usuario, Id_Estatus=1).first()
        if not usuario:
            return None
        for key, value in kwargs.items():
            setattr(usuario, key, value)
        usuario.Fecha_Modificacion = datetime.now()
        session.commit()
        return usuario
    finally:
        session.close()

def eliminar_usuario(id_usuario):
    session = SessionLocal()
    from datetime import datetime
    try:
        usuario = session.query(CatAltaUsuario).filter_by(Id_Usuario=id_usuario, Id_Estatus=1).first()
        if usuario:
            usuario.Id_Estatus = 3  # Borrado lógico
            if hasattr(usuario, 'Fecha_Final'):
                usuario.Fecha_Final = datetime.now()
            else:
                # Si el modelo no tiene Fecha_Final, agregarlo dinámicamente (no recomendado, pero fallback)
                setattr(usuario, 'Fecha_Final', datetime.now())
            session.commit()
            return True
        return False
    finally:
        session.close()

def validar_usuario_existente(usuario):
    session = SessionLocal()
    try:
        # Solo valida usuarios que no estén eliminados
        existe = session.query(CatAltaUsuario).filter(CatAltaUsuario.Usuario == usuario, CatAltaUsuario.Id_Estatus != 3).first()
        return existe is not None
    finally:
        session.close()
