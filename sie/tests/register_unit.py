import sie.database.models
from sie.services.unit_service import register_unit

nueva_unidad = {
    "unit_name": "CENTRO DE ESTUDIOS CIENTIFICOS Y TECNOLOGICOS NO.1",
    "unit_acronym": "CECyT 1",
    "capacity": 4000,
    "id_entidad_federativa": 1,
    "intranet_name": "sin nombre",
    "id_branch": 1,
}

try:
    unit = register_unit(nueva_unidad)
    print("exito con el siguiente id:", unit.id_unit)
except ValueError as e:
    print(f"error en la prueba:{e}")