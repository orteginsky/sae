from tosie.crud.unit import create_unit
from tosie.database.connection import get_db

nueva_unidad = {
    "unit_name": "CENTRO DE ESTUDIOS CIENTIFICOS Y TECNOLOGICOS NO.1",
    "unit_acronym": "CECyT 1",
    "capacity": 4000,
    "id_entidad_federativa": 1,
    "intranet_name": "sin nombre",
    "id_branch": 1,
}

db = next(get_db())

try:
    unit = create_unit(db, nueva_unidad)
    print(unit.id_unit)
except:
    print("error tests")
finally:
    db.close()