import sie.database.models
from sie.services.user_service import register_user

new_user_data = {
    "username": "lortegar",
    "first_name": "luis",
    "paternal_surname": "ortega",
    "maternal_surname": "ramirez",
    "password": "contraseñasegura",
    "id_role": 1,
    "email": "luis@email.com",
    "id_unit": 1,
}

try:
    user = register_user(new_user_data)
    print("Usuario creado con ID:", user.id_user)
except ValueError as e:
    print("Error al registrar usuario:", e)