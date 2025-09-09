from ..db_base import Base

from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

"""
-- Tabla: modalities
CREATE TABLE modalities (
    id_modality INTEGER PRIMARY KEY,
    modality_name VARCHAR(128) NOT NULL,
    modality_acronym VARCHAR(64) NOT NULL,
    modified_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
"""

class Modality(Base):
    __tablename__ = "modalities"

    id_modality: Mapped[int] = mapped_column(primary_key=True, index=True)
    modality_name: Mapped[str] = mapped_column(String(128), nullable=False)
    modality_acronym: Mapped[str] = mapped_column(String(64), nullable=False)
    modified_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    