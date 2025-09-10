from fastapi import APIRouter

router = APIRouter()

@router.get("/auth/")
async def autenticacion(data: dict):
    return "hola"
