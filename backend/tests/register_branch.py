from backend.services.branch_service import register_branch
#"id_branch": 1,
nueva_rama = {
    "branch_name": "Ingeniería en Ciencias Físico Matemáticas",
    "acronym_branch": "ICFM",
}

try:
    branch = register_branch(nueva_rama)
    print("exito con id",branch.id_branch)
except ValueError as e:
    print(f"ocurrio un error:{e}")