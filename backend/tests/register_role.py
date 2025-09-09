from backend.services.role_service import register_role

new_role = {
    "role_name": "admin",
    "role_acronym": "C1",
}

try:
    role = register_role(new_role)
    print("Usuario creado con ID:", role.id_role)
except ValueError as e:
    print("Error al registrar usuario:", e)