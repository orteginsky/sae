from db import SessionLocal
from models import CatAltaUsuario, CatUnidadAcademica, CatRol
from sqlalchemy import text

# Ejemplo CRUD con ORM

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

# Ejemplo de consulta con ORM

def obtener_usuarios():
    session = SessionLocal()
    try:
        return session.query(CatAltaUsuario).all()
    finally:
        session.close()

# Ejemplo de ejecución de stored procedure

def ejecutar_stored_procedure(nombre_proc, params):
    session = SessionLocal()
    try:
        # params debe ser una lista o tupla de parámetros en orden
        sql = f"EXEC {nombre_proc} " + ','.join(['?' for _ in params])
        result = session.execute(text(sql), params)
        return result.fetchall()
    finally:
        session.close()

# Uso ejemplo:
# crear_usuario('usuario1', 'pass', 'mail@mail.com', 1, 1)
# usuarios = obtener_usuarios()
# resultado_sp = ejecutar_stored_procedure('NombreDeSP', (param1, param2))
