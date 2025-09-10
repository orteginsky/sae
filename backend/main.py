#backend.sie.py
from backend.api import user
from backend.api import registro
from backend.api import validaciones
from backend.core.templates import templates, static

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import os


app = FastAPI()
app.mount("/static", static)
app.include_router(user.router, prefix="/users")
app.include_router(registro.router, prefix="/registro")
app.include_router(validaciones.router , prefix="/login")


# Redirigir raíz a portada
@app.get("/", response_class=HTMLResponse)
async def root():
    return RedirectResponse(url="/portada")

@app.get("/portada", response_class=HTMLResponse)
async def portada(request: Request):
    return templates.TemplateResponse("portada.html", {"request": request})
