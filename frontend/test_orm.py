
from db import SessionLocal
from models import CatAltaUsuario, CatUnidadAcademica, CatRol

session = SessionLocal()
try:
    # Consulta con join para mostrar nombre de unidad y rol
    results = session.query(
        CatAltaUsuario.Id_Usuario,
        CatAltaUsuario.Usuario,
        CatAltaUsuario.Email,
        CatUnidadAcademica.Nombre.label('Unidad'),
        CatRol.Nombre.label('Rol')
    ).join(CatUnidadAcademica, CatAltaUsuario.Id_Unidad_Academica == CatUnidadAcademica.Id_Unidad_Academica)
    results = results.join(CatRol, CatAltaUsuario.Id_Rol == CatRol.Id_Rol).all()
    for row in results:
        print(f"ID: {row.Id_Usuario} | Usuario: {row.Usuario} | Email: {row.Email} | Unidad: {row.Unidad} | Rol: {row.Rol}")
finally:
    session.close()