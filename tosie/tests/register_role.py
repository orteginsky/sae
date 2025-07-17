from tosie.services.role_service import register_role

new_role = {
    "id_role": 2,
    "role_name": "prueba",
    "role_acronym": "p1",
}

try:
    role = register_role(new_role)
    print("Usuario creado con ID:", role.id_role)
except ValueError as e:
    print("Error al registrar usuario:", e)

