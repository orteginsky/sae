from ..db_base import Base

from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

"""
-- Tabla: sexes
CREATE TABLE sexes (
    id_sex INTEGER PRIMARY KEY,
    sex_name VARCHAR(64) NOT NULL,
    sex_acronym VARCHAR(32) NOT NULL,
    modified_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
"""

class Sex(Base):
    __tablename__ = "sexes"

    id_sex: Mapped[int] = mapped_column(primary_key=True, index=True)
    sex_name: Mapped[int] = mapped_column(String(64), nullable=False)
    sex_acronym: Mapped[int] = mapped_column(String(32), nullable=False)
    modified_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    