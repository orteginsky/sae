import reflex as rx
from ..services.auth_service import verificar_usuario

class LoginState(rx.State):
    username: str = ""
    password: str = ""
    error: str = ""
    logged_in: bool = False

    @rx.event
    def set_username(self, value: str):
        self.username = value

    @rx.event
    def set_password(self, value: str):
        self.password = value

    @rx.event
    def login(self):
        if verificar_usuario(self.username, self.password):
            self.logged_in = True
            return rx.redirect("/")
        else:
            self.error = "Usuario o contraseña incorrectos"
    
def goto_create_user():
    return rx.redirect("/create")

def page():
    return rx.center(
        rx.vstack(
            rx.heading("Iniciar sesión"),
            rx.input(placeholder="Usuario", on_change=LoginState.set_username),
            rx.input(placeholder="Contraseña", type_="password", on_change=LoginState.set_password),
            rx.button("Ingresar", on_click=LoginState.login),
            rx.button("Crear un Nuevo Usuario", on_click=goto_create_user),
            rx.cond(LoginState.error != "", rx.text(LoginState.error, color="red")),
            spacing="4",
            width="300px"
        ),
        min_height="100vh"
    )
