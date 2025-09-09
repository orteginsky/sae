from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db_base import Base
from datetime import datetime

class CatUnidadAcademica(Base):
    __tablename__ = 'Cat_Unidad_Academica'
    Id_Unidad_Academica = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(255), nullable=False)
    Sigla = Column(String(50), nullable=True)

class CatRol(Base):
    __tablename__ = 'Cat_Roles'
    Id_Rol = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(100), nullable=False)

class CatAltaUsuario(Base):
    __tablename__ = 'Cat_Alta_Usuario'
    Id_Usuario = Column(Integer, primary_key=True, autoincrement=True)
    Id_Unidad_Academica = Column(Integer, ForeignKey('Cat_Unidad_Academica.Id_Unidad_Academica'))
    Id_Rol = Column(Integer, ForeignKey('Cat_Roles.Id_Rol'))
    Usuario = Column(String(100), nullable=False)
    Contraseña = Column(String(100), nullable=False)
    Email = Column(String(255), nullable=False)
    Fecha_Inicio = Column(DateTime, default=datetime.today, nullable=False)
    Fecha_Modificacion = Column(DateTime, default=datetime.today, nullable=False)
    #Fecha_Final = Column(DateTime, default=datetime.utcnow, nullable=True)
    Id_Estatus = Column(Integer, default=1, nullable=False)
    # Se pueden agregar más campos según sea necesario

    unidad = relationship('CatUnidadAcademica')
    rol = relationship('CatRol')
