from pydantic import BaseModel, EmailStr, Field

class UsuarioBase(BaseModel):
    Usuario: str
    Email: EmailStr

class UsuarioCreate(UsuarioBase):
    Id_Unidad_Academica: int
    Id_Rol: int
    Password: str
    Id_Estatus: int
    Nombre: str
    Paterno: str
    Materno: str
    model_config = {
        "populate_by_name": True,
    }
    
class UsuarioResponse(UsuarioBase):
    Id_Usuario: int

    model_config = {
        "from_attributes": True
    }
