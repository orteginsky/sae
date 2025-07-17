import bcrypt


def verificar_usuario(username: str, password: str) -> bool:
    usuario = get_usuario_by_username(username)
    if usuario and bcrypt.checkpw(password.encode(), usuario.password.encode()):
        return True
    return False
