from tosie.services.user_service import register_user
import reflex as rx

class CreateState(rx.State):
    first_name: str = ""
    paternal_surname: str = ""
    maternal_surname: str = ""
    username: str = ""
    email: str = ""
    password: str = ""
    confirmed_password: str = ""
    error_msg: str = ""
    error_status: bool = False

    @rx.event
    def create(self):
        if not all([self.first_name, self.paternal_surname, self.username, self.email, self.password, self.confirmed_password]):
            self.error_msg = "Todos los campos son obligatorios."
            self.error_status = True
            return

        if self.password != self.confirmed_password:
            self.error_msg = "Las contraseñas no coinciden."
            self.error_status = True
            return
        
        self.error_status = False

        try:
            new_user_data = {
            "username": self.username,
            "first_name": self.first_name,
            "paternal_surname": self.paternal_surname,
            "maternal_surname": self.maternal_surname,
            "password": self.password,
            "id_role": 1,
            "email": self.email,
            "id_unit": 1,
            }
            user = register_user(new_user_data)
            print("Usuario creado con ID:", user.id_user)
        except:
            raise ValueError("usuario ya registrado")

        return rx.redirect("/")


def page():
    return rx.center(
        rx.vstack(
            rx.heading("Registrar Nuevo Usuario"),
            rx.input(placeholder="Nombres", on_change=CreateState.set_first_name),
            rx.input(placeholder="Apellido Paterno", on_change=CreateState.set_paternal_surname),
            rx.input(placeholder="Apellido Materno", on_change=CreateState.set_maternal_surname),
            rx.input(placeholder="Nombre de Usuario", on_change=CreateState.set_username),
            rx.input(placeholder="Correo Electrónico", on_change=CreateState.set_email),
            rx.input(placeholder="Contraseña", type_="password", on_change=CreateState.set_password),
            rx.input(placeholder="Confirmar Contraseña", type_="password", on_change=CreateState.set_confirmed_password),
            rx.button("Registrar", on_click=CreateState.create),
            rx.cond(CreateState.error_status, rx.text(CreateState.error_msg, color="red")),
            spacing="4",
            width="300px",
        ),
        min_height="100vh"
    )

