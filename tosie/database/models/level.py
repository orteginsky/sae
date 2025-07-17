from ..db_base import Base

from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

"""
-- Tabla: levels
CREATE TABLE levels (
    id_level INTEGER PRIMARY KEY,
    level_name VARCHAR(128) NOT NULL,
    acronym_level VARCHAR(64) NOT NULL,
    modified_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
"""

class Level(Base):
    __tablename__ = "levels"

    id_level: Mapped[int] = mapped_column(primary_key=True, index=True)
    level_name: Mapped[str] = mapped_column(String(128), nullable=False)
    acronym_level: Mapped[str] = mapped_column(String(64), nullable=False)
    modified_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    