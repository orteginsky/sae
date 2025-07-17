from ..db_base import Base

from sqlalchemy import Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

"""
-- Tabla: dates
CREATE TABLE dates (
    id_date INTEGER PRIMARY KEY,
    anio INTEGER,
    semestre INTEGER,
    trimestre INTEGER,
    inicio_periodo TIMESTAMP,
    fin_periodo TIMESTAMP,
    modified_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
"""

class Date(Base):
    __tablename__ = "dates"

    id_date: Mapped[int] = mapped_column(primary_key=True, index=True)
    anio: Mapped[int] = mapped_column(Integer, nullable=False)
    semestre: Mapped[int] = mapped_column(Integer, nullable=False)
    trimestre: Mapped[int] = mapped_column(Integer, nullable=False)
    inicio_periodo: Mapped[datetime] = mapped_column(DateTime)
    fin_periodo: Mapped[datetime] = mapped_column(DateTime)
    modified_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    