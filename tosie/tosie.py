import reflex as rx
from .pages import login
#from .pages import create_user
from .database.init import init_db

init_db()

app = rx.App()
app.add_page(login.page, route="/login", title="Login")
#app.add_page(create_user.page, route="/create", title="Create New User")