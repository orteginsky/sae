from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Configuración de rutas para archivos estáticos y plantillas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Redirigir la raíz a la portada
@app.get("/", response_class=HTMLResponse)
async def root():
    return RedirectResponse(url="/portada")

# Endpoint para la portada principal
@app.get("/portada", response_class=HTMLResponse)
async def portada(request: Request):
    return templates.TemplateResponse("portada.html", {"request": request})

# Registrar routers
from frontend.routers import validaciones
app.include_router(validaciones.router)