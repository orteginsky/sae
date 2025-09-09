from backend.database.db_base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, func, ForeignKey

from datetime import datetime

"""
-- Tabla: programs_modalities
CREATE TABLE programs_modalities (
    id_program_modality SERIAL PRIMARY KEY,
    id_program INTEGER NOT NULL REFERENCES programs(id_program),
    id_modality INTEGER NOT NULL REFERENCES modalities(id_modality),
    start_date INTEGER NOT NULL REFERENCES dates(id_date),
    cancellation_date INTEGER NOT NULL REFERENCES dates(id_date),
    modified_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
"""

class ProgramModality(Base):
    __tablename__ = "programs_modalities"

    id_program_modality: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_program: Mapped[int] = mapped_column(ForeignKey("programs.id_program"))
    id_modality: Mapped[int] = mapped_column(ForeignKey("modalities.id_modality"))
    start_date: Mapped[int] = mapped_column(ForeignKey("dates.id_date"))
    cancellation_date: Mapped[int] = mapped_column(ForeignKey("dates.id_date"))
    modified_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
