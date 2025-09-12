#backend.main.py
from backend.api import registro
from backend.api import login
from backend.api import index
from backend.api import usuarios
from backend.core.templates import static

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()
app.mount("/static", static)
app.include_router(registro.router, prefix="/registro")
app.include_router(login.router , prefix="/login")
app.include_router(index.router , prefix="/index")
app.include_router(usuarios.router , prefix="/usuarios")

@app.get("/", response_class=HTMLResponse)
async def root():
    return RedirectResponse(url="/index")