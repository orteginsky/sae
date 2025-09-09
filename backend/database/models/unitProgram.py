from ..db_base import Base

from sqlalchemy import String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

"""
-- Tabla: units_programs
CREATE TABLE units_programs (
    id_unit INTEGER NOT NULL REFERENCES units(id_unit),
    id_program_modality INTEGER NOT NULL REFERENCES programs_modalities(id_program_modality),
    id_date INTEGER NOT NULL REFERENCES dates(id_date),
    modified_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id_unit, id_program_modality, id_date)
);
"""

class UnitProgram(Base):
    __tablename__ = "units_programs"

    id_unit: Mapped[int] = mapped_column(ForeignKey("units.id_unit"), primary_key=True)
    id_program_modality: Mapped[int] = mapped_column(ForeignKey("programs_modalities.id_program_modality"), primary_key=True)
    id_date: Mapped[int] = mapped_column(ForeignKey("dates.id_date"), primary_key=True)
    modified_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    
